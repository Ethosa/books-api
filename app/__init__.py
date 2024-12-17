from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mounts.user import user_app


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_headers="*",
    allow_methods="*",
    allow_origins="*",
    allow_credentials=True
)


app.mount('/user', user_app)
