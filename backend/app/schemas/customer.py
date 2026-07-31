from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, EmailStr


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    date_of_birth: date
    gender: str
    employment_type: str
    annual_income: Decimal
    credit_score: int
    branch_id: int


class CustomerUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    date_of_birth: date | None = None
    gender: str | None = None
    employment_type: str | None = None
    annual_income: Decimal | None = None
    credit_score: int | None = None
    branch_id: int | None = None


class CustomerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    customer_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    date_of_birth: date
    gender: str
    employment_type: str
    annual_income: Decimal
    credit_score: int
    branch_id: int