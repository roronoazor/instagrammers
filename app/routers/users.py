from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import users as user_schema
from app.services import users as user_service
from app.utils.auth import encode_token

from .dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "", status_code=status.HTTP_200_OK, response_model=user_schema.UserTokenOut
)
async def register_user(
    user_in: user_schema.UserCreate,
    db: Session = Depends(get_db),
):
    try:
        user = user_service.create_user(db, user_in)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email exists already"
        )

    payload = {"email": user.email}
    token = encode_token(payload)

    return dict(user=user, token=token)


@router.get(
    "/search",
    status_code=status.HTTP_200_OK,
    response_model=list[user_schema.UserProfileOut],
)
async def search_users(
    text: str = None,
    min_followers: int = None,
    max_followers: int = None,
    db: Session = Depends(get_db),
):
    users = user_service.list_users(db, text, min_followers, max_followers)
    return users


@router.put(
    "/profile",
    status_code=status.HTTP_200_OK,
    response_model=user_schema.UserProfileOut,
)
async def update_user(
    user_in: user_schema.UserProfileIn,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    try:
        return user_service.update_user(db, user, user_in)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username exists already",
        )
