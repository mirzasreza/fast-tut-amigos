from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Reza",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Mirza",
        last_name="Reza",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "World"}
    