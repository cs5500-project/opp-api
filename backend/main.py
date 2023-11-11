from fastapi import FastAPI, Depends
from starlette import status
from typing import Annotated
import models.models
from database import engine
from routers import auth, cards

# application
app = FastAPI()

# sets up database defined in engine
models.models.Base.metadata.create_all(bind=engine)

# Set API endpoints on router
app.include_router(auth.router)
app.include_router(cards.router)
