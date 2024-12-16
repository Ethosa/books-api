from pydantic import BaseModel


class RegisterUser(BaseModel):
    login: str
    password: str


class LoginUser(BaseModel):
    login: str
    password: str
