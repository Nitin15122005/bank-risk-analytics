from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class LoanCreate(BaseModel):
    customer_id: int
    loan_type: str
    loan_amount: Decimal
    interest_rate: Decimal
    tenure_months: int


class LoanUpdate(BaseModel):
    status: str | None = None
    approval_status: str | None = None
    risk_score: int | None = None


class LoanResponse(BaseModel):
    id: int
    loan_id: str
    customer_id: int
    loan_type: str
    loan_amount: Decimal
    interest_rate: Decimal
    tenure_months: int
    emi: Decimal
    status: str
    approval_status: str
    risk_score: int | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)