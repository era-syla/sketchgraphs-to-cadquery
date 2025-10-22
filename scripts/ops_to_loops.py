#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ops_to_cq_codegen.py
Read an ops.json and GENERATE a self-contained CadQuery script that recreates
the sketch as Lines/Arcs/Circles, assembles wires, finds faces (with holes),
and extrudes (either solids or a plate-with-holes). The generated code does
NOT parse JSON; it uses hard-coded numeric primitives.

Example:
  python3 scripts/ops_to_cq_codegen.py filtered_dataset/.../ops.json > out_cq.py
  python3 scripts/ops_to_cq_codegen.py ops.json --out-py out_cq.py
"""

import argparse, json, sys, os
from math import cos, sin, atan2, degrees
import math
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

import os  # (if not already imported)

import math
from typing import List, Dict, Tuple, Any

def get_multi_json_files(folder_path: str) -> List[str]:
    """
    Recursively find all files named 'ops.json' in any subdirectory of folder_path.

    Args:
        folder_path: Root folder to search in

    Returns:
        List of absolute paths to all ops.json files found
    """
    ops_json_files = []

    for root, dirs, files in os.walk(folder_path):
        if "ops.json" in files:
            abs_path = os.path.abspath(os.path.join(root, "ops.json"))
            ops_json_files.append(abs_path)

    return ops_json_files


def round_point(point: Tuple[float, float], decimals: int) -> Tuple[float, float]:
    """Round a point's coordinates to specified decimal places."""
    return (round(point[0], decimals), round(point[1], decimals))

def extract_endpoints(feature: Dict, decimals: int) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    """Extract start and end points from a feature."""
    if 'sketch_op' in feature:
        if feature['sketch_op'] in ['Arc', 'Line']:
            return (round_point(tuple(feature['start']), decimals), round_point(tuple(feature['end']), decimals))
    elif feature.get('kind') == 'NodeOp' and feature.get('label') == 'Line':
        params = feature['parameters']
        pnt = (params['pntX'], params['pntY'])
        dir_vec = (params['dirX'], params['dirY'])
        start_param = params['startParam']
        end_param = params['endParam']
        
        start = (pnt[0] + dir_vec[0] * start_param, pnt[1] + dir_vec[1] * start_param)
        end = (pnt[0] + dir_vec[0] * end_param, pnt[1] + dir_vec[1] * end_param)
        return (round_point(start, decimals), round_point(end, decimals))
    
    return None

