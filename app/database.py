from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import settings

DATABASE_URL = (
    f"postgresql+psycopg2://{settings().DB_USER}:{settings().DB_PASS}"
    f"@{settings().DB_HOST}:{settings().DB_PORT}/{settings().DB_NAME}"
)

engine = create_engine(DATABASE_URL)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
