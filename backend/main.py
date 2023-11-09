from fastapi import FastAPI, Depends
from starlette import status
from typing import Annotated
import models
from database import engine
from routers import auth
from routers.helpers import check_user_authentication
from routers.auth import get_current_user

# application
app = FastAPI()

# sets up database defined in engine
models.Base.metadata.create_all(bind=engine)

# Set API endpoints on router
app.include_router(auth.router)
