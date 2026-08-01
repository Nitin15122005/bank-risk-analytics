from datetime import datetime, timedelta, timezone
from typing import Any

from app.core.config import settings
from jose import jwt
from pwdlib import PasswordHash

# Password hasher
password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """Hash a plain text password."""
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against stored hash."""
    return password_hash.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(data: dict[str, Any]) -> str:
    """Generate JWT access token."""

    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )