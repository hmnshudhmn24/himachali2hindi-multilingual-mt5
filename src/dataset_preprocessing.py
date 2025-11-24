import argparse
import csv
import json
from pathlib import Path

def csv_to_jsonl(input_csv: str, output_jsonl: str,
                 src_col: str = "source_dialect",
                 text_col: str = "text",
                 tgt_col: str = "target_hindi"):
    p_in = Path(input_csv)
    p_out = Path(output_jsonl)
    p_out.parent.mkdir(parents=True, exist_ok=True)
    with p_in.open(encoding='utf-8') as fin, p_out.open('w', encoding='utf-8') as fout:
        reader = csv.DictReader(fin)
        for row in reader:
            dialect = (row.get(src_col) or "").strip().lower()
            text = (row.get(text_col) or "").strip()
            target = (row.get(tgt_col) or "").strip()
            if not dialect or not text or not target:
                continue
            inp = f"dialect: {dialect} | translate: {text}"
            fout.write(json.dumps({"input": inp, "target": target}, ensure_ascii=False) + "\n")

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    csv_to_jsonl(args.input, args.output)
