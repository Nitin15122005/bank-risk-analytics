from decimal import Decimal

from app.db.database import Base
from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    loan_id: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id"),
        nullable=False,
    )

    loan_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    purpose: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    loan_amount: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    interest_rate: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    tenure_months: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    emi: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="Pending",
    )


    approval_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="Pending",
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    customer = relationship(
        "Customer",
        back_populates="loans",
    )

    risk_assessments = relationship(
        "RiskAssessment",
        back_populates="loan",
        cascade="all, delete-orphan",
    )