export interface loan {
    id: number;

    loan_id: string;

    customer_id: number;

    loan_type: string;

    purpose: string;

    loan_amount: number;

    interest_rate: number;

    tenure_months: number;

    emi: number;

    status: string;

    approval_status: string;

    created_at: string;
}