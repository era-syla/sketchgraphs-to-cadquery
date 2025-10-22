#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
loops_to_cadquery.py
Read a loops.json file and generate CadQuery code.

Example:
  python3 scripts/loops_to_cadquery.py --json filtered_dataset/.../loops.json
"""

BBOX_TEMPLATE = '''{}
bbox = {}.val().BoundingBox()
'''

import argparse
import json
import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

OFFSET_DISTANCE = 0.5  # Distance to offset the revolve axis from the bounding box


def get_multi_json_files(folder_path):
    """
    Recursively find all files named 'loops.json' in any subdirectory of folder_path.

    Args:
        folder_path: Root folder to search in

    Returns:
        List of absolute paths to all loops.json files found
    """
    import os
    loops_json_files = []

    for root, dirs, files in os.walk(folder_path):
        if "loops.json" in files:
            abs_path = os.path.abspath(os.path.join(root, "loops.json"))
            loops_json_files.append(abs_path)

    return loops_json_files


def parse_args():
    p = argparse.ArgumentParser(description="Generate CadQuery code from loops.json")
    p.add_argument("--single_json", default=None, help="Path to a single loops.json file")
    p.add_argument("--multi_json_folder", default=None, help="Path to folder containing multiple loops.json files (will search recursively)")
    p.add_argument("--debug", action="store_true", help="Enable debug output")
    p.add_argument("--workers", type=int, default=8, help="Number of parallel workers for processing (default: 8)")
    return p.parse_args()

def load_loops(path):
    """Load loops from a JSON file."""
    with open(path, "r") as f:
        loops = json.load(f)
    if not isinstance(loops, list):
        raise ValueError("loops.json must be a list of loops.")
    return loops

def get_bbox_loop(code_thus_far, loop_name):
    import cadquery as cq

    code_to_run = BBOX_TEMPLATE.format(code_thus_far, loop_name)

    # Execute the code and extract bbox from namespace
    namespace = {'cq': cq}
    exec(code_to_run, namespace)

    bbox = namespace.get('bbox')
    if bbox:
        return {
            'xmin': bbox.xmin,
            'ymin': bbox.ymin,
            'zmin': bbox.zmin,
            'xmax': bbox.xmax,
            'ymax': bbox.ymax,
            'zmax': bbox.zmax
        }
    return None

def cadquery_loop(loop, loop_name, sketch_plane):
    cadquery = f"{loop_name} = {sketch_plane}"

    for i, sketch_feature in enumerate(loop):
        if i == 0: # For the first feature if it's not a circle, we need to move to the starting point
            if sketch_feature["sketch_op"] != "Circle":
                cadquery += f".moveTo({sketch_feature['start'][0]}, {sketch_feature['start'][1]})"
        if sketch_feature["sketch_op"] == "Line":
            cadquery += f".lineTo({sketch_feature['end'][0]}, {sketch_feature['end'][1]})"
        elif sketch_feature["sketch_op"] == "Arc":
            cadquery += f".threePointArc(({sketch_feature['mid'][0]}, {sketch_feature['mid'][1]}), ({sketch_feature['end'][0]}, {sketch_feature['end'][1]}))"
    cadquery += ".close()\n"
    return cadquery

def get_revolve_axis_points(bbox_values, plane_name):
    """
    Generate revolve axis points based on bounding box and plane.

    Args:
        bbox_values: Dict with keys xmin, xmax, ymin, ymax, zmin, zmax
        plane_name: One of 'XY', 'YZ', 'XZ'

    Returns:
        tuple: (start_point, end_point) - two tuples of (x, y, z) coordinates
    """
    if plane_name == 'XY':
        # Revolve axis should be in XY plane (z=0), either along X or Y direction
        # Randomly choose X or Y axis direction
        
        if random.choice([True, False]):
            # Revolve around X-axis (parallel to X)
            x_offset = bbox_values['xmin'] - OFFSET_DISTANCE
            y_pos = (bbox_values['ymin'] + bbox_values['ymax']) / 2
            start_point = (x_offset, y_pos, 0)
            end_point = (x_offset + 1, y_pos, 0)
        else:
            # Revolve around Y-axis (parallel to Y)
            x_pos = (bbox_values['xmin'] + bbox_values['xmax']) / 2
            y_offset = bbox_values['ymin'] - OFFSET_DISTANCE
            start_point = (x_pos, y_offset, 0)
            end_point = (x_pos, y_offset + 1, 0)

    elif plane_name == 'YZ':
        raise NotImplementedError("Revolve axis generation for YZ plane not yet implemented.")
        # Revolve axis should be in YZ plane (x=0), either along Y or Z direction
        if random.choice([True, False]):
            # Revolve around Y-axis (parallel to Y)
            y_offset = bbox_values['ymin'] - OFFSET_DISTANCE
            z_pos = (bbox_values['zmin'] + bbox_values['zmax']) / 2
            start_point = (0, y_offset, z_pos)
            end_point = (0, y_offset + 1, z_pos)
        else:
            # Revolve around Z-axis (parallel to Z)
            y_pos = (bbox_values['ymin'] + bbox_values['ymax']) / 2
            z_offset = bbox_values['zmin'] - OFFSET_DISTANCE
            start_point = (0, y_pos, z_offset)
            end_point = (0, y_pos, z_offset + 1)

    elif plane_name == 'XZ':
        raise NotImplementedError("Revolve axis generation for XZ plane not yet implemented.")
        # Revolve axis should be in XZ plane (y=0), either along X or Z direction
        if random.choice([True, False]):
            # Revolve around X-axis (parallel to X)
            x_offset = bbox_values['xmin'] - OFFSET_DISTANCE
            z_pos = (bbox_values['zmin'] + bbox_values['zmax']) / 2
            start_point = (x_offset, 0, z_pos)
            end_point = (x_offset + 1, 0, z_pos)
        else:
            # Revolve around Z-axis (parallel to Z)
            x_pos = (bbox_values['xmin'] + bbox_values['xmax']) / 2
            z_offset = bbox_values['zmin'] - OFFSET_DISTANCE
            start_point = (x_pos, 0, z_offset)
            end_point = (x_pos, 0, z_offset + 1)

    else:
        raise ValueError(f"Unknown plane name: {plane_name}")

    return start_point, end_point

def cadquery_sketch(plane_index):
    planes = ['XY', 'YZ', 'XZ']
    chosen_plane = random.choice(planes)
    wp_name = f"wp_sketch{plane_index}"
    wp_code = f"{wp_name} = cq.Workplane('{chosen_plane}')\n"
    return wp_code, chosen_plane, wp_name

def perform_3d_op_on_loop(loop_name, sketch_name, code_thus_far, plane_name):
    op_types_3d = ['extrude'] # TODO: add more operations, like loft and sweep
    chosen_op = random.choice(op_types_3d)
    if chosen_op == 'extrude':
        bbox_values = get_bbox_loop(code_thus_far, loop_name)
        # Get the max dimension of the boudning box to determine extrusion height
        max_dim = max(bbox_values['xmax'] - bbox_values['xmin'],
                      bbox_values['ymax'] - bbox_values['ymin'],
                      bbox_values['zmax'] - bbox_values['zmin'])
        height = max_dim * random.uniform(-3.0, 3.0)
        return f"solid={sketch_name}.add({loop_name}).extrude({height})\n"
    elif chosen_op == 'revolve':
        angle = random.uniform(0, 360)
        bbox_values = get_bbox_loop(code_thus_far, loop_name)
        start_point, end_point = get_revolve_axis_points(bbox_values, plane_name)
        print(start_point, end_point)
        return f"solid={sketch_name}.add({loop_name}).revolve(angle={angle}, axis=({start_point}, {end_point}))\n"

def run_single(loops_json_path, debug=False):
    loops = load_loops(loops_json_path)
    cadquery_code = "import cadquery as cq\n"

    if debug:
        print(f"Loaded {len(loops)} loop(s) from {loops_json_path}")
        for i, loop in enumerate(loops):
            print(f"Loop {i}: {len(loop)} features")
    
    if len(loops) == 0:
        print("No loops found in the JSON file.")
        return
    
    elif len(loops) > 1:
        raise NotImplementedError("Multiple loops not yet supported.")
    
    else: # handle single loops
        loop = loops[0]
        sketch_cq, plane, wp_name = cadquery_sketch(0)
        cadquery_code += sketch_cq
        loop_cq = cadquery_loop(loop, "loop0", wp_name)
        cadquery_code += loop_cq
        cadquery_code += perform_3d_op_on_loop("loop0", wp_name, cadquery_code, plane)
        
        if debug:
            print("*"*50)
            print(cadquery_code)

    # Save the CadQuery code to a file
    import os
    output_path = os.path.join(os.path.dirname(loops_json_path), "cq_code.py")
    with open(output_path, "w") as f:
        f.write(cadquery_code)
    print(f"Saved CadQuery code to: {output_path}")
    return

def main():
    import sys
    args = parse_args()

    # Check if neither argument is provided
    if args.single_json is None and args.multi_json_folder is None:
        print("Error: Please provide either --single_json or --multi_json_folder argument", file=sys.stderr)
        sys.exit(1)

    # If single_json is provided, use run_single
    if args.single_json is not None:
        run_single(args.single_json, debug=args.debug)

    # If multi_json_folder is provided, process all loops.json files in parallel
    if args.multi_json_folder is not None:
        input_jsons = get_multi_json_files(args.multi_json_folder)
        failed_files = []

        with ProcessPoolExecutor(max_workers=args.workers) as executor:

            # Submit all tasks
            future_to_item = {executor.submit(run_single, str(item)): item for item in input_jsons}
            for future in tqdm(as_completed(future_to_item), total=len(input_jsons),
                            desc=f"Processing {run_single.__name__}"):
                item = future_to_item[future]
                try:
                    result = future.result()
                except Exception as e:
                    failed_files.append((item, str(e)))
                    if args.debug:
                        print(f"\nError processing {item}: {e}")

        # Report summary at the end
        if failed_files:
            print(f"\n{len(failed_files)} file(s) failed to process:")
            for item, error in failed_files:
                print(f"  - {item}: {error}")

if __name__ == "__main__":
    main()
