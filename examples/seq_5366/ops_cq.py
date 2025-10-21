import cadquery as cq
from math import cos, sin, atan2, degrees

# ------------- Config baked into this script -------------
EXTRUDE_MODE   = "solids"        # "solids" or "plate"
SOLID_HEIGHT   = 0.008        # m
PLATE_THICK    = 0.004   # m
PLATE_MARGIN   = 0.002        # m
TOL_EDGE       = 1e-09
TOL_CLOSE      = 1e-06
BRIDGE_GAPS    = True  # auto-bridge tiny end gaps
PRINT_DEBUG    = True

# ------------- Helpers -------------
def V(x, y, z=0.0): 
    return cq.Vector(float(x), float(y), float(z))

def dbg(*a):
    if PRINT_DEBUG:
        print(*a)

def edge_ok(e, tol=TOL_EDGE):
    # robust non-degenerate check without .length()
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
        return True

def _to_wire_list(obj):
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

def assemble_closed_wires(edges, direct_wires):
    try:
        assembled = cq.Wire.assembleEdges(edges) if edges else []
        wires_all = _to_wire_list(assembled)
    except Exception as ex:
        dbg("assembleEdges(all) failed → fallback:", ex)
        wires_all = []
        for e in edges:
            try:
                wires_all.extend(_to_wire_list(cq.Wire.assembleEdges([e])))
            except Exception as ex2:
                dbg("assembleEdges(single) failed:", ex2)
    closed = []
    for w in wires_all + list(direct_wires):
        try:
            if w.isClosed():
                closed.append(w)
        except Exception:
            try:
                sp = V(*w.startPoint().toTuple()); ep = V(*w.endPoint().toTuple())
                if (sp-ep).Length <= TOL_CLOSE:
                    closed.append(w)
            except:
                pass
    return closed, wires_all

def close_small_gaps(edges, wires_all):
    added = False
    for w in wires_all:
        try:
            if w.isClosed(): 
                continue
        except:
            pass
        try:
            sp = V(*w.startPoint().toTuple()); ep = V(*w.endPoint().toTuple())
        except Exception:
            continue
        gap = (sp - ep).Length
        if 0 < gap <= TOL_CLOSE:
            edges.append(cq.Edge.makeLine(ep, sp))
            added = True
    if added:
        dbg(f"[auto-close] bridged gaps ≤ {TOL_CLOSE}")
        return assemble_closed_wires(edges, [])
    return [], wires_all

def wires_bbox_area(w):
    b = w.BoundingBox()
    return (b.xmax - b.xmin) * (b.ymax - b.ymin)

def group_outer_and_holes(closed_wires):
    wires_sorted = sorted(closed_wires, key=wires_bbox_area, reverse=True)
    groups = []  # [ [outer, [holes]], ... ]
    for w in wires_sorted:
        placed = False
        bb = w.BoundingBox()
        for outer, holes in groups:
            ob = outer.BoundingBox()
            if (bb.xmin >= ob.xmin - 1e-9 and bb.ymin >= ob.ymin - 1e-9 and
                bb.xmax <= ob.xmax + 1e-9 and bb.ymax <= ob.ymax + 1e-9):
                holes.append(w); placed=True; break
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

# ---------- BEGIN PRIMITIVES (generated below) ----------
edges = []
direct_wires = []
edges.append(cq.Edge.makeCircle(0.017500000000000002, V(-7.7459808439044551e-19, 0.025000000000000001), cq.Vector(0,0,1), -35.060069163, 145.633635552))
edges.append(cq.Edge.makeCircle(0.012500000000000001, V(-7.7459808439044551e-19, 0.025000000000000001), cq.Vector(0,0,1), -91.0245864158, 145.119167587))
edges.append(cq.Edge.makeLine(V(-0.012801486171211547, 0.031509374148739611), V(-0.013700907094109692, 0.031966716931135834)))
edges.append(cq.Edge.makeLine(V(-0.0074999999999999997, 0), V(0.0074999999999999997, 0)))
edges.append(cq.Edge.makeCircle(0.044999999999999998, V(0.051159390874778693, -0.010902182737566385), cq.Vector(0,0,1), 144.939930837, 165.979400618))
edges.append(cq.Edge.makeCircle(0.059663906394430463, V(0.051159390874778693, -0.010902182737566385), cq.Vector(0,0,1), 160.324449611, 169.471383026))
edges.append(cq.Edge.makeCircle(0.0050000000000000079, V(-0.000312925433939743, 0.0075027980044581506), cq.Vector(0,0,1), 88.9754135842, 160.324449611))
edges.append(cq.Edge.makeCircle(0.002, V(-0.011894976896370583, 0.03329213631308664), cq.Vector(0,0,1), -116.952690646, -34.8808324126))
edges.append(cq.Edge.makeCircle(0.0020000000000000005, V(-0.012794397819268728, 0.033749479095482864), cq.Vector(0,0,1), 145.633635552, -116.952690646))
# ---------- END PRIMITIVES ----------

# Optional tiny-gap bridging (close nearly-closed loops)
closed_wires, all_wires = assemble_closed_wires(edges, direct_wires)
if BRIDGE_GAPS and not closed_wires:
    closed_wires, all_wires = close_small_gaps(edges, all_wires)

dbg(f"edges={{len(edges)}} | direct_wires(circles)={{len(direct_wires)}} | wires(all)={{len(all_wires)}} | closed={{len(closed_wires)}}")

groups = group_outer_and_holes(closed_wires)
faces  = faces_from_groups(groups)
dbg(f"wire_groups={{len(groups)}} | faces={{len(faces)}}")

result = None
if EXTRUDE_MODE == "solids":
    result = extrude_faces_union(faces, SOLID_HEIGHT)

elif EXTRUDE_MODE == "plate":
    bb = bbox_of_wires(closed_wires)
    if bb:
        xmin, ymin, xmax, ymax = bb
        w = (xmax - xmin) + 2*PLATE_MARGIN
        h = (ymax - ymin) + 2*PLATE_MARGIN
        cx = 0.5*(xmin + xmax)
        cy = 0.5*(ymin + ymax)
        plate = (cq.Workplane("XY")
                 .center(cx, cy)
                 .rect(w, h)
                 .extrude(PLATE_THICK)
                 .val())
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

# Show something in CQ-Editor if run interactively
show_object(cq.Workplane(obj=result) if result else cq.Workplane())