import { useState } from "react";
import {
    Box,
    Button,
    Card,
    CardContent,
    Container,
    TextField,
    Typography,
} from "@mui/material";
import { useNavigate } from "react-router-dom";

import { authService } from "../services/auth";

export default function Login() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    async function handleLogin(e: React.FormEvent) {

        e.preventDefault();

        setLoading(true);
        setError("");

        try {

            const data = await authService.login(
                email,
                password
            );

            localStorage.setItem(
                "token",
                data.access_token
            );

            navigate("/dashboard");

        } catch {

            setError("Invalid email or password");

        }

        setLoading(false);

    }

    return (

        <Container maxWidth="sm">

            <Box
                sx={{
                    display: "flex",
                    minHeight: "100vh",
                    alignItems: "center",
                }}
            >

                <Card
                    sx={{
                        width: "100%",
                        p: 2,
                        borderRadius: 4,
                    }}
                >

                    <CardContent>

                        <Typography
                        variant="h4"
                        sx={{
                            fontWeight: 700,
                            mb: 1,
                        }}
                    >
                        Bank Risk Analytics
                    </Typography>

                        <Typography
                        sx={{
                            color: "text.secondary",
                            mb: 4,
                        }}
                    >
                        Login
                    </Typography>

                        <Box
                            component="form"
                            onSubmit={handleLogin}
                        >

                            <TextField
                                fullWidth
                                margin="normal"
                                label="Email"
                                value={email}
                                onChange={(e) =>
                                    setEmail(e.target.value)
                                }
                            />

                            <TextField
                                fullWidth
                                margin="normal"
                                label="Password"
                                type="password"
                                value={password}
                                onChange={(e) =>
                                    setPassword(e.target.value)
                                }
                            />

                            {error && (

                                <Typography
                                sx={{
                                    color: "error.main",
                                    mt: 2,
                                }}
                            >
                                {error}
                            </Typography>

                            )}

                            <Button
                                fullWidth
                                type="submit"
                                variant="contained"
                                sx={{
                                    mt: 3,
                                    py: 1.5,
                                }}
                                disabled={loading}
                            >
                                {loading
                                    ? "Signing In..."
                                    : "Login"}
                            </Button>

                        </Box>

                    </CardContent>

                </Card>

            </Box>

        </Container>

    );

}