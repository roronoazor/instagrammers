from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import users as user_service
from app.utils.auth import decode_token

oauth2_scheme = OAuth2PasswordBearer("api/users")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_token(token)
    if not payload:
        raise error

    user = user_service.get_user_or_none(db, payload.get("email", ""))
    if user is None:
        raise error

    return user
