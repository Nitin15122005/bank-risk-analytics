from app.api.loan import router as loan_router
from app.api.v1 import risk_assessment
from app.api.v1.auth import router as auth_router
from app.api.v1.customers import router as customer_router
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

register_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(loan_router)

app.include_router(risk_assessment.router)

app.include_router(
    auth_router,
    prefix="/api/v1",
)

app.include_router(
    customer_router,
    prefix="/api/v1",
)


@app.get("/")
def root():
    return {
        "message": settings.APP_NAME,
    }