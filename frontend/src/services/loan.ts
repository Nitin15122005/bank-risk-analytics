import api from "./api";

import type { loan } from "../types/loan";

export const loanService = {

    async getAll(): Promise<loan[]> {

        const response = await api.get("/loans/");

        return response.data;

    },

    async create(data: Partial<loan>): Promise<loan> {

        const response = await api.post(
            "/loans/",
            data
        );

        return response.data;

    },

};