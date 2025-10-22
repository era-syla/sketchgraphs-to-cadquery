# Auto-generated: complex wrapper for an existing base CadQuery script
# Loads the base script (ops_cq.py), applies extra features, and shows result.

import cadquery as cq
import runpy, random

BASE_PATH = r"/Users/erasyla/SketchGraphs/SketchGraphs-1/filtered_dataset/complex_closed_500/seq_7677/ops_cq.py"
FEATURE_PLAN_KIND = "rules"
FEATURE_SEED = 0
FEATURE_PLAN = [{'name': 'fillet', 'params': {'r_frac': 0.06}}, {'name': 'pocket', 'params': {'inset_frac': 0.25, 'depth_frac': 0.25}}, {'name': 'holes', 'params': {'count': 3, 'dia_frac': 0.08, 'through': True}}, {'name': 'chamfer', 'params': {'d_frac': 0.05}}]
PRINT_DEBUG = True

def dbg(*a):
    if PRINT_DEBUG:
        print(*a)

def load_base_solid(path):
    env = {"show_object": lambda *args, **kwargs: None}  # suppress viewer during import
    g = runpy.run_path(path, init_globals=env)
    solid = g.get("result", None) or g.get("solid", None)
    if solid is None:
        raise RuntimeError("Base script did not produce 'result' or 'solid'.")
    return solid

def _bbox_xy(s):
    b = s.BoundingBox()
    return (b.xmin, b.ymin, b.xmax, b.ymax)

def _safe_span(s):
    xmin, ymin, xmax, ymax = _bbox_xy(s)
    return max(1e-9, min(xmax - xmin, ymax - ymin))

def _largest_top_face(s):
    wp = cq.Workplane(obj=s)
    faces = wp.faces(">Z").vals() or wp.faces().vals()
    if not faces: return None
    def area(f):
        b = f.BoundingBox()
        return (b.xmax-b.xmin)*(b.ymax-b.ymin)
    return sorted(faces, key=area, reverse=True)[0]

def feat_fillet_all_lines(s, r_frac=0.05):
    try:
        r = max(1e-5, r_frac * _safe_span(s))
        return cq.Workplane(obj=s).edges("%LINE").fillet(r).val()
    except Exception as ex:
        dbg("fillet fail:", ex); return s

def feat_chamfer_all_lines(s, d_frac=0.05):
    try:
        d = max(1e-5, d_frac * _safe_span(s))
        return cq.Workplane(obj=s).edges("%LINE").chamfer(d).val()
    except Exception as ex:
        dbg("chamfer fail:", ex); return s

def feat_pocket_on_top(s, inset_frac=0.25, depth_frac=0.25):
    f = _largest_top_face(s)
    if f is None: return s
    b = f.BoundingBox()
    w, h = (b.xmax-b.xmin), (b.ymax-b.ymin)
    if w <= 0 or h <= 0: return s
    inset_w = max(1e-6, (1 - max(1e-6, min(0.99, inset_frac))) * w)
    inset_h = max(1e-6, (1 - max(1e-6, min(0.99, inset_frac))) * h)
    try:
        return (cq.Workplane(obj=s)
                .faces(">Z").workplane(centerOption="CenterOfMass")
                .rect(inset_w, inset_h)
                .cutBlind(-depth_frac * 0.008)  # assumes your base height; tweak if needed
                .val())
    except Exception as ex:
        dbg("pocket fail:", ex); return s

def feat_random_holes_on_top(s, count=3, dia_frac=0.08, through=True, seed=0):
    f = _largest_top_face(s)
    if f is None: return s
    b = f.BoundingBox()
    w, h = (b.xmax-b.xmin), (b.ymax-b.ymin)
    if w <= 0 or h <= 0: return s
    rnd = random.Random(seed)
    m = 0.1 * min(w, h)
    xs = (b.xmin + m, b.xmax - m)
    ys = (b.ymin + m, b.ymax - m)
    cx, cy = (b.xmin + 0.5*w), (b.ymin + 0.5*h)
    pts = []
    for _ in range(max(1, int(count))):
        x = rnd.uniform(xs[0], xs[1]) - cx
        y = rnd.uniform(ys[0], ys[1]) - cy
        pts.append((x, y))
    dia = max(1e-5, dia_frac * _safe_span(s))
    try:
        wp = (cq.Workplane(obj=s)
              .faces(">Z").workplane(centerOption="CenterOfMass")
              .pushPoints(pts))
        if through:
            return wp.hole(dia).val()
        else:
            return wp.hole(dia, depth=0.006).val()
    except Exception as ex:
        dbg("holes fail:", ex); return s

# run
solid = load_base_solid(BASE_PATH)
dbg("[complex] plan:", FEATURE_PLAN_KIND, FEATURE_PLAN)
for step in FEATURE_PLAN:
    name = step["name"]; params = step.get("params", {})
    dbg(" apply:", name, params)
    if name == "fillet":
        solid = feat_fillet_all_lines(solid, r_frac=params.get("r_frac", 0.06))
    elif name == "chamfer":
        solid = feat_chamfer_all_lines(solid, d_frac=params.get("d_frac", 0.05))
    elif name == "pocket":
        solid = feat_pocket_on_top(solid,
                                   inset_frac=params.get("inset_frac", 0.25),
                                   depth_frac=params.get("depth_frac", 0.25))
    elif name == "holes":
        solid = feat_random_holes_on_top(solid,
                                         count=params.get("count", 3),
                                         dia_frac=params.get("dia_frac", 0.08),
                                         through=params.get("through", True),
                                         seed=FEATURE_SEED + 97)
    else:
        dbg(" unknown feature:", name)

show_object(cq.Workplane(obj=solid))
