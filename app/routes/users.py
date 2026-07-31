from fastapi import APIRouter, HTTPException

TAG_USERS = "Users"

users_router = APIRouter(prefix="/users", tags=[TAG_USERS])


@users_router.get("/get_all", summary="Get all users")
def get_users():
    return {"message": "This endpoint will return all users."}
