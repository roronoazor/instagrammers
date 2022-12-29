from fastapi import status
from fastapi.routing import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", status_code=status.HTTP_200_OK)
async def register_user():
    pass


@router.get("/search", status_code=status.HTTP_200_OK)
async def search_users():
    pass


@router.put("/profile", status_code=status.HTTP_200_OK)
async def update_user():
    pass
