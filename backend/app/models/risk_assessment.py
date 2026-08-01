from decimal import Decimal

from app.db.database import Base
from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class RiskAssessment(Base):
    __tablename__ = "risk_assessments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id"),
        nullable=False,
    )

    loan_id: Mapped[int] = mapped_column(
        ForeignKey("loans.id"),
        nullable=False,
    )

    prediction: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    probability_of_default: Mapped[Decimal] = mapped_column(
        Numeric(5, 4),
        nullable=False,
    )

    risk_score: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    model_version: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="v1.0.0",
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    customer = relationship(
        "Customer",
        back_populates="risk_assessments",
    )

    loan = relationship(
        "Loan",
        back_populates="risk_assessments",
    )