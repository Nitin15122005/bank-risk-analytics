from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.sql import func

from app.db.base import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    loan_id = Column(
        String(20),
        unique=True,
        nullable=False,
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False,
    )

    loan_type = Column(
        String(50),
        nullable=False,
    )

    loan_amount = Column(
        Numeric(15, 2),
        nullable=False,
    )

    interest_rate = Column(
        Numeric(5, 2),
        nullable=False,
    )

    tenure_months = Column(
        Integer,
        nullable=False,
    )

    emi = Column(
        Numeric(15, 2),
        nullable=False,
    )

    status = Column(
        String(30),
        default="Pending",
        nullable=False,
    )

    risk_score = Column(
        Integer,
        nullable=True,
    )

    approval_status = Column(
        String(30),
        default="Pending",
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )