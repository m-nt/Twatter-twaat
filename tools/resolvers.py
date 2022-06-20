from typing import List, Union
import motor.motor_asyncio
import os
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from models.Schemas import *
from models.Datatypes import *
from tools.useful import *

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


async def get_twaat(twaat_id: str, token: Union[str, None] = "") -> ATwaat:
    is_login = await check_if_loggin(token)
    if is_login is False:
        return ATwaat()
    twaat = await db["twaats"].find_one({"_id": ObjectId(twaat_id)})
    print(twaat)
    the_twaat = Twaat(twaat)
    like_to = await db["twaats"].find({"like_to": twaat_id}).to_list(1000000)
    liked = len(like_to)
    reply_to = await db["twaats"].find({"reply_to": twaat_id}).to_list(1000000)
    print(reply_to)
    replyed: List[Twaat] = []
    for document in reply_to:
        replyed.append(Twaat(dict=document))
    return ATwaat(twaat=the_twaat, liked=liked, replys=replyed)


async def get_twaats(
    self, token: Union[str, None] = "", count: Union[int, None] = 10
) -> Schema:
    is_login = await check_if_loggin(token)
    if is_login is False:
        return Schema([])
    result = await db["twaats"].find().to_list(length=count)
    twaats: List[Twaat] = []
    for document in result:
        twaats.append(Twaat(dict=document))
    return Schema(twaats=twaats)


def echo(self, echo: Union[str, None] = "") -> str:
    return echo
