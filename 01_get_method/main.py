from fastapi import FastAPI

app = FastAPI()

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
