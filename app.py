from fastapi import FastAPI
from routers.auth import auth

app = FastAPI(
    responses={
        404: {"error": "not_found"},
        418: {"error": "I'm a teapot."}
    }
)
app.title = "hanul.cat"
app.version = "1.0.0"
app.include_router(auth.router)