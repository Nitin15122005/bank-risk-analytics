from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/register",
    response_model=UserResponse,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),  # noqa: B008
):
    try:
        return AuthService.register(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db),  # noqa: B008
):
    try:
        return AuthService.login(db, login_data)

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )

@router.get("/me")
def get_me(
    current_user=Depends(get_current_user),
):
    return current_user