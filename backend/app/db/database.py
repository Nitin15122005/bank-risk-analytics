from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Create PostgreSQL engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
)

# Create database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)