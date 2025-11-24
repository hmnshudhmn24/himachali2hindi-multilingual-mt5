from src.dataset_preprocessing import csv_to_jsonl
import json
def test_csv_to_jsonl(tmp_path):
    csv = tmp_path / 'd.csv'
    csv.write_text('source_dialect,text,target_hindi\nbilaspuri,mai khet jaa reha,मैं खेत जा रहा हूँ\n')
    out = tmp_path / 'out.jsonl'
    csv_to_jsonl(str(csv), str(out))
    data = out.read_text().strip().splitlines()
    obj = json.loads(data[0])
    assert 'input' in obj and 'target' in obj