def points_match(p1: Tuple[float, float], p2: Tuple[float, float], tolerance: float = 1e-9) -> bool:
    """Check if two points match within tolerance."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) < tolerance

def round_feature(feature: Dict, decimals: int) -> Dict:
    """Round all coordinates in a feature to specified decimal places."""
    rounded = feature.copy()
    if 'start' in rounded:
        rounded['start'] = round_point(tuple(rounded['start']), decimals)
    if 'end' in rounded:
        rounded['end'] = round_point(tuple(rounded['end']), decimals)
    if 'mid' in rounded:
        rounded['mid'] = round_point(tuple(rounded['mid']), decimals)
    return rounded

def find_closed_loops(features: List[Dict], tolerance: float = 1e-9, decimals: int = 5) -> List[List[Dict]]:
    """
    Find all closed loops in a list of sketch features.

    Args:
        features: List of feature dictionaries
        tolerance: Distance tolerance for matching points
        decimals: Number of decimal places to round points to (default: 5)

    Returns:
        List of closed loops, where each loop is a list of features with rounded coordinates
    """
    loops = []
    used_indices = set()

    # First, check for circles - they are closed loops by definition
    for idx, feature in enumerate(features):
        if feature.get('sketch_op') == 'Circle':
            # Round the circle's center and radius
            rounded_circle = feature.copy()
            rounded_circle['center'] = round_point(tuple(rounded_circle['center']), decimals)
            rounded_circle['radius'] = round(rounded_circle['radius'], decimals)
            loops.append([rounded_circle])
            used_indices.add(idx)

    # Try to build a loop starting from each unused feature
    for start_idx in range(len(features)):
        if start_idx in used_indices:
            continue

        loop = []
        current_indices = []
        endpoints = extract_endpoints(features[start_idx], decimals)

        if endpoints is None:
            continue

        current_start, current_end = endpoints
        loop.append(round_feature(features[start_idx], decimals))
        current_indices.append(start_idx)

        # Try to extend the loop
        while True:
            found_next = False

            # Look for a feature that connects to current_end
            for idx in range(len(features)):
                if idx in current_indices:
                    continue

                endpoints = extract_endpoints(features[idx], decimals)
                if endpoints is None:
                    continue

                feat_start, feat_end = endpoints

                # Check if this feature connects (forward or reversed)
                if points_match(current_end, feat_start, tolerance):
                    loop.append(round_feature(features[idx], decimals))
                    current_indices.append(idx)
                    current_end = feat_end
                    found_next = True
                    break
                elif points_match(current_end, feat_end, tolerance):
                    # Need to flip this feature
                    flipped = features[idx].copy()
                    if 'sketch_op' in flipped:
                        flipped['start'], flipped['end'] = flipped['end'], flipped['start']
                        if 'mid' in flipped:
                            # For arcs, we keep mid as is (it's still the midpoint)
                            pass
                    loop.append(round_feature(flipped, decimals))
                    current_indices.append(idx)
                    current_end = feat_start
                    found_next = True
                    break

            if not found_next:
                break

            # Check if loop is closed
            if points_match(current_end, current_start, tolerance):
                # We have a closed loop!
                loops.append(loop)
                used_indices.update(current_indices)
                break

        # If we didn't find a closed loop, discard this attempt
        if not (loop and points_match(current_end, current_start, tolerance)):
            loop = []

    return loops


def feature_to_cadquery(feature, loop_name="loop0", workplane_name="wp_sketch0"):
    """
    Convert a sketch feature dict to CadQuery code string.
    
    Args:
        feature: Dict with 'sketch_op', 'start', 'mid', 'end' (and 'end' for Line)
        loop_name: Variable name for the loop
        workplane_name: Variable name for the workplane
        is_first: If True, includes moveTo() for the start point
    
    Returns:
        String of CadQuery code
    """
    sketch_op = feature['sketch_op']
    
    code = f"{loop_name} = {workplane_name}."
    
    if sketch_op == 'Arc':
        start = feature['start']
        mid = feature['mid']
        end = feature['end']
        code += f"moveTo({start[0]}, {start[1]}).threePointArc(({mid[0]}, {mid[1]}), ({end[0]}, {end[1]}))"
    elif sketch_op == 'Line':
        start = feature['start']
        end = feature['end']
        code += f"moveTo({start[0]}, {start[1]}).lineTo({end[0]}, {end[1]})"
    elif sketch_op == 'Circle':
        center = feature['center']
        radius = feature['radius']
        code += f"moveTo({center[0]}, {center[1]}).circle({radius})"
    return code


def features_to_cadquery(features, loop_name="loop0", workplane_name="wp_sketch0"):
    """
    Convert a list of sketch features to CadQuery code.
    
    Args:
        features: List of feature dicts
        loop_name: Variable name for the loop
        workplane_name: Variable name for the workplane
    
    Returns:
        String of CadQuery code with proper line continuation
    """
    if not features:
        return ""
    
    lines = []
    for i, feature in enumerate(features):
        line = feature_to_cadquery(feature, loop_name, workplane_name, is_first=(i == 0))
        lines.append(line)
    
    # Join with line continuation for readability
    code = lines[0]
    for line in lines[1:]:
        # Extract just the method call (after the "loop_name = loop_name" part)
        method_call = line.split("= " + loop_name)[1]
        code += f" \\\n    {method_call}"
    
    return code

def parse_args():
    p = argparse.ArgumentParser(description="Generate CadQuery code from ops.json")
    p.add_argument("--single_json", default=None, help="Path to ops.json (list or {'ops': [...]})")
    p.add_argument("--multi_json_folder", default=None, help="Path to ops.json (list or {'ops': [...]})")
    p.add_argument("--debug", action="store_true", help="Enable debug output")
    p.add_argument("--workers", type=int, default=8, help="Number of parallel workers for processing (default: 8)")
    return p.parse_args()

def load_ops(path):
    with open(path, "r") as f:
        data = json.load(f)
    if isinstance(data, dict) and "ops" in data:
        ops = data["ops"]
    else:
        ops = data
    if not isinstance(ops, list):
        raise ValueError("ops_json must be a list or a dict with key 'ops'.")
    return ops

def get_circle_feature(params):
    # Circle parameters
    xCenter = params["xCenter"]
    yCenter = params["yCenter"]
    radius = params["radius"]

    return {"sketch_op": "Circle",
            "center": (xCenter, yCenter),
            "radius": radius
        }

def get_line_feature(params):
    pntX = params["pntX"]
    pntY = params["pntY"]
    dirX = params["dirX"]
    dirY = params["dirY"]
    startParam = params["startParam"]
    endParam = params["endParam"]

    # Start point
    start_x = pntX + startParam * dirX
    start_y = pntY + startParam * dirY

    # End point
    end_x = pntX + endParam * dirX
    end_y = pntY + endParam * dirY
    return {"sketch_op": "Line",
            "start": (start_x, start_y),
            "end": (end_x, end_y)
        }

def get_arc_feature(params):
    # Arc parameters
    xCenter = params["xCenter"]
    yCenter = params["yCenter"]
    xDir = params["xDir"]
    yDir = params["yDir"]
    radius = params["radius"]
    startParam = params["startParam"]
    endParam = params["endParam"]
    clockwise = params["clockwise"]

    ref_angle = math.atan2(yDir, xDir)  # 0 for (1.0, 0.0)

    # Start point
    start_angle = ref_angle + startParam
    start_x = xCenter + radius * math.cos(start_angle)
    start_y = yCenter + radius * math.sin(start_angle)

    # End point
    end_angle = ref_angle + endParam
    end_x = xCenter + radius * math.cos(end_angle)
    end_y = yCenter + radius * math.sin(end_angle)

    # Midpoint - need to handle arc direction properly
    # Calculate the angular span
    angular_span = endParam - startParam

    # For counterclockwise arcs, this should be positive
    # If we need to wrap, adjust accordingly
    if not clockwise and angular_span < 0:
        angular_span += 2 * math.pi
    elif clockwise and angular_span > 0:
        angular_span -= 2 * math.pi

    mid_param = startParam + angular_span / 2
    mid_angle = ref_angle + mid_param
    mid_x = xCenter + radius * math.cos(mid_angle)
    mid_y = yCenter + radius * math.sin(mid_angle)

    return {"sketch_op": "Arc",
            "start": (start_x, start_y),
            "mid": (mid_x, mid_y),
            "end": (end_x, end_y)
        }
    
def run_single(json_path, debug=False):
    ops = load_ops(json_path)

    # Get the relevant ops
    relevant_ops = []
    for n in ops:
        if n.get("kind") != "NodeOp":
            continue
        label = n.get("label","")
        p = (n.get("parameters") or {})
        if p.get("isConstruction", False):
            continue
        if label == "Line":
            relevant_ops.append(n)
        elif label == "Arc":
            relevant_ops.append(n)
        elif label == "Circle":
            relevant_ops.append(n)
    
    if debug:
        print("RAW OPS")
        print("*" * 40)
        for op in relevant_ops:
            print(op)
        print("*" * 40)

    # Get start and end points of the features
    start_end_features = []
    for feature in relevant_ops:
        if feature["label"] == "Arc":
            start_end_features.append(get_arc_feature(feature["parameters"]))
        elif feature["label"] == "Line":
            start_end_features.append(get_line_feature(feature["parameters"]))
        elif feature["label"] == "Circle":
            start_end_features.append(get_circle_feature(feature["parameters"]))
        else:
            raise ValueError(f"Unknown feature label: {feature['label']}")
    
    if debug:
        print("START END FEATURES")
        print("*" * 40)
        for op in start_end_features:
            print(op)
        print("*" * 40)
        
    # Get closed loops
    closed_loops = find_closed_loops(start_end_features)

    # Write the closed loops to a json
    input_dir = os.path.dirname(os.path.abspath(json_path))
    output_path = os.path.join(input_dir, "loops.json")
    with open(output_path, "w") as f:
        json.dump(closed_loops, f, indent=2)

    if debug:
        print(f"Wrote {len(closed_loops)} loop(s) to {output_path}")
    
    
    if debug:
        print("CLOSED LOOPS")
        print("*" * 40)
        print(f"Found {len(closed_loops)} closed loop(s):\n")
        for i, loop in enumerate(closed_loops):
            print(f"Loop {i+1} ({len(loop)} features):")
            for feature in loop:
                print(" ", feature)
        print("*" * 40)

    if debug:
        print("CADQUERY TEST")
        print("*" * 40)
        print(f"Found {len(closed_loops)} closed loop(s):\n")
        print(f"Loop {i+1} ({len(loop)} features):")
        print(f"import cadquery as cq\nwp_sketch0 = cq.Workplane('XY')")
        for i, loop in enumerate(closed_loops):
            for j, feature in enumerate(loop):
                print(feature_to_cadquery(feature, loop_name=f"loop{i}_{j}", workplane_name="wp_sketch0"))
        print("*" * 40)
    return

def main():
    args = parse_args()

    # Check if neither argument is provided
    if args.single_json is None and args.multi_json_folder is None:
        print("Error: Please provide either --single_json or --multi_json_folder argument", file=sys.stderr)
        sys.exit(1)

    # If single_json is provided, use run_single
    if args.single_json is not None:
        run_single(args.single_json, debug=args.debug)

    # If multi_json_folder is provided, show not yet implemented error
    if args.multi_json_folder is not None:
        input_jsons = get_multi_json_files(args.multi_json_folder)

        with ProcessPoolExecutor(max_workers=args.workers) as executor:

            # Submit all tasks
            future_to_item = {executor.submit(run_single, str(item)): item for item in input_jsons}
            for future in tqdm(as_completed(future_to_item), total=len(input_jsons),
                            desc=f"Processing {run_single.__name__}"):
                result = future.result()
    


if __name__ == "__main__":
    main()
