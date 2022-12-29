from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    follower_count = Column(Integer)
    bio = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
