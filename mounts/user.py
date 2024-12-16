import os

from fastapi import FastAPI
from jwt import decode, encode
from werkzeug.security import check_password_hash, generate_password_hash
from fastapi.responses import JSONResponse

from models import RegisterUser
from database import cur, db


user_app = FastAPI(root_path='/')


@user_app.post('/user/')
async def create_new_user(user: RegisterUser):
    existing_user = cur.execute('SELECT (id) FROM user WHERE login = ?', [user.login]).fetchone()
    if existing_user is not None:
        return JSONResponse({'message': 'Логин занят'}, status_code=400)
    hashed_password = generate_password_hash(user.password)
    cur.execute('INSERT INTO user (login, password) VALUES (?, ?)', [
        user.login, hashed_password
    ])
    db.commit()
    token = encode({'user': user.login}, os.getenv('JWT_SECRET'))
    return {'response': token}
