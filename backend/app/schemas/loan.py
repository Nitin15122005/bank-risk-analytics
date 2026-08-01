from datetime import datetime
from decimal import Decimal

from app.core.enums import LoanTypeEnum, PurposeEnum
from pydantic import BaseModel, ConfigDict


class LoanBase(BaseModel):
    customer_id: int

    loan_type: LoanTypeEnum
    purpose: PurposeEnum

    loan_amount: Decimal
    interest_rate: Decimal

    tenure_months: int

class LoanCreate(LoanBase):
    pass


class LoanUpdate(BaseModel):
    status: str | None = None
    approval_status: str | None = None
    purpose: PurposeEnum | None = None


class LoanResponse(LoanBase):
    id: int
    loan_id: str

    emi: Decimal

    status: str
    approval_status: str

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)