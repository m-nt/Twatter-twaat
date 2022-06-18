from passlib.context import CryptContext
from jose import JWTError, jwt
import time
import motor
from requests import *
import os
from models.Datatypes import *
from fastapi.encoders import jsonable_encoder


async def check_if_loggin(token: str) -> bool:
    # request the auth service for checking
    data = {"token": token}
    res = post(url=os.getenv("AUTH_URL") + "token/checklogin", json=data)
    auth_res = jsonable_encoder(res.text)
    if "username" not in auth_res:
        return False
    return True


def verify_password(pwd_context: CryptContext, plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(pwd_context: CryptContext, password):
    return pwd_context.hash(password)
