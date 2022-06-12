import io
import base64

from PIL import Image
from pydantic import BaseModel

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse 
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates 


app = FastAPI() 

templates = Jinja2Templates(directory="templates") 
app.mount("/static", StaticFiles(directory="static"), name="static") 

@app.get('/', response_class=HTMLResponse) 
def home(request: Request): 
	return templates.TemplateResponse("home.html", {"request": request})

class uploaded_image(BaseModel):
    filename:str
    filedata:str

@app.post("/upload64")
async def upload(uploaded_image:uploaded_image):
    filename = uploaded_image.filename
    filedata = uploaded_image.filedata
    try:
        img_recovered = base64.b64decode(filedata)
        dataBytesIO = io.BytesIO(img_recovered)
        image = Image.open(dataBytesIO)
        image.save(filename)
    except Exception:
        return {"message": "There was an error uploading the file"}
    
    inference = "오리"

    return {
        "message": f"Successfuly uploaded {filename}",
        "inference": inference,
    }

@app.get("/game", response_class=HTMLResponse) 
async def read_item(request: Request): 
	return templates.TemplateResponse("game.html", {"request": request}) 
