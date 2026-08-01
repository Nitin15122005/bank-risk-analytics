from app.db.database import Base
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.sql import func


class RiskAssessment(Base):
    __tablename__ = "risk_assessments"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    loan_id = Column(
        Integer,
        ForeignKey("loans.id"),
        nullable=False,
    )

    monthly_income = Column(
        Numeric(15, 2),
        nullable=False,
    )

    monthly_expenses = Column(
        Numeric(15, 2),
        nullable=False,
    )

    existing_emi = Column(
        Numeric(15, 2),
        nullable=False,
        default=0,
    )

    credit_score = Column(
        Integer,
        nullable=False,
    )

    employment_years = Column(
        Integer,
        nullable=False,
    )

    debt_to_income = Column(
        Numeric(5, 2),
        nullable=False,
    )

    risk_score = Column(
        Integer,
        nullable=False,
    )

    risk_level = Column(
        String(20),
        nullable=False,
    )

    recommendation = Column(
        String(30),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )