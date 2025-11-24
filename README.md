# 🏔️ Himachali → Hindi Multilingual Translator (mT5)

A specialized multilingual NLP model designed to translate local Himachali dialects into **standard Hindi**.  
This is one of the first open-source attempts to build a unified translator for:

- **Bilaspuri**
- **Mandeali**
- **Kangri**
- **Kulluvi**

Built using **google/mt5-small**, the model uses a sequence-to-sequence architecture fine-tuned on parallel dialect → Hindi pairs.

---

# 🚀 Features

- Translate 4+ Himachali dialects into Hindi
- Unified multilingual translation architecture
- Full ML workflow:
  - Dataset preprocessing
  - Training
  - Evaluation
  - Inference
  - API + UI
- Gradio demo interface
- FastAPI server endpoint
- Apache 2.0 license (commercial-friendly)
- HuggingFace model card included
- Extensible for future dialects

---

# 📁 Project Structure

```
himachali2hindi-multilingual-mt5/
│
├── data/
│   ├── raw/
│   │   └── parallel.csv
│   ├── processed/
│   │   └── dataset_clean.jsonl
│   └── README.md
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── dataset_preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   ├── inference.py
│   └── model_utils.py
│
├── app/
│   ├── api.py
│   └── ui.py
│
├── huggingface/
│   ├── model_card.md
│   ├── sample_inputs.txt
│   └── sample_outputs.txt
│
├── notebooks/
│   ├── 01-data-exploration.ipynb
│   ├── 02-training.ipynb
│   └── 03-evaluation.ipynb
│
├── model/
│   ├── tokenizer/
│   └── checkpoints/
│       └── best-model/
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_inference.py
│   └── test_training.py
│
├── README.md
├── LICENSE
└── requirements.txt
```

---

# ✨ Supported Dialects

| Dialect | Region |
|--------|--------|
| **Bilaspuri** | Bilaspur district |
| **Mandeali** | Mandi district |
| **Kangri** | Kangra district |
| **Kulluvi** | Kullu valley |

You can add more dialects (e.g., Sirmauri, Chambeali) simply by adding datapoints.

---

# 📡 Input Prompt Format

The model expects a standardized prompt:

```
dialect: <dialect> | translate: <sentence>
```

### Example:

```
dialect: bilaspuri | translate: mai khet jaa reha
```

Model Output:

```
मैं खेत जा रहा हूँ
```

---

# 🧾 Dataset Format

### **CSV (raw)**

```
source_dialect,text,target_hindi
bilaspuri,mai khet jaa reha,मैं खेत जा रहा हूँ
mandeali,tus kinne jaande ho?,तुम कहाँ जा रहे हो?
```

### **Processed JSONL**

```
{
  "input": "dialect: bilaspuri | translate: mai khet jaa reha",
  "target": "मैं खेत जा रहा हूँ"
}
```

Convert CSV → JSONL:

```bash
python -m src.dataset_preprocessing   --input data/raw/parallel.csv   --output data/processed/dataset_clean.jsonl
```

---

# 🏋️ Train the Model

```bash
python -m src.train
```

Outputs saved to:

```
model/checkpoints/best-model/
```

---

# 🧪 Evaluate

```bash
python -m src.evaluate
```

Metrics: **ROUGE-1**, **ROUGE-L**, and optionally **BLEU** / **chrF**.

---

# 🤖 Inference (Python)

```python
from src.inference import translate

out = translate("mai khet jaa reha", dialect="bilaspuri")
print(out)  # Expected: मैं खेत जा रहा हूँ
```

---

# 🌐 FastAPI Server

Start server:

```bash
uvicorn app.api:app --reload --port 8000
```

Send request:

```json
POST /translate
{
  "text": "mai khet jaa reha",
  "dialect": "bilaspuri"
}
```

---

# 🎨 Gradio Demo

```bash
python app/ui.py
```

UI lets users type dialect text + select dialect.

---

# 📦 Installation

```bash
pip install -r requirements.txt
```

Or create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

# 📝 HuggingFace Metadata (YAML)

```yaml
---
language:
  - hi
  - en
tags:
  - translation
  - himachali
  - bilaspuri
  - mandeali
  - kangri
  - kulluvi
license: apache-2.0
pipeline_tag: translation
model_name: himachali2hindi-multilingual-mt5
base_model: google/mt5-small
datasets:
  - custom
---
```

---

# ⚖️ License

This project uses the **Apache License 2.0**, which allows commercial use, modification, distribution, and private use.

---

# 🙏 Acknowledgements

- Himachali language speakers & communities  
- open-source contributors  
- Google mT5 team  
- Developers preserving regional languages

---

# ⚠️ Disclaimer

This model is a research prototype. Translations may be imperfect — verify critical content with native speakers.

