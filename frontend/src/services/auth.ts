import api from "./api";

export const authService = {
    async login(username: string, password: string) {

        const form = new URLSearchParams();

        form.append("grant_type", "password");
        form.append("username", username);
        form.append("password", password);

        const response = await api.post(
            "/api/v1/auth/login",
            form,
            {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            }
        );

        return response.data;
    },
};