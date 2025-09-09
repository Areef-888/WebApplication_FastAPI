from fastapi import APIRouter, Form
from app.Schemas.user import UserDetails
from fastapi.templating import Jinja2Templates
from fastapi import Request
import logging
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import SecretStr
from app.services.userdetailsvalidation import Validations

logging.info("calling the html code from the templates")
templates=Jinja2Templates(directory='app/templates')

router=APIRouter()


logging.info("Calling loginPage")
@router.get("/login",response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

@router.post("/login")
async def logindetails(username:str=Form(...),password:SecretStr=Form(...)):
    data=UserDetails(user_name=username,password=password)
    logindetails=Validations.userloginvalidations(username,password)
    
    return RedirectResponse(url="/home",status_code=303)


@router.get("/home")
async def homepage(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})










