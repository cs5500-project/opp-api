from fastapi import FastAPI
import models
from database import engine
from routers import auth, cards, transactions, validations

# application
app = FastAPI()

# sets up database defined in engine
models.models.Base.metadata.create_all(bind=engine)

# Set API endpoints on router
app.include_router(auth.router)
app.include_router(cards.router)
app.include_router(transactions.router)
app.include_router(validations.router)
