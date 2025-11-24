from datasets import load_dataset, load_metric
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from src.config import config

def evaluate(model_dir: str = None):
    model_dir = model_dir or config.output_dir
    ds = load_dataset('json', data_files=config.processed_data_path)['train']
    ds = ds.train_test_split(test_size=0.1, seed=config.seed)['test']

    tokenizer = AutoTokenizer.from_pretrained(model_dir, use_fast=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

    rouge = load_metric('rouge')
    preds, refs = [], []
    for item in ds:
        inputs = tokenizer(item['input'], return_tensors='pt', truncation=True).to(config.device)
        outs = model.generate(**inputs, max_length=config.max_target_length, num_beams=4)
        pred = tokenizer.decode(outs[0], skip_special_tokens=True)
        preds.append(pred)
        refs.append(item['target'])
    results = rouge.compute(predictions=preds, references=refs)
    print(results)

if __name__ == '__main__':
    evaluate()
