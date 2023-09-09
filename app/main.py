from fastapi import FastAPI,Request
import random
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@app.get("/random")
def get_random():
    result: int = random.randint(0,100)
    return {'number': result, 'limit' : 100}