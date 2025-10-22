# ============================================================
# scripts/ops_to_cq_full.py
#
# SketchGraphs OPS  ➜  CadQuery code generator (2D + simple extrusion)
# - Preserves lines + arcs (no polyline approximation)
# - Uses SN_* markers + coincident sets to snap endpoints
# - Curve-preserving greedy loop assembly with tiny-gap bridging
# - Filters degenerate (zero/tiny) segments to avoid OCCT failures
# - Writes a runnable CadQuery script: <dir>/<stem>_cq.py
#
# Usage:
#   python3 scripts/ops_to_cq_full.py filtered_dataset/.../seq_xxxx/ops.json
# ============================================================

import os, sys, json, math
from collections import defaultdict, Counter
from typing import List, Tuple, Dict, Optional, Set

# ------------ knobs / tolerances ------------
SCALE            = 1000.0        # meters -> mm
TARGET_SPAN_MM   = 100.0         # normalize span to <= this (0 disables)
ANG_EPS          = 1e-6
SNAP_TOL_SEQ     = [(0.6, 0.6), (1.5, 1.2), (3.0, 2.0), (5.0, 3.0)]  # (snap, bridge)
MIN_SEG_MM       = 1e-4          # drop segments shorter than this
EPS_MM           = 1e-6
EXTRUDE_MM       = 3.0           # default thin extrusion in generated code
DEBUG            = True

# ------------ debug print ------------
def dprint(*a, **k):
    if DEBUG:
        print(*a, **k)

# ============================================================
# 1) OPS parsing + pre-normalization (center + optional rescale)
# ============================================================

def load_ops(path: str) -> List[dict]:
    with open(path, "r") as f:
        data = json.load(f)
    return data["ops"] if isinstance(data, dict) and "ops" in data else data

def collect_points_m(ops: List[dict]) -> List[Tuple[float,float]]:
    pts = []
    for d in ops:
        if d.get("kind") != "NodeOp": continue
        lab = d.get("label"); p = d.get("parameters", {}) or {}
        try:
            if lab == "Line":
                px, py = float(p["pntX"]), float(p["pntY"])
                dx, dy = float(p["dirX"]), float(p["dirY"])
                a,  b  = float(p["startParam"]), float(p["endParam"])
                pts.append((px + dx*a, py + dy*a))
                pts.append((px + dx*b, py + dy*b))
            elif lab == "Arc":
                cx, cy = float(p["xCenter"]), float(p["yCenter"])
                r      = float(p["radius"])
                xd, yd = float(p.get("xDir", 1.0)), float(p.get("yDir", 0.0))
                t0, t1 = float(p["startParam"]), float(p["endParam"])
                base   = math.atan2(yd, xd)
                a0, a1 = base + t0, base + t1
                pts += [
                    (cx + r*math.cos(a0), cy + r*math.sin(a0)),
                    (cx + r*math.cos(a1), cy + r*math.sin(a1)),
                    (cx, cy),
                ]
            elif lab == "Circle":
                cx, cy = float(p["xCenter"]), float(p["yCenter"])
                r      = float(p["radius"])
                pts += [(cx, cy), (cx + r, cy)]
        except Exception:
            pass
    return pts

def make_normalizer(ops: List[dict]):
    pts = collect_points_m(ops)
    if not pts:
        return (lambda x, y: (x, y)), 1.0, (0.0, 0.0)

    xs, ys = zip(*pts)
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    cx, cy     = (xmin + xmax)/2.0, (ymin + ymax)/2.0
    span_m     = max(xmax - xmin, ymax - ymin) or 1.0

    if TARGET_SPAN_MM > 0:
        span_mm      = span_m * SCALE
        scale_factor = min(1.0, TARGET_SPAN_MM / span_mm) if span_mm > TARGET_SPAN_MM else 1.0
    else:
        scale_factor = 1.0

    def norm(x, y):
        return (x - cx) * scale_factor, (y - cy) * scale_factor

    dprint(f"[pre-norm] center(m)=({cx:.6f},{cy:.6f}), span(m)={span_m:.6f}, rescale={scale_factor:.4f}")
    return norm, scale_factor, (cx, cy)

