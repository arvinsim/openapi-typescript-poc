from typing import Union
from fastapi.openapi.utils import get_openapi

from fastapi import FastAPI

app = FastAPI()

app.openapi_version = "3.0.0"

users = [
    {"id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 25, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": 35, "email": "charlie@example.com"},
    {"id": 4, "name": "Diana", "age": 28, "email": "diana@example.com"},
    {"id": 5, "name": "Ethan", "age": 22, "email": "ethan@example.com"},
    {"id": 6, "name": "Felicia", "age": 29, "email": "fiona@example.com"},
    {"id": 7, "name": "George", "age": 32, "email": "george@example.com"},
    {"id": 8, "name": "Hannah", "age": 24, "email": "hannah@example.com"},
    {"id": 9, "name": "Ian", "age": 27, "email": "ian@example.com"},
    {"id": 10, "name": "Jenna", "age": 26, "email": "jenna@example.com"}
]


@app.get("/users")
def read_users():
    return users


@app.get("/users/{user_id}")
def read_user(user_id: int, q: Union[str, None] = None):
    for user in users:
        if user_id == user.get('id'):
            return user
    raise Exception(f'There is no user of id: {user_id}')


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        summary="This is a very custom OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
