import { Box } from "@mui/material";
import { Outlet } from "react-router-dom";

import Header from "../components/header";
import Sidebar from "../components/Sidebar";

export default function MainLayout() {
    return (
        <>
            <Header />
            <Sidebar />

            <Box
                sx={{
                    ml: "240px",
                    mt: "64px",
                    p: 4,
                    minHeight: "100vh",
                    bgcolor: "#F4F7FA",
                }}
            >
                <Outlet />
            </Box>
        </>
    );
}