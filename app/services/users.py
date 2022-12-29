from sqlalchemy.orm import Session
from sqlalchemy.sql import or_

from app.models.users import User
from app.schemas.users import UserCreate, UserProfileIn


def list_users(
    db: Session,
    text: str = None,
    min_followers: int = None,
    max_followers: int = None,
):
    query = db.query(User)

    if text is not None:
        text = f"%{text}%"
        query = query.filter(or_(User.username.ilike(text), User.bio.ilike(text)))

    if min_followers:
        query = query.filter(User.follower_count >= min_followers)

    if max_followers:
        query = query.filter(User.follower_count <= max_followers)

    return query.order_by(User.created_at.asc()).all()


def get_user_or_none(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email.lower()).first()


def create_user(db: Session, user_in: UserCreate):
    user = User(email=user_in.email.lower())
    # TODO: add password hashing

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_user(db: Session, user: User, user_in: UserProfileIn):
    db.query(User).filter(User.id == user.id).update(
        {
            "username": user_in.username.lower(),
            "bio": user_in.bio or user.bio,
            "follower_count": user_in.follower_count,
        }
    )

    db.commit()
    db.refresh(user)

    return user
