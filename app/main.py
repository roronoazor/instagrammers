from fastapi import FastAPI

from app.routers import router

app = FastAPI(
    title="Instagrammers",
    description="An instagram influencer search portal",
)
app.include_router(router)
