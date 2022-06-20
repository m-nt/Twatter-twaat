import strawberry
from typing import List
from models.Datatypes import *
from pydantic import Field


@strawberry.type
class Schema:
    twaats: List[Twaat]


@strawberry.type
class ATwaat:
    twaat: Twaat = None
    liked: int = 0
    replys: List[Twaat] = Field(default=[])
