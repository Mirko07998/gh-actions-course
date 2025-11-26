from fastapi import FastAPI, Form, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from utils import calculate

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class CalculationInput(BaseModel):
    first_number: float
    operator: str
    second_number: float


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request, "result": None, "error": None})


@app.post("/calculate", response_class=HTMLResponse)
async def calculate_result(
    request: Request,
    first_number: float = Form(...),
    operator: str = Form(...),
    second_number: float = Form(...)
):
    try:
        result = calculate(first_number, operator, second_number)
        return templates.TemplateResponse("calculator.html", {"request": request, "result": result, "error": None})
    except ValueError as e:
        return templates.TemplateResponse("calculator.html", {"request": request, "result": None, "error": str(e)})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)