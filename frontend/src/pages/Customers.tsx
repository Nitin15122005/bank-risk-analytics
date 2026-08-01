import { useEffect, useState } from "react";

import {
    Alert,
    Box,
    Button,
    Snackbar,
    TextField,
    Typography,
} from "@mui/material";

import AddIcon from "@mui/icons-material/Add";

import {
    DataGrid,
    type GridColDef,
    type GridRenderCellParams,
} from "@mui/x-data-grid";

import CustomerDialog from "../components/CustomerDialog";
import DeleteCustomerDialog from "../components/DeleteCustomerDialog";

import { customerService } from "../services/customer";

import type { customer } from "../types/customer";

export default function Customers() {

    const [customers, setCustomers] = useState<customer[]>([]);

    const [loading, setLoading] = useState(false);

    const [search, setSearch] = useState("");

    const [dialogOpen, setDialogOpen] = useState(false);

    const [deleteOpen, setDeleteOpen] = useState(false);

    const [selected, setSelected] =
        useState<customer | null>(null);

    const [snackbar, setSnackbar] = useState({

        open: false,

        message: "",

        severity: "success" as
            | "success"
            | "error",

    });

    async function loadCustomers() {

        try {

            setLoading(true);

            const data =
                await customerService.getAll();

            setCustomers(data);

        }

        catch {

            setSnackbar({

                open: true,

                message:
                    "Unable to load customers",

                severity: "error",

            });

        }

        finally {

            setLoading(false);

        }

    }

    useEffect(() => {

    void (async () => {

        await loadCustomers();

    })();

}, []);

    async function handleSave(

        data: Omit<
            customer,
            "id" | "customer_id"
        >

    ) {

        try {

            if (selected) {

                await customerService.update(
                    selected.customer_id,
                    data
                );

                setSnackbar({

                    open: true,

                    message:
                        "Customer updated successfully",

                    severity: "success",

                });

            }

            else {

                await customerService.create(
                    data
                );

                setSnackbar({

                    open: true,

                    message:
                        "Customer added successfully",

                    severity: "success",

                });

            }

            setDialogOpen(false);

            setSelected(null);

            await loadCustomers();

        }

        catch {

            setSnackbar({

                open: true,

                message:
                    "Operation failed",

                severity: "error",

            });

        }

    }

    async function handleDelete() {

        if (!selected) return;

        try {

            await customerService.delete(
                selected.customer_id
            );

            setDeleteOpen(false);

            setSelected(null);

            await loadCustomers();

            setSnackbar({

                open: true,

                message:
                    "Customer deleted",

                severity: "success",

            });

        }

        catch {

            setSnackbar({

                open: true,

                message:
                    "Delete failed",

                severity: "error",

            });

        }

    }

    const filteredCustomers =
        customers.filter((c) => {

            const text =

                `${c.customer_id}
${c.first_name}
${c.last_name}
${c.email}
${c.phone}`

                    .toLowerCase();

            return text.includes(
                search.toLowerCase()
            );

        });

    const columns: GridColDef[] = [

        {

            field: "customer_id",

            headerName: "Customer ID",

            width: 140,

        },

        {

            field: "first_name",

            headerName: "First Name",

            flex: 1,

        },

        {

            field: "last_name",

            headerName: "Last Name",

            flex: 1,

        },

        {

            field: "email",

            headerName: "Email",

            flex: 1.5,

        },

        {

            field: "phone",

            headerName: "Phone",

            width: 150,

        },

        {

            field: "credit_score",

            headerName: "Credit Score",

            width: 140,

        },

        {

            field: "employment_type",

            headerName: "Employment",

            width: 170,

        },

        {

            field: "actions",

            headerName: "Actions",

            width: 190,

            sortable: false,

            renderCell: (

                params: GridRenderCellParams

            ) => (

                <Box
                    sx={{
                        display: "flex",
                        gap: 1,
                        mt: 0.5,
                    }}
                >

                    <Button

                        size="small"

                        variant="contained"

                        onClick={() => {

                            setSelected(
                                params.row as customer
                            );

                            setDialogOpen(true);

                        }}

                    >

                        Edit

                    </Button>

                    <Button

                        size="small"

                        color="error"

                        variant="contained"

                        onClick={() => {

                            setSelected(
                                params.row as customer
                            );

                            setDeleteOpen(true);

                        }}

                    >

                        Delete

                    </Button>

                </Box>

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
                        fontWeight: 700,
                    }}
                >
                    Customers
                </Typography>

                <Button
                    variant="contained"
                    startIcon={<AddIcon />}
                    onClick={() => {

                        setSelected(null);

                        setDialogOpen(true);

                    }}
                >
                    Add Customer
                </Button>

            </Box>

            <TextField
                fullWidth
                placeholder="Search by Customer ID, Name, Email or Phone..."
                value={search}
                onChange={(e) =>
                    setSearch(e.target.value)
                }
                sx={{
                    mb: 3,
                }}
            />

            <Box
                sx={{
                    height: 650,
                    bgcolor: "white",
                    borderRadius: 3,
                    overflow: "hidden",
                }}
            >

                <DataGrid

                    rows={filteredCustomers}

                    columns={columns}

                    loading={loading}

                    getRowId={(row) => row.id}

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

                    disableRowSelectionOnClick

                    sx={{
                        border: 0,
                    }}

                />

            </Box>

            <CustomerDialog

                open={dialogOpen}

                customer={selected}

                onClose={() => {

                    setDialogOpen(false);

                    setSelected(null);

                }}

                onSave={handleSave}

            />

            <DeleteCustomerDialog

                open={deleteOpen}

                onClose={() => {

                    setDeleteOpen(false);

                    setSelected(null);

                }}

                onDelete={handleDelete}

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

                anchorOrigin={{
                    vertical: "top",
                    horizontal: "right",
                }}

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