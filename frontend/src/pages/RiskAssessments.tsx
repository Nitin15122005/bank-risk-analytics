import { useEffect, useState } from "react";

import {
    Alert,
    Box,
    Paper,
    Snackbar,
    TextField,
    Typography,
    Chip,
} from "@mui/material";

import {
    DataGrid,
    type GridColDef,
} from "@mui/x-data-grid";

import { riskService } from "../services/risk";

import type { riskAssessment } from "../types/risk";

export default function RiskAssessments() {

    const [assessments, setAssessments] =
        useState<riskAssessment[]>([]);

    const [loading, setLoading] =
        useState(true);

    const [search, setSearch] =
        useState("");

    const [snackbar, setSnackbar] =
        useState({

            open: false,

            message: "",

            severity: "success" as
                | "success"
                | "error",

        });

    async function loadAssessments() {

        try {

            setLoading(true);

            const data =
                await riskService.getAll();

            setAssessments(data);

        } catch {

            setSnackbar({

                open: true,

                message:
                    "Failed to load assessments",

                severity: "error",

            });

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        void (async () => {

            await loadAssessments();

        })();

    }, []);


        const filteredAssessments =
        assessments.filter((assessment) => {

            const text = `
                ${assessment.id}
                ${assessment.customer_id}
                ${assessment.loan_id}
                ${assessment.prediction}
                ${assessment.model_version}
            `.toLowerCase();

            return text.includes(
                search.toLowerCase()
            );

        });

    const columns: GridColDef[] = [

        {
            field: "id",
            headerName: "ID",
            width: 90,
        },

        {
            field: "customer_id",
            headerName: "Customer",
            width: 120,
        },

        {
            field: "loan_id",
            headerName: "Loan",
            width: 120,
        },

        {
            field: "prediction",
            headerName: "Prediction",
            width: 150,

            renderCell: (params) => (

                <Chip
                    label={params.value}
                    color={
                        params.value === "Good"
                            ? "success"
                            : "error"
                    }
                    size="small"
                />

            ),

        },

        {
            field: "risk_score",
            headerName: "Risk Score",
            width: 130,

            valueFormatter: (value) =>
                `${Number(value).toFixed(2)}%`,
        },

        {
            field: "probability_of_default",
            headerName: "PD",
            width: 130,

            valueFormatter: (value) =>
                `${(
                    Number(value) * 100
                ).toFixed(2)}%`,
        },

        {
            field: "model_version",
            headerName: "Model",
            width: 120,
        },

        {
            field: "created_at",
            headerName: "Created",
            width: 220,

            valueFormatter: (value) =>
                new Date(value)
                    .toLocaleString(),
        },

    ];


        return (

        <Box>

            <Typography
                variant="h4"
                sx={{
                    fontWeight: "bold",
                    mb: 3,
                }}
            >
                Risk Assessments
            </Typography>

            <Paper
                sx={{
                    p: 2,
                    mb: 2,
                }}
            >

                <TextField
                    fullWidth
                    placeholder="Search by Assessment ID, Customer, Loan, Prediction..."
                    value={search}
                    onChange={(e) =>
                        setSearch(
                            e.target.value
                        )
                    }
                />

            </Paper>

            <Paper>

                <DataGrid
                    rows={filteredAssessments}
                    columns={columns}
                    loading={loading}
                    autoHeight
                    disableRowSelectionOnClick
                    pageSizeOptions={[
                        5,
                        10,
                        20,
                    ]}
                    initialState={{
                        pagination: {
                            paginationModel: {
                                pageSize: 10,
                                page: 0,
                            },
                        },
                    }}
                />

            </Paper>

            <Snackbar
                open={snackbar.open}
                autoHideDuration={3000}
                onClose={() =>
                    setSnackbar({
                        ...snackbar,
                        open: false,
                    })
                }
            >

                <Alert
                    severity={snackbar.severity}
                    variant="filled"
                >
                    {snackbar.message}
                </Alert>

            </Snackbar>

        </Box>

    );

}