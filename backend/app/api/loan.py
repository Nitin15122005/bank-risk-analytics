from app.db.session import get_db
from app.schemas.loan import LoanCreate, LoanResponse, LoanUpdate
from app.schemas.loan_prediction import LoanPredictionResponse
from app.services.loan_service import LoanService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/loans", tags=["Loans"])


@router.post("/", response_model=LoanPredictionResponse)
@router.post("/", response_model=LoanPredictionResponse)
def create_loan(
    loan: LoanCreate,
    db: Session = Depends(get_db),  # noqa: B008
):
    try:
        return LoanService.create(db, loan)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.get("/", response_model=list[LoanResponse])
def get_all_loans(
    db: Session = Depends(get_db),  # noqa: B008
):
    return LoanService.get_all(db)


@router.get("/{loan_id}", response_model=LoanResponse)
def get_loan(
    loan_id: str,
    db: Session = Depends(get_db),  # noqa: B008
):
    loan = LoanService.get_by_id(db, loan_id)

    if loan is None:
        raise HTTPException(
            status_code=404,
            detail="Loan not found",
        )

    return loan


@router.put("/{loan_id}", response_model=LoanResponse)
def update_loan(
    loan_id: str,
    data: LoanUpdate,
    db: Session = Depends(get_db),  # noqa: B008
):
    loan = LoanService.update(
        db,
        loan_id,
        data,
    )

    if loan is None:
        raise HTTPException(
            status_code=404,
            detail="Loan not found",
        )

    return loan