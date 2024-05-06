from fastapi import FastAPI
from database import engine
import models
import uvicorn
import users, products

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(users.router)
app.include_router(products.router)

