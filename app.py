from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Montar carpeta de archivos estáticos
app.mount("/img", StaticFiles(directory="static"), name="static")

# Configurar carpeta de plantillas
templates = Jinja2Templates(directory="template")

# Ruta que renderiza la plantilla
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})
