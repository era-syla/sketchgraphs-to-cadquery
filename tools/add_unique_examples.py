# tools/add_unique_examples.py
# Add N new, non-overlapping sequences into an existing dataset folder.
# - Reads existing seq_* indices from OUT_DIR to avoid duplicates
# - Samples from .npy dataset (SketchGraphs flat dictionary)
# - Writes ops.json, meta.json, optional PNG
# - Updates/creates index.csv; appends to manifest.jsonl

import os, re, json, csv, random, argparse
from typing import List, Set, Tuple

from sketchgraphs.data import flat_array, sequence
from sketchgraphs.data.sequence import EdgeOp, NodeOp, ConstraintType

# -------------------------- helpers --------------------------

def find_existing_indices(out_dir: str) -> Set[int]:
    """Collect existing seq_* indices already present in out_dir."""
    existing = set()
    if not os.path.isdir(out_dir):
        return existing
    for name in os.listdir(out_dir):
        if not name.startswith("seq_"):
            continue
        m = re.search(r"seq_(\d+)", name)
        if m:
            existing.add(int(m.group(1)))
    return existing

def op_to_plain(op):
    if isinstance(op, NodeOp):
        label = getattr(op, "label", None)
        params = getattr(op, "parameters", {})
        return {
            "kind": "NodeOp",
            "label": getattr(label, "name", str(label)),
            "parameters": dict(params),
        }
    if isinstance(op, EdgeOp):
        label = getattr(op, "label", None)
        refs  = getattr(op, "references", None)
        params = getattr(op, "parameters", {})
        refs_plain = None
        if refs is not None:
            try:
                refs_plain = [(int(a), int(b)) for (a, b) in refs]
            except Exception:
                try:
                    refs_plain = [list(x) for x in refs]
                except Exception:
                    refs_plain = str(refs)
        return {
            "kind": "EdgeOp",
            "label": getattr(label, "name", str(label)),
            "references": refs_plain,
            "parameters": dict(params),
        }
    try:
        lbl = op[0]
        return {"kind": "Unknown", "head": getattr(lbl, "name", str(lbl)), "raw": repr(op)}
    except Exception:
        return {"kind": "Unknown", "raw": repr(op)}

def minimal_clean(seq_ops):
    """Drop Subnode edges (common noise) but otherwise leave sequence intact."""
    cleaned = []
    for op in seq_ops:
        if isinstance(op, EdgeOp):
            lbl = getattr(op, "label", op[0])
            if lbl == ConstraintType.Subnode:
                continue
        cleaned.append(op)
    return cleaned

