from app.models.loan import Loan
from sqlalchemy.orm import Session


class LoanRepository:

    @staticmethod
    def create(db: Session, loan: Loan):
        db.add(loan)
        db.commit()
        db.refresh(loan)
        return loan

    @staticmethod
    def get_by_id(db: Session, loan_id: str):
        return (
            db.query(Loan)
            .filter(Loan.loan_id == loan_id)
            .first()
        )

    @staticmethod
    def get_all(db: Session):
        return db.query(Loan).all()

    @staticmethod
    def get_customer_loans(db: Session, customer_id: int):
        return (
            db.query(Loan)
            .filter(Loan.customer_id == customer_id)
            .all()
        )

    @staticmethod
    def update(db: Session, loan: Loan):
        db.commit()
        db.refresh(loan)
        return loan