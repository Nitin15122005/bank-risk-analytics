from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    customer_id: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    first_name: Mapped[str] = mapped_column(String(100))

    last_name: Mapped[str] = mapped_column(String(100))

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
    )

    phone: Mapped[str] = mapped_column(String(20))

    date_of_birth: Mapped[date] = mapped_column(Date)

    gender: Mapped[str] = mapped_column(String(20))

    employment_type: Mapped[str] = mapped_column(String(50))

    annual_income: Mapped[float] = mapped_column(
        Numeric(15, 2)
    )

    credit_score: Mapped[int] = mapped_column(Integer)

    branch_id: Mapped[int] = mapped_column(
        ForeignKey("branches.id")
    )

    branch = relationship(
        "Branch",
        back_populates="customers",
    )