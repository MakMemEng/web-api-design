from fastapi import APIRouter
from typing import Dict

router = APIRouter()

user_list = ["John", "Jane", "Jack", "Jill"]


@router.get("/users")
def get_users():
    return {"users": user_list}


@router.get("/users/{index}")
def get_user(index: int):
    return {"user": user_list[index]}


@router.post("/users")
def create_user(json: Dict):
    user = json.get("user")
    user_list.append(user)
    return {"message": "Successfully created."}


@router.put("/users/{index}")
def update_user(index: int, json: Dict):
    user = json.get("user")
    user_list[index] = user
    return {"message": "Successfully updated."}


@router.delete("/users/{index}")
def delete_user(index: int):
    user_list.pop(index)
    return {"message": "Successfully deleted."}
