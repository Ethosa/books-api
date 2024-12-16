from uvicorn.main import run
from dotenv import load_dotenv

from app import app
from database import cur, db


load_dotenv()


if __name__ == '__main__':
    run(app, port=5000, host='127.0.0.1')
