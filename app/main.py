from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.weather import fetch_weather
from app.etl.processor import normalize_weather

from app.reasoning.ai_engine import generate_result

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request, "result": None, "error": None},
    )


@app.post("/", response_class=HTMLResponse)
def analyze_weather(request: Request, city: str = Form(...)):
    raw_data = fetch_weather(city)

    if "error" in raw_data:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"request": request, "result": None, "error": raw_data["error"]},
        )

    processed = normalize_weather(raw_data)

    if not processed:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"request": request, "result": None, "error": "Could not process weather data."},
        )

    
    reasoning = generate_result(processed)

    result = {
        **processed,
        **reasoning
    }

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request, "result": result, "error": None},
    )