# ============================================================
# 2) Build edge specs (mm, centered) + track SN_* markers
# ============================================================

# we keep edges as specs, not CadQuery objects, e.g.:
#   ('line', (x0,y0,0), (x1,y1,0))
#   ('arc',  (x0,y0,0), (xm,ym,0), (x1,y1,0))
# separate list for full circles: { "c": (cx,cy,0), "r": r }

SN_MAP: Dict[int, Tuple[float,float,float]] = {}
_last_curve = {"start": None, "end": None, "center": None}

def remember_curve_endpoints_mm(p0, p1, params: dict, is_arc: bool, norm):
    global _last_curve
    _last_curve["start"] = (p0[0], p0[1], 0.0)
    _last_curve["end"]   = (p1[0], p1[1], 0.0)
    if is_arc:
        try:
            cx, cy = float(params["xCenter"]), float(params["yCenter"])
            ncx, ncy = norm(cx, cy)
            _last_curve["center"] = (ncx*SCALE, ncy*SCALE, 0.0)
        except Exception:
            _last_curve["center"] = None
    else:
        _last_curve["center"] = None

def record_sn(op_index: int, tag: str):
    v = None
    if tag == "SN_Start":    v = _last_curve["start"]
    elif tag == "SN_End":    v = _last_curve["end"]
    elif tag == "SN_Center": v = _last_curve["center"]
    if v is not None:
        SN_MAP[op_index] = v

def line_spec_mm(p: dict, norm):
    if p.get("isConstruction"): return None
    try:
        px, py = float(p["pntX"]), float(p["pntY"])
        dx, dy = float(p["dirX"]), float(p["dirY"])
        a,  b  = float(p["startParam"]), float(p["endParam"])
        x0, y0 = px + dx*a, py + dy*a
        x1, y1 = px + dx*b, py + dy*b
        nx0, ny0 = norm(x0, y0); nx1, ny1 = norm(x1, y1)
        p0 = (nx0*SCALE, ny0*SCALE, 0.0)
        p1 = (nx1*SCALE, ny1*SCALE, 0.0)
        remember_curve_endpoints_mm((p0[0],p0[1]), (p1[0],p1[1]), p, False, norm)
        return ('line', p0, p1)
    except Exception:
        return None

def arc_spec_mm(p: dict, norm):
    if p.get("isConstruction"): return None
    try:
        cx, cy = float(p["xCenter"]), float(p["yCenter"])
        r      = float(p["radius"])
        xd, yd = float(p.get("xDir", 1.0)), float(p.get("yDir", 0.0))
        t0, t1 = float(p["startParam"]), float(p["endParam"])
        if abs(t1 - t0) < ANG_EPS:
            t1 = t0 + 1e-3
        base = math.atan2(yd, xd)
        a0, a1 = base + t0, base + t1
        if a1 <= a0: a1 += 2*math.pi
        def P(a):
            x = cx + r*math.cos(a); y = cy + r*math.sin(a)
            nx, ny = norm(x, y)
            return (nx*SCALE, ny*SCALE, 0.0)
        p0, pm, p1 = P(a0), P((a0+a1)/2.0), P(a1)
        remember_curve_endpoints_mm((p0[0],p0[1]), (p1[0],p1[1]), p, True, norm)
        return ('arc', p0, pm, p1)
    except Exception:
        return None

def circle_entry_mm(p: dict, norm):
    if p.get("isConstruction"): return None
    try:
        cx, cy = float(p["xCenter"]), float(p["yCenter"])
        r      = float(p["radius"])
        ncx, ncy = norm(cx, cy)
        return {"c": (ncx*SCALE, ncy*SCALE, 0.0), "r": r*SCALE}
    except Exception:
        return None

