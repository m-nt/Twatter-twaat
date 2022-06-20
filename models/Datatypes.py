import strawberry
from pydantic import Field


@strawberry.type
class Twaat:
    pk: str
    message: str
    id: str = ""
    reply_to: str = ""
    like_to: str = ""

    def __init__(self, dict):
        self.__dict__ = dict

    @staticmethod
    def parse_obj(dict):
        return Twaat(dict=dict)


@strawberry.input
class TwaatInput:
    pk: str
    message: str
    reply_to: str = ""
    like_to: str = ""


@strawberry.type
class TwaatReturn:
    id: str = ""
    pk: str = ""
    message: str = ""
    reply_to: str = ""
    like_to: str = ""

    def __init__(self, dict):
        self.__dict__ = dict

    @staticmethod
    def parse_obj(dict):
        return TwaatReturn(dict=dict)


@strawberry.type
class User:
    username: str = ""
    password: str = ""
    email: str = ""
    full_name: str = ""
    token: str = ""

    def __init__(self, dict):
        self.__dict__ = dict

    @staticmethod
    def parse_obj(dict):
        return User(dict=dict)


@strawberry.input
class UserInput:
    username: str = ""
    password: str = ""
    email: str = ""
    full_name: str = ""
    token: str = ""
