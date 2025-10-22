# ============================================================
# Auto-generated CadQuery reconstruction from:
#   /Users/erasyla/SketchGraphs/SketchGraphs-1/filtered_dataset/complex_closed_500/seq_3182/ops.json
#
# Rebuilds 2D sketch (lines, arcs, circles), assembles closed
# loops with tiny-gap bridging, builds faces (outer + holes),
# and extrudes the largest face by EXTRUDE_HEIGHT_MM.
# ============================================================
import cadquery as cq
from cadquery import Vector, Edge, Wire, Face

EXTRUDE_HEIGHT_MM = 3.000

DEBUG = True
def dprint(*a, **k):
    if DEBUG: print(*a, **k)

# tiny guards
EPS_MM = 1e-06
MIN_SEG_MM = 0.0001

def _vlen(p, q):
    dx = p[0]-q[0]; dy = p[1]-q[1]; dz = p[2]-q[2]
    return (dx*dx + dy*dy + dz*dz)**0.5

def _valid_line(p0, p1): return _vlen(p0, p1) > MIN_SEG_MM
def _valid_arc(p0, pm, p1):
    return (_vlen(p0, p1) > MIN_SEG_MM and
            _vlen(p0, pm) > MIN_SEG_MM and
            _vlen(pm, p1) > MIN_SEG_MM)

# ---- 1) Edge/circle specs ----
LOOPS = []

CIRCLES = [{'c': (4.7704895589362195e-15, 24.417923763394356, 0.0), 'r': 2.0}]

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

print({"edges_from_loops": sum(len(l) for l in LOOPS), "n_wires": len(wires), "n_faces": len(faces), "solid": bool(solid)})

try:
    for i, w in enumerate(wires): show_object(w, name=f"wire_{i}")
    for i, f in enumerate(faces): show_object(f, name=f"face_{i}", options={"alpha": 0.4})
    if solid is not None: show_object(solid, name="solid")
except Exception:
    pass
