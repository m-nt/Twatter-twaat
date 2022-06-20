import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import dotenv
from models.Datatypes import *
from models.Schemas import *
from tools.resolvers import *


dotenv.load_dotenv()


@strawberry.type
class Query:
    twaat: ATwaat = strawberry.field(resolver=get_twaat)
    twaats: Schema = strawberry.field(resolver=get_twaats)
    echo: Union[str, None] = strawberry.field(resolver=echo)


@strawberry.type
class Mutaion:
    add_twaat: TwaatReturn = strawberry.field(resolver=add_twaat)


schema = strawberry.Schema(Query, mutation=Mutaion)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
