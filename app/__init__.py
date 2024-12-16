from fastapi import FastAPI
from mounts.user import user_app


app = FastAPI()


app.mount('/user', user_app)
