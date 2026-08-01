from decimal import Decimal

from app.ml.predictor import Predictor
from app.models.customer import Customer
from app.models.loan import Loan
from app.repositories.loan_repository import LoanRepository
from app.services.risk_assessment_service import RiskAssessmentService
from sqlalchemy.orm import Session


class LoanService:

    @staticmethod
    def calculate_emi(
        principal: Decimal,
        annual_rate: Decimal,
        months: int,
    ):
        r = float(annual_rate) / 12 / 100
        p = float(principal)

        if r == 0:
            return round(p / months, 2)

        emi = (
            p * r * (1 + r) ** months
            / ((1 + r) ** months - 1)
        )

        return round(emi, 2)

    @staticmethod
    def generate_loan_id(db: Session):
        count = db.query(Loan).count() + 1
        return f"LN{count:06d}"

    @staticmethod
    def create(
        db: Session,
        data,
    ):

        customer = (
            db.query(Customer)
            .filter(Customer.id == data.customer_id)
            .first()
        )

        if customer is None:
            raise ValueError("Customer not found")

        loan = Loan(
            loan_id=LoanService.generate_loan_id(db),
            customer_id=data.customer_id,
            loan_type=data.loan_type,
            purpose=data.purpose,
            loan_amount=data.loan_amount,
            interest_rate=data.interest_rate,
            tenure_months=data.tenure_months,
            emi=LoanService.calculate_emi(
                data.loan_amount,
                data.interest_rate,
                data.tenure_months,
            ),
        )

        loan = LoanRepository.create(
            db,
            loan,
        )

        prediction = Predictor.predict(
            customer,
            loan,
        )

        assessment = RiskAssessmentService.create(
            db=db,
            customer_id=customer.id,
            loan_id=loan.id,
            prediction=prediction["prediction"],
            probability_of_default=prediction["probability_of_default"],
            risk_score=prediction["risk_score"],
            model_version=prediction["model_version"],
        )

        return {
            "loan": loan,
            "risk_assessment": assessment,
        }

    @staticmethod
    def get_all(db: Session):
        return LoanRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db: Session,
        loan_id: str,
    ):
        return LoanRepository.get_by_id(
            db,
            loan_id,
        )

    @staticmethod
    def update(
        db: Session,
        loan_id: str,
        data,
    ):

        loan = LoanRepository.get_by_id(
            db,
            loan_id,
        )

        if loan is None:
            return None

        if data.status is not None:
            loan.status = data.status

        if data.approval_status is not None:
            loan.approval_status = data.approval_status

        if getattr(data, "purpose", None) is not None:
            loan.purpose = data.purpose

        return LoanRepository.update(
            db,
            loan,
        )