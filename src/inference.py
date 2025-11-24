from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from src.config import config

_cache = {}

def _load(model_dir=None):
    model_dir = model_dir or config.output_dir
    if model_dir not in _cache:
        tokenizer = AutoTokenizer.from_pretrained(model_dir, use_fast=True)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_dir).to(config.device)
        _cache[model_dir] = (tokenizer, model)
    return _cache[model_dir]

def translate(text: str, dialect: str = "bilaspuri", model_dir: str = None, max_length: int = None):
    tokenizer, model = _load(model_dir)
    prompt = f"dialect: {dialect.strip().lower()} | translate: {text}"
    max_length = max_length or config.max_target_length
    inputs = tokenizer(prompt, return_tensors='pt', truncation=True).to(config.device)
    outputs = model.generate(**inputs, max_length=max_length, num_beams=4)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
