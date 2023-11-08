from fastapi import FastAPI, Depends
from starlette import status
from typing import Annotated
from models import models
from database.database import engine
from routers import auth
from routers.helpers import check_user_authentication
from routers.auth import get_current_user

# application
app = FastAPI()

# sets up database defined in engine
models.Base.metadata.create_all(bind=engine)

# Set API endpoints on router
app.include_router(auth.router)

user_dependency = Annotated[dict, Depends(get_current_user)]


@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency):
    check_user_authentication(user)
    return user