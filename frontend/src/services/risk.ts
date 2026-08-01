import api from "./api";

import type { riskAssessment } from "../types/risk";

export const riskService = {

    async getAll(): Promise<riskAssessment[]> {

        const response = await api.get(
            "/risk-assessments/"
        );

        return response.data;

    },

};