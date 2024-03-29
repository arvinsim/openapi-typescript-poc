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


@app.get(
    "/users",
    summary="Get all users",
    description="Get the user information of all users",
)
def read_users():
    return users


@app.get(
    "/users/{user_id}",
    summary="Get a specific user",
    description="Get a specific user's information based on the user id provided",
    )
def read_user(user_id: int, q: Union[str, None] = None):
    for user in users:
        if user_id == user.get('id'):
            return user
    raise Exception(f'There is no user of id: {user_id}')