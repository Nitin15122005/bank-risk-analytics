import { useEffect, useState } from "react";

import {
    Box,
    Button,
    Snackbar,
    Alert,
    TextField,
    Typography,
} from "@mui/material";

import AddIcon from "@mui/icons-material/Add";

import {
    DataGrid,
    type GridColDef,
} from "@mui/x-data-grid";

import { loanService } from "../services/loan";
import { customerService } from "../services/customer";

import type { loan } from "../types/loan";
import type { customer } from "../types/customer";

import LoanDialog from "../components/LoanDialog";

export default function Loans() {

    const [loans, setLoans] =
        useState<loan[]>([]);

    const [customers, setCustomers] =
        useState<customer[]>([]);

    const [loading, setLoading] =
        useState(true);

    const [search, setSearch] =
        useState("");

    const [dialogOpen, setDialogOpen] =
        useState(false);

    const [selected, setSelected] =
        useState<loan | null>(null);

    const [snackbar, setSnackbar] =
        useState({

            open: false,

            message: "",

            severity: "success" as
                | "success"
                | "error",

        });

    async function loadData() {

        try {

            setLoading(true);

            const [loanData, customerData] =
                await Promise.all([

                    loanService.getAll(),

                    customerService.getAll(),

                ]);

            setLoans(loanData);

            setCustomers(customerData);

        }

        catch {

            setSnackbar({

                open: true,

                message: "Failed to load data",

                severity: "error",

            });

        }

        finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        void (async () => {

            await loadData();

        })();

    }, []);

    async function handleSave(
        data: Omit<
            loan,
            | "id"
            | "loan_id"
            | "emi"
            | "status"
            | "approval_status"
            | "created_at"
        >
    ) {

        try {

            if (selected) {

                await loanService.update(
                    selected.loan_id,
                    data,
                );

                setSnackbar({

                    open: true,

                    message: "Loan Updated",

                    severity: "success",

                });

            }

            else {

                await loanService.create(
                    data,
                );

                setSnackbar({

                    open: true,

                    message: "Loan Created",

                    severity: "success",

                });

            }

            setDialogOpen(false);

            setSelected(null);

            await loadData();

        }

        catch {

            setSnackbar({

                open: true,

                message: "Operation Failed",

                severity: "error",

            });

        }

    }

        const filteredLoans = loans.filter((loan) => {

        const customer = customers.find(
            (c) => c.id === loan.customer_id,
        );

        const text = `
            ${loan.loan_id}
            ${loan.loan_type}
            ${loan.purpose}
            ${customer?.first_name ?? ""}
            ${customer?.last_name ?? ""}
        `
            .toLowerCase();

        return text.includes(
            search.toLowerCase(),
        );

    });

    const columns: GridColDef[] = [

        {
            field: "loan_id",
            headerName: "Loan ID",
            width: 130,
        },

        {
            field: "customer",
            headerName: "Customer",
            width: 220,

            valueGetter: (_value, row) => {

                const customer = customers.find(
                    (c) => c.id === row.customer_id,
                );

                return customer
                    ? `${customer.first_name} ${customer.last_name}`
                    : "Unknown";

            },
        },

        {
            field: "loan_type",
            headerName: "Loan Type",
            width: 140,
        },

        {
            field: "purpose",
            headerName: "Purpose",
            width: 170,
        },

        {
            field: "loan_amount",
            headerName: "Amount",
            width: 150,

            valueFormatter: (value) =>
                `₹${Number(value).toLocaleString()}`,
        },

        {
            field: "interest_rate",
            headerName: "Interest %",
            width: 120,
        },

        {
            field: "tenure_months",
            headerName: "Months",
            width: 100,
        },

        {
            field: "emi",
            headerName: "EMI",
            width: 140,

            valueFormatter: (value) =>
                `₹${Number(value).toLocaleString()}`,
        },

        {
            field: "status",
            headerName: "Status",
            width: 120,
        },

        {
            field: "approval_status",
            headerName: "Approval",
            width: 130,
        },

        {
            field: "actions",
            headerName: "Actions",
            width: 130,
            sortable: false,

            renderCell: (params) => (

                <Button
                    size="small"
                    variant="contained"
                    onClick={() => {

                        setSelected(params.row);

                        setDialogOpen(true);

                    }}
                >
                    Edit
                </Button>

            ),

        },

    ];

        return (

        <Box>

            <Box
                sx={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    mb: 3,
                }}
            >

                <Typography
                    variant="h4"
                    sx={{
                        fontWeight: "bold",
                    }}
                >
                    Loans
                </Typography>

                <Button
                    variant="contained"
                    startIcon={<AddIcon />}
                    onClick={() => {

                        setSelected(null);

                        setDialogOpen(true);

                    }}
                >
                    Add Loan
                </Button>

            </Box>

            <TextField
                fullWidth
                placeholder="Search by Loan ID, Customer, Loan Type..."
                value={search}
                onChange={(e) =>
                    setSearch(e.target.value)
                }
                sx={{ mb: 3 }}
            />

            <DataGrid
                rows={filteredLoans}
                columns={columns}
                loading={loading}
                autoHeight
                disableRowSelectionOnClick
                pageSizeOptions={[5, 10]}
                initialState={{
                    pagination: {
                        paginationModel: {
                            pageSize: 10,
                            page: 0,
                        },
                    },
                }}
            />

            <LoanDialog
                open={dialogOpen}
                onClose={() => {

                    setDialogOpen(false);

                    setSelected(null);

                }}
                onSave={handleSave}
                customers={customers}
                loan={selected}
            />

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