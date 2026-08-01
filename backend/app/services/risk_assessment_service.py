from app.models.risk_assessment import RiskAssessment
from app.repositories.risk_assessment_repository import (
    RiskAssessmentRepository,
)
from sqlalchemy.orm import Session


class RiskAssessmentService:

    @staticmethod
    def create(
        db: Session,
        customer_id: int,
        loan_id: int,
        prediction: str,
        probability_of_default: float,
        risk_score: float,
        model_version: str = "v1.0.0",
    ):
        assessment = RiskAssessment(
            customer_id=customer_id,
            loan_id=loan_id,
            prediction=prediction,
            probability_of_default=probability_of_default,
            risk_score=risk_score,
            model_version=model_version,
        )

        return RiskAssessmentRepository.create(
            db,
            assessment,
        )

    @staticmethod
    def get_by_id(
        db: Session,
        assessment_id: int,
    ):
        return RiskAssessmentRepository.get_by_id(
            db,
            assessment_id,
        )

    @staticmethod
    def get_by_loan(
        db: Session,
        loan_id: int,
    ):
        return RiskAssessmentRepository.get_by_loan(
            db,
            loan_id,
        )

    @staticmethod
    def get_by_customer(
        db: Session,
        customer_id: int,
    ):
        return RiskAssessmentRepository.get_by_customer(
            db,
            customer_id,
        )

    @staticmethod
    def get_all(
        db: Session,
    ):
        return RiskAssessmentRepository.get_all(db)