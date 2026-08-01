from datetime import date
from decimal import Decimal

from app.core.enums import (
    CheckingAccountEnum,
    EmploymentTypeEnum,
    HousingEnum,
    SavingAccountEnum,
)
from pydantic import BaseModel, ConfigDict, EmailStr


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str

    date_of_birth: date
    gender: str

    employment_type: EmploymentTypeEnum

    housing: HousingEnum
    saving_account: SavingAccountEnum
    checking_account: CheckingAccountEnum

    annual_income: Decimal
    monthly_expenses: Decimal

    employment_years: int
    credit_score: int

    branch_id: int

class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None

    employment_type: EmploymentTypeEnum | None = None

    housing: HousingEnum | None = None

    saving_account: SavingAccountEnum | None = None

    checking_account: CheckingAccountEnum | None = None

    annual_income: Decimal | None = None
    monthly_expenses: Decimal | None = None

    employment_years: int | None = None
    credit_score: int | None = None

    branch_id: int | None = None


class CustomerResponse(CustomerBase):
    id: int
    customer_id: str

    model_config = ConfigDict(
        from_attributes=True,
    )