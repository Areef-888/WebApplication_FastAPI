from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import logging
from  app.routers import auth



app=FastAPI()

app.include_router(auth.router)

