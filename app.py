from datetime import date
from fastapi import FastAPI
from fastapi_crudrouter.core.tortoise import TortoiseCRUDRouter
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
import hashlib
import os
from dotenv import load_dotenv
from models import User
from schemas import UserSchema, UserSchemaCreate, UserSchemaUpdate

load_dotenv()

db_connection = "{0}://{1}:{2}@{3}:{4}/{5}".format(os.getenv("DB_DRIVER"), os.getenv("DB_USERNAME"),
                                                   os.getenv("DB_PASSWORD"),
                                                   os.getenv("DB_HOST"), os.getenv("DB_PORT"), os.getenv("DB_NAME"))

TORTOISE_ORM = {
    "connections": {"default": db_connection},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


app = FastAPI(
    title="testAPI",
    description="test API",
    version="0.1.0"
)

register_tortoise(app, config=TORTOISE_ORM)

router = TortoiseCRUDRouter(
    schema=UserSchema,
    create_schema=UserSchemaCreate,
    update_schema=UserSchemaUpdate,
    db_model=User,
)


@router.post("")
async def overloaded_create(item: UserSchemaCreate):
    data = item.dict(exclude_unset=True)
    data['password'] = hashlib.md5(data['password'].encode("utf-8")).hexdigest()
    data['register_date'] = date.today()
    await User.create(**data)
    return "User created successfully"


app.include_router(router)
