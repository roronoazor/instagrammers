from jose import JWTError, jwt

from app.settings import settings

SECRET_KEY = settings().SECRET_KEY
ALGO = "HS256"


def encode_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGO)


def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGO])
        return payload
    except JWTError:
        return None
