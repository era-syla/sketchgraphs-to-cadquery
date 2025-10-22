import cadquery as cq
from math import cos, sin, atan2, degrees

# ──────────────────────────────────────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────────────────────────────────────
EXTRUDE_MODE   = "solids"       # "solids" or "plate_with_holes"
SOLID_HEIGHT   = 0.008          # 8 mm (used in "solids" mode)
PLATE_THICK    = 0.004          # 4 mm (used in "plate_with_holes" mode)
PLATE_MARGIN   = 0.002          # extra margin around bbox for plate
TOL_EDGE       = 1e-9           # skip degenerate edges
TOL_CLOSE      = 1e-6           # bridge gaps ≤ this to close loops
PRINT_DEBUG    = True

# ──────────────────────────────────────────────────────────────────────────────
# PASTE YOUR OPS HERE
# ──────────────────────────────────────────────────────────────────────────────
ops = [
    # replace with your JSON ops each time
]

# ──────────────────────────────────────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────────────────────────────────────
def V(x, y, z=0.0): 
    return cq.Vector(float(x), float(y), float(z))

def dbg(*a):
    if PRINT_DEBUG: 
        print(*a)

# Robust “non-degenerate” check without .length()
def edge_ok(e, tol=TOL_EDGE):
    try:
        sp, ep = e.startPoint(), e.endPoint()
        if (V(*sp.toTuple()) - V(*ep.toTuple())).Length > tol:
            return True
    except Exception:
        pass
    try:
        b = e.BoundingBox()
        span = max(b.xmax - b.xmin, b.ymax - b.ymin, b.zmax - b.zmin)
        return span > tol
    except Exception:
        # last resort: keep it
        return True

def line_endpoints(p):
    dx, dy = float(p["dirX"]), float(p["dirY"])
    px, py = float(p["pntX"]), float(p["pntY"])
    t0, t1 = float(p["startParam"]), float(p["endParam"])
    p0 = V(px + dx * t0, py + dy * t0)
    p1 = V(px + dx * t1, py + dy * t1)
    return p0, p1

def arc_edge(p):
    # Build an oriented circular arc from center, radius, local axes, and angles
    cx, cy = float(p["xCenter"]), float(p["yCenter"])
    R = float(p["radius"])
    xdx, xdy = float(p["xDir"]), float(p["yDir"])
    ydx, ydy = -xdy, xdx
    a0, a1 = float(p["startParam"]), float(p["endParam"])

    def world_angle(a):
        vx = cos(a)*xdx + sin(a)*ydx
        vy = cos(a)*xdy + sin(a)*ydy
        return degrees(atan2(vy, vx))

    return cq.Edge.makeCircle(R, V(cx, cy, 0), cq.Vector(0,0,1), world_angle(a0), world_angle(a1))

def circle_wire(p):
    # Full circle as a closed wire (better than assembling edges)
    cx, cy = float(p["xCenter"]), float(p["yCenter"])
    R = float(p["radius"])
    if R <= TOL_EDGE:
        return None
    return cq.Wire.makeCircle(R, V(cx, cy, 0), cq.Vector(0,0,1))

def build_primitives_from_ops(ops):
    """Return (edges, direct_wires) where direct_wires are full circles already closed."""
    edges, direct_wires = [], []
    for n in ops:
        if n.get("kind") != "NodeOp":
            continue
        lbl = n.get("label","")
        p = n.get("parameters",{}) or {}

        if lbl == "Line":
            if p.get("isConstruction", False): 
                continue
            p0, p1 = line_endpoints(p)
            e = cq.Edge.makeLine(p0, p1)
            if edge_ok(e):
                edges.append(e)

        elif lbl == "Arc":
            if p.get("isConstruction", False): 
                continue
            e = arc_edge(p)
            if edge_ok(e):
                edges.append(e)

        elif lbl == "Circle":
            if p.get("isConstruction", False): 
                continue
            w = circle_wire(p)
            if w is not None:
                direct_wires.append(w)
        # ignore Points/constraints
    return edges, direct_wires

def _to_wire_list(obj):
    """Normalize return types to list[Wire], coercing Edges to Wires when needed."""
    if obj is None:
        return []
    if isinstance(obj, cq.Wire):
        return [obj]
    if isinstance(obj, cq.Edge):
        return _to_wire_list(cq.Wire.assembleEdges([obj]))
    if isinstance(obj, (list, tuple)):
        out = []
        for it in obj:
            if isinstance(it, cq.Wire):
                out.append(it)
            elif isinstance(it, cq.Edge):
                out.extend(_to_wire_list(cq.Wire.assembleEdges([it])))
        return out
    return []

def assemble_closed_wires(edges, direct_closed):
    # Assemble all edges → wires (robust across versions)
    try:
        assembled = cq.Wire.assembleEdges(edges) if edges else []
        wires = _to_wire_list(assembled)
    except Exception as ex:
        dbg("assembleEdges(all) failed → fallback per-edge:", ex)
        wires = []
        for e in edges:
            try:
                wires.extend(_to_wire_list(cq.Wire.assembleEdges([e])))
            except Exception as ex2:
                dbg("assembleEdges(single) failed:", ex2)

    # filter closed & include direct circle wires
    closed = []
    for w in wires + list(direct_closed):
        try:
            if w.isClosed():
                closed.append(w)
        except Exception:
            try:
                sp = V(*w.startPoint().toTuple())
                ep = V(*w.endPoint().toTuple())
                if (sp - ep).Length <= TOL_CLOSE:
                    closed.append(w)
            except:
                pass
    return closed, wires