def build_specs_mm(ops: List[dict]):
    global SN_MAP, _last_curve
    SN_MAP.clear()
    _last_curve = {"start": None, "end": None, "center": None}
    norm, _, _ = make_normalizer(ops)

    edges_specs, circles = [], []
    for idx, d in enumerate(ops):
        if d.get("kind") != "NodeOp": continue
        lab = d.get("label"); p = d.get("parameters", {}) or {}
        if   lab == "Line":
            s = line_spec_mm(p, norm);   edges_specs += [s] if s else []
        elif lab == "Arc":
            s = arc_spec_mm(p, norm);    edges_specs += [s] if s else []
        elif lab == "Circle":
            c = circle_entry_mm(p, norm); circles += [c] if c else []
        elif lab in ("SN_Start","SN_End","SN_Center"):
            record_sn(idx, lab)
    return edges_specs, circles

# ============================================================
# 3) Coincident graph → component anchors (for snapping)
# ============================================================

def parse_ref_tuple(s: str) -> Tuple[int, int]:
    t = s.strip().strip("()")
    a, b = t.split(",")
    return int(a.strip()), int(b.strip())

def build_coincident_anchor_map(ops: List[dict]) -> Dict[int, Tuple[float,float,float]]:
    adj: Dict[int, Set[int]] = defaultdict(set)
    for d in ops:
        if d.get("kind") == "EdgeOp" and d.get("label") == "Coincident":
            try:
                ai, bi = parse_ref_tuple(d.get("references", "(, )"))
                adj[ai].add(bi); adj[bi].add(ai)
            except Exception:
                pass

    visited: Set[int] = set()
    anchor_map: Dict[int, Tuple[float,float,float]] = {}

    def dfs(start: int, comp: List[int]):
        stack = [start]
        while stack:
            u = stack.pop()
            if u in visited: continue
            visited.add(u)
            if u in SN_MAP: comp.append(u)
            for v in adj[u]:
                if v not in visited:
                    stack.append(v)

    for seed in list(adj.keys()):
        if seed in visited: continue
        comp: List[int] = []
        dfs(seed, comp)
        pts = [SN_MAP[i] for i in comp if i in SN_MAP]
        if pts:
            cx = sum(p[0] for p in pts)/len(pts)
            cy = sum(p[1] for p in pts)/len(pts)
            anchor = (cx, cy, 0.0)
            for i in comp: anchor_map[i] = anchor
    return anchor_map

# ============================================================
# 4) Curve-preserving loop assembly  (FIXED + degenerate filter)
# ============================================================

def _dist(a, b):
    dx = a[0]-b[0]; dy = a[1]-b[1]; dz = a[2]-b[2]
    return (dx*dx + dy*dy + dz*dz)**0.5

def _key(v, tol):
    return (round(v[0]/tol), round(v[1]/tol))

def _nearest_sn_anchor(v, sn_points, tol):
    if not sn_points:
        return v
    sn_vec, anc = min(sn_points, key=lambda pair: _dist(v, pair[0]))
    return anc if _dist(v, sn_vec) <= max(tol, 0.6) else v

def _valid_line(p0, p1):
    return _dist(p0, p1) > MIN_SEG_MM

def _valid_arc(p0, pm, p1):
    return (_dist(p0, p1) > MIN_SEG_MM and
            _dist(p0, pm) > MIN_SEG_MM and
            _dist(pm, p1) > MIN_SEG_MM)

