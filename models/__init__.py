from pydantic import BaseModel


class RegisterUser(BaseModel):
    login: str
    password: str
