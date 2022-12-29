from fastapi import Depends, status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import users as user_schema
from app.services import users as user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", status_code=status.HTTP_200_OK)
async def register_user(
    user_in: user_schema.UserCreate,
    db: Session = Depends(get_db),
):
    pass


@router.get("/search", status_code=status.HTTP_200_OK)
async def search_users(
    text: str = None,
    min_followers: int = None,
    max_followers: int = None,
    db: Session = Depends(get_db),
):
    users = user_service.list_users(db, text, min_followers, max_followers)
    return users


@router.put("/profile", status_code=status.HTTP_200_OK)
async def update_user(
    user_in: user_schema.UserProfileIn, db: Session = Depends(get_db)
):
    pass
