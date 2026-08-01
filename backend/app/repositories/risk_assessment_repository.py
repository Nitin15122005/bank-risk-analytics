from app.models.risk_assessment import RiskAssessment
from sqlalchemy.orm import Session


class RiskAssessmentRepository:

    @staticmethod
    def create(
        db: Session,
        risk_assessment: RiskAssessment,
    ):
        db.add(risk_assessment)
        db.commit()
        db.refresh(risk_assessment)
        return risk_assessment

    @staticmethod
    def get_by_id(
        db: Session,
        assessment_id: int,
    ):
        return (
            db.query(RiskAssessment)
            .filter(
                RiskAssessment.id == assessment_id,
            )
            .first()
        )

    @staticmethod
    def get_by_loan(
        db: Session,
        loan_id: int,
    ):
        return (
            db.query(RiskAssessment)
            .filter(
                RiskAssessment.loan_id == loan_id,
            )
            .order_by(
                RiskAssessment.created_at.desc(),
            )
            .first()
        )

    @staticmethod
    def get_by_customer(
        db: Session,
        customer_id: int,
    ):
        return (
            db.query(RiskAssessment)
            .filter(
                RiskAssessment.customer_id == customer_id,
            )
            .order_by(
                RiskAssessment.created_at.desc(),
            )
            .all()
        )

    @staticmethod
    def get_all(
        db: Session,
    ):
        return (
            db.query(RiskAssessment)
            .order_by(
                RiskAssessment.created_at.desc(),
            )
            .all()
        )