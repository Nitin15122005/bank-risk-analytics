export interface riskAssessment {

    id: number;

    customer_id: number;

    loan_id: number;

    prediction: string;

    probability_of_default: string;

    risk_score: string;

    model_version: string;

    created_at: string;

}