def assemble_loops_specs(edges_specs: List[tuple], sn_points: List[Tuple[tuple, tuple]]):
    """
    edges_specs: [('line', p0, p1) or ('arc', p0, pm, p1)] in mm
    sn_points:   [(sn_vec, anchor_vec)] for snapping to coincident components

    Returns: list of LOOPS; each loop is a list of items:
      ('line', p0, p1) or ('arc', p0, pm, p1)
    """
    loops_all: List[List[tuple]] = []

    for tol, bridge in SNAP_TOL_SEQ:
        # -- snap endpoints to anchors, drop degenerates early
        snapped = []
        buckets = defaultdict(list)

        for it in edges_specs:
            if it[0] == 'line':
                _, P0, P1 = it
                A = _nearest_sn_anchor(P0, sn_points, tol)
                B = _nearest_sn_anchor(P1, sn_points, tol)
                if _valid_line(A, B):
                    snapped.append(('line', A, B))
                    buckets[_key(A, tol)].append(A); buckets[_key(B, tol)].append(B)
            else:
                _, P0, PM, P1 = it
                A = _nearest_sn_anchor(P0, sn_points, tol)
                M = PM
                B = _nearest_sn_anchor(P1, sn_points, tol)
                if _valid_arc(A, M, B):
                    snapped.append(('arc', A, M, B))
                    buckets[_key(A, tol)].append(A); buckets[_key(B, tol)].append(B)

        # adjacency: node -> incident edge indices
        adj = defaultdict(list)
        for i, it in enumerate(snapped):
            if it[0] == 'line':
                _, A, B = it
            else:
                _, A, _, B = it
            adj[_key(A, tol)].append(i)
            adj[_key(B, tol)].append(i)

        globally_used: Set[int] = set()

        def add_connector(chain: List[tuple], p, q):
            if _dist(p, q) <= bridge and _valid_line(p, q):
                chain.append(('line', p, q))
                return True
            return False

        # try growing loops from every edge (both orientations), but
        # commit edges to 'used' ONLY when a loop closes
        for start_idx in range(len(snapped)):
            if start_idx in globally_used:
                continue

            for start_from_A in (True, False):
                locally_used: Set[int] = set()
                chain: List[tuple] = []

                # seed
                it0 = snapped[start_idx]
                if it0[0] == 'line':
                    _, A0, B0 = it0
                else:
                    _, A0, M0, B0 = it0
                start_node = _key(A0, tol) if start_from_A else _key(B0, tol)
                first_point = A0 if start_from_A else B0
                cur_edge = start_idx
                cur_from_A = start_from_A
                cur_point = first_point
                steps = 0
                closed = False

                while steps < 5000:
                    steps += 1
                    if cur_edge in locally_used or cur_edge in globally_used:
                        break
                    locally_used.add(cur_edge)

                    it = snapped[cur_edge]
                    if it[0] == 'line':
                        _, A, B = it
                        A2, B2 = (A, B) if cur_from_A else (B, A)
                        if chain and _dist(chain[-1][-1], A2) > EPS_MM:
                            if not add_connector(chain, chain[-1][-1], A2):
                                break
                        chain.append(('line', A2, B2))
                        cur_point = B2
                    else:
                        _, A, M, B = it
                        A2, M2, B2 = (A, M, B) if cur_from_A else (B, M, A)
                        if chain and _dist(chain[-1][-1], A2) > EPS_MM:
                            if not add_connector(chain, chain[-1][-1], A2):
                                break
                        chain.append(('arc', A2, M2, B2))
                        cur_point = B2

                    # arrived back to start node?
                    if len(chain) >= 3 and _key(cur_point, tol) == start_node:
                        if _dist(chain[-1][-1], first_point) > EPS_MM:
                            if not add_connector(chain, chain[-1][-1], first_point):
                                break
                        closed = True
                        break

                    # choose next unused edge at current node
                    k_cur = _key(cur_point, tol)
                    nxt = None
                    for idx2 in adj[k_cur]:
                        if idx2 in locally_used or idx2 in globally_used:
                            continue
                        it2 = snapped[idx2]
                        if it2[0] == 'line':
                            _, a2, b2 = it2
                            if _key(a2, tol) == k_cur: nxt = (idx2, True);  break
                            if _key(b2, tol) == k_cur: nxt = (idx2, False); break
                        else:
                            _, a2, m2, b2 = it2
                            if _key(a2, tol) == k_cur: nxt = (idx2, True);  break
                            if _key(b2, tol) == k_cur: nxt = (idx2, False); break

                    if nxt is None:
                        # try to close with tiny bridge
                        if len(chain) >= 3 and add_connector(chain, chain[-1][-1], first_point):
                            closed = True
                        break

                    cur_edge, cur_from_A = nxt

                if closed and len(chain) >= 3:
                    loops_all.append(chain)
                    globally_used.update(locally_used)
                    break  # no need to try other orientation for this start

        if loops_all:
            dprint(f"assemble_loops_specs: closed {len(loops_all)} loop(s) with tol={tol}, bridge={bridge}")
            break

    return loops_all

