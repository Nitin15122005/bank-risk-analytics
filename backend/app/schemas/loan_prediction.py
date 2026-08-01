from app.schemas.loan import LoanResponse
from app.schemas.risk_assessment import RiskAssessmentResponse
from pydantic import BaseModel


class LoanPredictionResponse(BaseModel):
    loan: LoanResponse
    risk_assessment: RiskAssessmentResponse