import api from "./api";

import type { loan } from "../types/loan";
import type { riskAssessment } from "../types/risk";

export interface LoanPredictionResponse {

    loan: loan;

    risk_assessment: riskAssessment;

}



export const loanService = {

    async getAll(): Promise<loan[]> {

        const response = await api.get("/loans/");

        return response.data;

    },

    async getById(
        loanId: string
    ): Promise<loan> {

        const response = await api.get(
            `/loans/${loanId}`
        );

        return response.data;

    },

    async create(
        data: {
            customer_id: number;
            loan_type: string;
            purpose: string;
            loan_amount: number;
            interest_rate: number;
            tenure_months: number;
        }
    ): Promise<LoanPredictionResponse> {

        const response =
            await api.post(
                "/loans/",
                data
            );

        return response.data;

    },

    async update(

        loanId: string,

        data: {

            status?: string;

            approval_status?: string;

            purpose?: string;

        }

    ) {

        const response =
            await api.put(
                `/loans/${loanId}`,
                data
            );

        return response.data;

    },

    async delete(
        loanId: string
    ) {

        return api.delete(
            `/loans/${loanId}`
        );

    },

};