def try_render_png(sketch, out_png: str) -> bool:
    """Render a quick PNG; returns True if written, False if skipped/failed."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from sketchgraphs.data import _plotting as plotting

        os.makedirs(os.path.dirname(out_png), exist_ok=True)
        fig, ax = plt.subplots(figsize=(5, 5))
        if hasattr(plotting, "plot_sketch"):
            plotting.plot_sketch(sketch, ax=ax)
        else:
            plotting.render_sketch(sketch, ax=ax)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")
        fig.savefig(out_png, dpi=180, bbox_inches="tight", pad_inches=0.05)
        plt.close(fig)
        return True
    except Exception as e:
        print(f"[render] skipped: {e}")
        return False

def read_existing_index_csv(index_csv_path: str) -> List[Tuple[int,int,int,str]]:
    rows = []
    if not os.path.exists(index_csv_path):
        return rows
    with open(index_csv_path, newline="") as f:
        r = csv.reader(f)
        header = next(r, None)
        for row in r:
            if not row: continue
            try:
                rows.append((int(row[0]), int(row[1]), int(row[2]), row[3]))
            except Exception:
                # tolerate malformed older rows
                pass
    return rows

def write_index_csv(index_csv_path: str, rows: List[Tuple[int,int,int,str]]) -> None:
    with open(index_csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["seq_index","n_entities","n_constraints","has_png"])
        for row in rows:
            w.writerow(row)

# -------------------------- main --------------------------

def main():
    ap = argparse.ArgumentParser(description="Add new, unique SketchGraphs sequences into an existing folder.")
    ap.add_argument("--data-path", default="sequence_data/sg_t16_validation.npy", help="Flat dictionary .npy file.")
    ap.add_argument("--out-dir",   default="filtered_dataset/complex_closed_500", help="Existing folder to extend.")
    ap.add_argument("--n",         type=int, default=2000, help="How many new sequences to add.")
    ap.add_argument("--seed",      type=int, default=42)
    ap.add_argument("--render",    action="store_true", help="Also render PNG previews for each new sequence.")
    ap.add_argument("--scan-limit",type=int, default=None, help="Only consider first K sequences from dataset when sampling.")
    ap.add_argument("--overwrite-existing", action="store_true",
                    help="If a seq_<idx> folder already exists, overwrite its files (default: skip).")
    args = ap.parse_args()

    random.seed(args.seed)
    os.makedirs(args.out_dir, exist_ok=True)

    # Load dataset
    print(f"[load] {args.data_path}")
    data = flat_array.load_dictionary_flat(args.data_path)
    seqs = data["sequences"]
    total = len(seqs)
    pool_size = total if args.scan_limit is None else min(args.scan_limit, total)
    print(f"[dataset] total={total}, pool={pool_size}")

    # Find existing indices to avoid duplicates
    existing = find_existing_indices(args.out_dir)
    print(f"[existing] found {len(existing)} already in {args.out_dir}")

    # Build candidate pool (exclude existing)
    pool = [i for i in range(pool_size) if i not in existing]
    if not pool:
        print("[abort] No available new indices (pool is empty after excluding existing).")
        return

    k = min(args.n, len(pool))
    picked = random.sample(pool, k)
    picked.sort()
    print(f"[sample] selected {k} new unique indices")

    index_csv_path = os.path.join(args.out_dir, "index.csv")
    manifest_path  = os.path.join(args.out_dir, "manifest.jsonl")

    # Load/merge existing index
    index_rows = read_existing_index_csv(index_csv_path)
    index_map = {row[0]: row for row in index_rows}  # seq_index -> row

    manifest = open(manifest_path, "a")  # append mode

    added = 0
    for idx in picked:
        s = seqs[idx]
        seq_dir = os.path.join(args.out_dir, f"seq_{idx}")
        if os.path.exists(seq_dir) and not args.overwrite_existing:
            print(f"[skip] seq_{idx} already exists (use --overwrite-existing to force).")
            continue

        try:
            cleaned = minimal_clean(s)
            sk = sequence.sketch_from_sequence(cleaned)
        except Exception as e:
            print(f"[skip {idx}] build error: {e}")
            continue

        os.makedirs(seq_dir, exist_ok=True)

        # ops.json
        ops_plain = [op_to_plain(op) for op in cleaned]
        with open(os.path.join(seq_dir, "ops.json"), "w") as f:
            json.dump(ops_plain, f, indent=2)

        # meta.json
        try:
            entities = list(sk.entities.values()) if hasattr(sk.entities, "values") else list(sk.entities)
            constraints = list(sk.constraints.values()) if hasattr(sk.constraints, "values") else list(sk.constraints)
        except Exception:
            entities, constraints = [], []
        meta = {"seq_index": idx, "n_entities": len(entities), "n_constraints": len(constraints)}
        with open(os.path.join(seq_dir, "meta.json"), "w") as f:
            json.dump(meta, f, indent=2)

        # optional PNG
        has_png = False
        if args.render:
            has_png = try_render_png(sk, os.path.join(seq_dir, f"seq_{idx}.png"))

        # update in-memory index rows (dedupe on seq_index)
        index_map[idx] = (idx, len(entities), len(constraints), "yes" if has_png else "no")

        # append to manifest.jsonl
        manifest.write(json.dumps({
            "path": f"seq_{idx}",
            "seq_index": idx,
            "n_entities": len(entities),
            "n_constraints": len(constraints),
            "has_png": has_png
        }) + "\n")

        added += 1
        if added % 200 == 0:
            print(f"[progress] added {added}/{k}...")

    manifest.close()

    # Write merged index.csv (existing + new)
    merged_rows = list(index_map.values())
    merged_rows.sort(key=lambda r: r[0])
    write_index_csv(index_csv_path, merged_rows)

    print(f"[done] added {added} new sequences into {args.out_dir}")
    print(f"[artifacts] updated {index_csv_path}; appended {manifest_path}")

if __name__ == "__main__":
    main()
