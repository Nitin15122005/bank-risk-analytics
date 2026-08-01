from pydantic import BaseModel

from app.schemas.loan import LoanResponse
from app.schemas.risk_assessment import RiskAssessmentResponse


class LoanPredictionResponse(BaseModel):
    loan: LoanResponse
    risk_assessment: RiskAssessmentResponse