# ============================================================
# 5) Generate a runnable CadQuery script (_cq.py)
# ============================================================

GENERATED_TEMPLATE = """\
# ============================================================
# Auto-generated CadQuery reconstruction from:
#   {src}
#
# Rebuilds 2D sketch (lines, arcs, circles), assembles closed
# loops with tiny-gap bridging, builds faces (outer + holes),
# and extrudes the largest face by EXTRUDE_HEIGHT_MM.
# ============================================================
import cadquery as cq
from cadquery import Vector, Edge, Wire, Face

EXTRUDE_HEIGHT_MM = {extrude_height:.3f}

DEBUG = True
def dprint(*a, **k):
    if DEBUG: print(*a, **k)

# tiny guards
EPS_MM = {eps}
MIN_SEG_MM = {min_seg}

def _vlen(p, q):
    dx = p[0]-q[0]; dy = p[1]-q[1]; dz = p[2]-q[2]
    return (dx*dx + dy*dy + dz*dz)**0.5

def _valid_line(p0, p1): return _vlen(p0, p1) > MIN_SEG_MM
def _valid_arc(p0, pm, p1):
    return (_vlen(p0, p1) > MIN_SEG_MM and
            _vlen(p0, pm) > MIN_SEG_MM and
            _vlen(pm, p1) > MIN_SEG_MM)

# ---- 1) Edge/circle specs ----
LOOPS = {loops}

CIRCLES = {circles}

# ---- 2) Build CQ edges ----
def build_edges_from_loop(loop):
    edges = []
    for item in loop:
        if item[0] == 'line':
            _, p0, p1 = item
            if not _valid_line(p0, p1): 
                continue
            edges.append(Edge.makeLine(Vector(*p0), Vector(*p1)))
        else:
            _, p0, pm, p1 = item
            if not _valid_arc(p0, pm, p1): 
                continue
            edges.append(Edge.makeThreePointArc(Vector(*p0), Vector(*pm), Vector(*p1)))
    return edges

# ---- 3) Assemble wires ----
def loop_to_wire(loop):
    edges = build_edges_from_loop(loop)
    if len(edges) < 3:
        dprint("loop_to_wire: too few edges:", len(edges))
        return []
    try:
        return Wire.makeWire(edges)
    except Exception as e:
        dprint("Wire.makeWire failed:", e)
        try:
            ww = Wire.assembleEdges(edges)
            if isinstance(ww, list): 
                return [wi for wi in ww if wi]
            return [ww] if ww else []
        except Exception as e2:
            dprint("Wire.assembleEdges failed:", e2)
            return []

def build_all_wires():
    wires = []
    for loop in LOOPS:
        w = loop_to_wire(loop)
        if not w: continue
        if isinstance(w, list):
            wires.extend(w)
        else:
            wires.append(w)
    for c in CIRCLES:
        cx, cy, cz = c["c"]; r = c["r"]
        try:
            wires.append(Wire.makeCircle(r, Vector(cx, cy, cz), Vector(0,0,1)))
        except Exception as e:
            dprint("Circle wire fail:", e)
    return wires

# ---- 4) Faces + extrude ----
def nest_wires(wires):
    pairs, taken = [], set()
    for i, w in enumerate(wires):
        if i in taken: continue
        try:
            oface = Face.makeFromWires(w)
        except Exception:
            continue
        holes = []
        for j, h in enumerate(wires):
            if j == i or j in taken: continue
            try:
                if oface.isInside(h.startPoint(), 1e-6, True):
                    holes.append(h); taken.add(j)
            except Exception:
                pass
        pairs.append((w, holes))
    return pairs

def build_faces(wires):
    faces = []
    for outer, holes in nest_wires(wires):
        try:
            faces.append(Face.makeFromWires(outer, holes if holes else None))
        except Exception:
            try: faces.append(Face.makeFromWires(outer))
            except Exception: pass
    return faces

def extrude_largest(faces):
    if not faces: return None, None
    areas = [(i, abs(f.Area())) for i, f in enumerate(faces)]
    areas.sort(key=lambda t: t[1], reverse=True)
    i0 = areas[0][0]
    try:
        solid = cq.Workplane("XY").add(faces[i0]).extrude(EXTRUDE_HEIGHT_MM)
        for i, _ in areas[1:]:
            try:
                tool = cq.Workplane("XY").add(faces[i]).extrude(99.0, both=True)
                solid = solid.cut(tool)
            except Exception as e:
                dprint("Cut failed for face", i, e)
        return solid, i0
    except Exception as e:
        dprint("Extrude failed:", e)
        return None, None

# ---- 5) Run ----
wires = build_all_wires()
faces = build_faces(wires)
solid, main_face_idx = extrude_largest(faces)

print({{"edges_from_loops": sum(len(l) for l in LOOPS), "n_wires": len(wires), "n_faces": len(faces), "solid": bool(solid)}})

try:
    for i, w in enumerate(wires): show_object(w, name=f"wire_{{i}}")
    for i, f in enumerate(faces): show_object(f, name=f"face_{{i}}", options={{"alpha": 0.4}})
    if solid is not None: show_object(solid, name="solid")
except Exception:
    pass
"""

