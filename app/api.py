from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import translate

app = FastAPI(title="Himachali → Hindi Translator API")

class Request(BaseModel):
    text: str
    dialect: str = "bilaspuri"

@app.post("/translate")
async def translate_api(req: Request):
    out = translate(req.text, req.dialect)
    return {"dialect": req.dialect, "input": req.text, "translation": out}

@app.get("/")
async def root():
    return {"message": "POST /translate with JSON {text, dialect}."}
