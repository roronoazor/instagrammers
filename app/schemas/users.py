import pydantic


class UserCreate(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: pydantic.SecretStr


class UserProfileIn(pydantic.BaseModel):
    username: str
    follower_count: int
    bio: str | None = None

    class Config:
        orm_mode = True
