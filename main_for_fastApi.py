from fastapi import FastAPI
from models import User
from typing import List
from models import Gender

app = FastAPI()

db: list[User]=[
    User(
        first_name='yusuf',
        last_name='sobhy',
        gender='male'
        )

]

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI is working!"}

@app.get("/api/h3")
async def user_fetch():
    return db ;

@app.post("/")
async def new_user(user:User):
    db.append(user)
    return {'id',user.id}
