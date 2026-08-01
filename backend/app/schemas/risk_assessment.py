from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class RiskAssessmentResponse(BaseModel):
    id: int

    customer_id: int
    loan_id: int

    prediction: str

    probability_of_default: Decimal

    risk_score: Decimal

    model_version: str

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )