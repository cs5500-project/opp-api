from fastapi import FastAPI
from models import models
from database.database import engine
from routers import auth

# application
app = FastAPI()

# sets up database defined in engine
models.Base.metadata.create_all(bind=engine)

# Set API endpoints on router
app.include_router(auth.router)
