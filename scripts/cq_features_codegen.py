#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, sys, json, random, runpy
from pathlib import Path
from typing import List

def parse_args():
    p = argparse.ArgumentParser(description="Generate complex CadQuery wrappers for ops_cq.py files.")
    p.add_argument("target", help="Path to a single ops_cq.py OR a directory containing many seq_*/ops_cq.py.")
    p.add_argument("--plan", choices=["rules","random"], default="rules", help="Feature plan type.")
    p.add_argument("--steps", type=int, default=3, help="Number of random features when --plan random.")
    p.add_argument("--seed", type=int, default=None, help="Seed for random plan.")
    p.add_argument("--basename", default="ops_cq.py", help="Base script filename to look for (default: ops_cq.py).")
    p.add_argument("--dry-run", action="store_true", help="List what would be generated; do not write files.")
    return p.parse_args()


RULES_PLAN = [
    {"name":"fillet",  "params":{"r_frac":0.06}},
    {"name":"pocket",  "params":{"inset_frac":0.25, "depth_frac":0.25}},
    {"name":"holes",   "params":{"count":3, "dia_frac":0.08, "through":True}},
    {"name":"chamfer", "params":{"d_frac":0.05}},
]
RANDOM_POOL = [
    ("fillet",  lambda rng: {"r_frac": rng.uniform(0.04, 0.12)}),
    ("chamfer", lambda rng: {"d_frac": rng.uniform(0.04, 0.12)}),
    ("pocket",  lambda rng: {"inset_frac": rng.uniform(0.18, 0.35),
                             "depth_frac": rng.uniform(0.15, 0.35)}),
    ("holes",   lambda rng: {"count": rng.randint(1,5),
                             "dia_frac": rng.uniform(0.05, 0.12),
                             "through": rng.random() < 0.7}),
]

from typing import Optional
def make_feature_plan(kind: str, steps: int, seed: Optional[int]):
    if kind == "rules":
        return {"seed": (seed if seed is not None else 0), "plan": RULES_PLAN}
    rng = random.Random(seed if seed is not None else 0)
    plan = []
    for _ in range(max(1, int(steps))):
        name, sampler = rng.choice(RANDOM_POOL)
        plan.append({"name": name, "params": sampler(rng)})
    return {"seed": (seed if seed is not None else 0), "plan": plan}


TEMPLATE = r'''

import cadquery as cq
import runpy, random

BASE_PATH = r"{BASE_PATH}"
FEATURE_PLAN_KIND = "{PLAN_KIND}"
FEATURE_SEED = {SEED}
FEATURE_PLAN = {PLAN_PY}
PRINT_DEBUG = True

def dbg(*a):
    if PRINT_DEBUG:
        print(*a)

def load_base_solid(path):
    env = {{"show_object": lambda *args, **kwargs: None}}  
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
                .cutBlind(-depth_frac * 0.008)  
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
    name = step["name"]; params = step.get("params", {{}})
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
'''


def targets_from_path(target: str, basename: str) -> List[Path]:
    p = Path(target)
    if p.is_file():
        if p.name != basename:
            print(f"[warn] Provided file is not named {basename}: {p.name}", file=sys.stderr)
        return [p]
    if p.is_dir():
        return [f for f in p.rglob(basename)]
    raise FileNotFoundError(target)

def out_path_for(base_file: Path) -> Path:
    return base_file.with_name(base_file.stem.replace(".py","") + "_complex.py")

def main():
    args = parse_args()
    plan = make_feature_plan(args.plan, args.steps, args.seed)
    base_files = targets_from_path(args.target, args.basename)

    if not base_files:
        print("[info] no targets found.", file=sys.stderr)
        sys.exit(1)

    for base in base_files:
        out_py = out_path_for(base)
        code = TEMPLATE.format(
        BASE_PATH=str(base.resolve()),
        PLAN_KIND=args.plan,
        SEED=plan["seed"],
        PLAN_PY=repr(plan["plan"]),   # use Python repr instead of JSON
        )
        if args.dry_run:
            print(f"[dry-run] would write: {out_py}")
            continue
        out_py.parent.mkdir(parents=True, exist_ok=True)
        with open(out_py, "w") as f:
            f.write(code)
        # If only one file given, also print to stdout for convenience
        if len(base_files) == 1:
            sys.stdout.write(code)
        print(f"[ok] wrote {out_py}")

if __name__ == "__main__":
    main()
