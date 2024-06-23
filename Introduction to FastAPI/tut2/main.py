from fastapi import FastAPI, status
import uuid
from models import User

app = FastAPI()


users = {
    "1": {
        "name": "0xPb",
        "age": 25
    },
    "2": {
        "name": "Prashanth Bodepu",
        "age": 22
        }
}

@app.get("/users/")
def users_list():
    return users

@app.get("/users/{user_id}")
def user_detail(user_id: str):
    return users[user_id]

@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users[str(uuid.uuid4())] = user
    return "User created"

@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: str, user: User):
    users[user_id] = user
    return "User updated"

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return "User deleted"