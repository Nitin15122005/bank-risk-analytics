
from app.db.session import get_db
from app.schemas.risk_assessment import RiskAssessmentResponse
from app.services.risk_assessment_service import RiskAssessmentService
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/risk-assessments",
    tags=["Risk Assessments"],
)


@router.get(
    "/",
    response_model=list[RiskAssessmentResponse],
)
def get_all(
    db: Session = Depends(get_db),  # noqa: B008
):
    return RiskAssessmentService.get_all(db)


@router.get(
    "/{assessment_id}",
    response_model=RiskAssessmentResponse,
)
def get_by_id(
    assessment_id: int,
    db: Session = Depends(get_db),  # noqa: B008
):
    return RiskAssessmentService.get_by_id(
        db,
        assessment_id,
    )


@router.get(
    "/loan/{loan_id}",
    response_model=RiskAssessmentResponse,
)
def get_by_loan(
    loan_id: int,
    db: Session = Depends(get_db),  # noqa: B008
):
    return RiskAssessmentService.get_by_loan(
        db,
        loan_id,
    )


@router.get(
    "/customer/{customer_id}",
    response_model=list[RiskAssessmentResponse],
)
def get_by_customer(
    customer_id: int,
    db: Session = Depends(get_db),  # noqa: B008
):
    return RiskAssessmentService.get_by_customer(
        db,
        customer_id,
    )