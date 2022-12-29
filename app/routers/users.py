from fastapi import status
from fastapi.routing import APIRouter

from app.schemas import users as user_schema

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", status_code=status.HTTP_200_OK)
async def register_user(user_in: user_schema.UserCreate):
    pass


@router.get("/search", status_code=status.HTTP_200_OK)
async def search_users(
    text: str = None, min_followers: int = None, max_followers: int = None
):
    pass


@router.put("/profile", status_code=status.HTTP_200_OK)
async def update_user(user_in: user_schema.UserProfileIn):
    pass
