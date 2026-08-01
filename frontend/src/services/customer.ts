import api from "./api";

import type { customer } from "../types/customer";

export const customerService = {

    async getAll(): Promise<customer[]> {

        const response = await api.get("/api/v1/customers/");
        return response.data;

    },

    async getById(id: number): Promise<customer> {

        const response = await api.get(`/api/v1/customers/${id}`);
        return response.data;

    },

    async create(
        data: Omit<customer, "id" | "customer_id">
    ): Promise<customer> {

        const response = await api.post(
            "/api/v1/customers/",
            data
        );

        return response.data;

    },

    async update(
        id: number,
        data: Partial<customer>
    ): Promise<customer> {

        const response = await api.put(
            `/api/v1/customers/${id}`,
            data
        );

        return response.data;

    },

    async delete(id: number): Promise<void> {

        await api.delete(`/api/v1/customers/${id}`);

    },

};