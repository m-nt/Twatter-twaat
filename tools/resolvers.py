from typing import List, Union
import motor.motor_asyncio
import os
from fastapi.encoders import jsonable_encoder
from models.Schemas import *
from models.Datatypes import *
from tools.useful import *
import dotenv

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client["twatter"]


async def add_twaat(twaat: TwaatInput, token: str) -> TwaatReturn:
    is_login = await check_if_loggin(token)
    if is_login is False:
        return TwaatReturn({})
    data = jsonable_encoder(twaat)
    insert = await db["twaats"].insert_one(data)
    result = await db["twaats"].find_one({"_id": insert.inserted_id})
    if result:
        return TwaatReturn.parse_obj(result)
    return TwaatReturn({})


def echo(self, echo: Union[str, None] = "") -> str:
    return echo
