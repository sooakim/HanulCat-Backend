from fastapi import FastAPI

from database.entity import *
from database.database import Base, engine
from routers.auth import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    debug=True,
    responses={
        404: {"error": "not_found"},
        418: {"error": "I'm a teapot."}
    }
)
app.title = "hanul.cat"
app.version = "1.0.0"
app.include_router(auth.router)