from fastapi import APIRouter

from .users import users_router

router = APIRouter()

router.include_router(users_router)
