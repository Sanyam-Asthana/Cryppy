from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import sys
import os

sys.path.append(os.path.dirname(__file__))
import decoder
import detector

import uvicorn

from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).parent.parent 

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get('/')
def root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post('/decode')
def decode(request: Request, enc_str: str = Form(...)):
    predictions = detector.detect_encodings(enc_str)
    results = decoder.decode_encodings(enc_str, predictions)

    results = {k: v for k, v in results.items() if v != "" and all(c.isprintable() or c in '\n\r\t' for c in v)}
    return templates.TemplateResponse(request, 
        "index.html",
        {
            "results": results,
            "input": enc_str
        }
    )

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