def close_small_gaps(edges, wires_all):
    """Add tiny 'bridge' edges to close near-closed wires; reassemble once."""
    added = False
    for w in wires_all:
        try:
            if w.isClosed():
                continue
        except:
            pass
        try:
            sp = V(*w.startPoint().toTuple())
            ep = V(*w.endPoint().toTuple())
        except Exception:
            continue
        gap = (sp - ep).Length
        if 0 < gap <= TOL_CLOSE:
            edges.append(cq.Edge.makeLine(ep, sp))  # bridge edge
            added = True
    if added:
        closed, wires_all2 = assemble_closed_wires(edges, [])
        return closed, wires_all2, True
    return [], wires_all, False

def wires_bbox_area(w):
    b = w.BoundingBox()
    return (b.xmax - b.xmin) * (b.ymax - b.ymin)

def group_outer_and_holes(closed_wires):
    # Sort by area desc so big loops tend to be outers
    wires_sorted = sorted(closed_wires, key=wires_bbox_area, reverse=True)
    groups = []  # list of [outer_wire, [hole_wires]]
    for w in wires_sorted:
        placed = False
        bb = w.BoundingBox()
        for outer, holes in groups:
            ob = outer.BoundingBox()
            if (bb.xmin >= ob.xmin - 1e-9 and bb.ymin >= ob.ymin - 1e-9 and
                bb.xmax <= ob.xmax + 1e-9 and bb.ymax <= ob.ymax + 1e-9):
                holes.append(w)
                placed = True
                break
        if not placed:
            groups.append([w, []])
    return groups

def faces_from_groups(groups):
    faces = []
    for outer, holes in groups:
        try:
            if holes:
                faces.append(cq.Face.makeFromWires(outer, holes))
            else:
                faces.append(cq.Face.makeFromWires(outer))
        except Exception as ex:
            dbg("Face failed:", ex)
    return faces

def extrude_faces_union(faces, height):
    solids = []
    for f in faces:
        try:
            solids.append(cq.Workplane(obj=f).extrude(height).val())
        except Exception as ex:
            dbg("Extrude failed:", ex)
    if not solids:
        return None
    return cq.Workplane().newObject(solids).combine().val()

def bbox_of_wires(wires):
    if not wires:
        return None
    bb = None
    for w in wires:
        b = w.BoundingBox()
        if bb is None:
            bb = [b.xmin, b.ymin, b.xmax, b.ymax]
        else:
            bb[0] = min(bb[0], b.xmin)
            bb[1] = min(bb[1], b.ymin)
            bb[2] = max(bb[2], b.xmax)
            bb[3] = max(bb[3], b.ymax)
    return bb

# ──────────────────────────────────────────────────────────────────────────────
# RUN
# ──────────────────────────────────────────────────────────────────────────────
edges, direct_wires = build_primitives_from_ops(ops)
closed_wires, wires_all = assemble_closed_wires(edges, direct_wires)

if not closed_wires:
    # one pass of tiny bridging
    closed_wires, wires_all, bridged = close_small_gaps(edges, wires_all)
    if bridged:
        dbg(f"[auto-close] bridged tiny gaps ≤ {TOL_CLOSE}")

dbg(f"edges={len(edges)} | direct_wires(circles)={len(direct_wires)} | wires(all)={len(wires_all)} | closed={len(closed_wires)}")

groups = group_outer_and_holes(closed_wires)
faces  = faces_from_groups(groups)
dbg(f"wire_groups={len(groups)} | faces={len(faces)}")

result = None
if EXTRUDE_MODE == "solids":
    result = extrude_faces_union(faces, SOLID_HEIGHT)

elif EXTRUDE_MODE == "plate_with_holes":
    bb = bbox_of_wires(closed_wires)
    if bb:
        xmin, ymin, xmax, ymax = bb
        w = (xmax - xmin) + 2*PLATE_MARGIN
        h = (ymax - ymin) + 2*PLATE_MARGIN
        cx, cy = 0.5*(xmin + xmax), 0.5*(ymin + ymax)
        plate = (cq.Workplane("XY")
                 .center(cx, cy)
                 .rect(w, h)
                 .extrude(PLATE_THICK)
                 .val())
        # holes: extrude each face through plate and cut
        cutters = []
        for f in faces:
            try:
                cutters.append(cq.Workplane(obj=f).extrude(PLATE_THICK + 1e-3).val())
            except Exception as ex:
                dbg("Cutter extrude failed:", ex)
        if cutters:
            cutters_combined = cq.Workplane().newObject(cutters).combine().val()
            result = plate.cut(cutters_combined)
        else:
            result = plate
    else:
        dbg("No closed wires; skipping plate.")
        result = None

# Show result (or an empty Workplane)
show_object(cq.Workplane(obj=result) if result else cq.Workplane())
