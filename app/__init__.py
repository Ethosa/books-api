from fastapi import FastAPI
from mounts.user import user_app


app = FastAPI(
    version='1.0.0',
    description='Books API'
)

app.mount('/user', user_app)
