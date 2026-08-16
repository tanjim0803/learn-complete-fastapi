from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


class User(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr


USERS = [
    {
        "id": 1,
        "name": "Tanjim Ahmed",
        "email": "tanjim@gmail.com",
    },
    {
        "id": 2,
        "name": "Tanim Ahmed",
        "email": "tanim@gmail.com",
    },
    {
        "id": 3,
        "name": "Tamim Ahmed",
        "email": "tamim@gmail.com",
    },
]


@app.get("/users")
async def get_users():
    return USERS


@app.post("/user")
async def create_user(user: User):
    id = USERS[len(USERS) - 1]["id"] + 1
    new_user = {"id": id, **user.model_dump()}
    USERS.append(new_user)
    return new_user


@app.put("/user/{id}")
async def update_user(id: int, updated_user: User):
    for user in USERS:
        if user["id"] == id:
            user["name"] = updated_user.name
            user["email"] = updated_user.email

    return updated_user