def write_generated_script(out_py: str, loops: List[List[tuple]], circles: List[dict], src: str):
    payload = GENERATED_TEMPLATE.format(
        src=os.path.abspath(src),
        extrude_height=EXTRUDE_MM,
        eps=EPS_MM,
        min_seg=MIN_SEG_MM,
        loops=repr(loops),
        circles=repr(circles),
    )
    with open(out_py, "w") as f:
        f.write(payload)

# ============================================================
# 6) Top-level: ops.json -> build specs -> assemble loops -> write _cq.py
# ============================================================

def main(ops_path: str):
    ops = load_ops(ops_path)
    labs = Counter([d.get("label") for d in ops if d.get("kind") == "NodeOp"])
    dprint("NodeOp labels:", labs)

    edges_specs, circles = build_specs_mm(ops)
    anchor_map = build_coincident_anchor_map(ops)
    if anchor_map:
        comps = len(set(map(id, anchor_map.values())))
        dprint(f"Anchor components: {comps} comps, {len(anchor_map)} SN→anchor mappings")

    # SN points for snapping: (sn_vec, component_anchor)
    sn_points = [(SN_MAP[i], anchor_map.get(i, SN_MAP[i])) for i in SN_MAP]

    loops = assemble_loops_specs(edges_specs, sn_points)

    out_dir = os.path.dirname(os.path.abspath(ops_path))
    stem   = os.path.splitext(os.path.basename(ops_path))[0]
    out_py = os.path.join(out_dir, f"{stem}_cq.py")
    write_generated_script(out_py, loops, circles, ops_path)

    print({
        "input": ops_path,
        "output_py": out_py,
        "n_loops": len(loops),
        "n_circles": len(circles),
        "extrude_mm": EXTRUDE_MM,
    })

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/ops_to_cq_full.py /path/to/ops.json")
        sys.exit(1)
    main(sys.argv[1])
