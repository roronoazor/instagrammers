from typing import Optional

import pydantic


class UserCreate(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: pydantic.SecretStr


class UserProfileIn(pydantic.BaseModel):
    username: str
    follower_count: int
    bio: Optional[str] = None

    class Config:
        orm_mode = True


class UserProfileOut(UserProfileIn):
    username: Optional[str] = None


class UserTokenOut(pydantic.BaseModel):
    token: str
    user: UserProfileOut
