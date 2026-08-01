import { useEffect, useState } from "react";

import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button,
    Grid,
    TextField,
    MenuItem,
} from "@mui/material";

import type { customer } from "../types/customer";
import type { loan } from "../types/loan";

type Props = {
    open: boolean;
    onClose: () => void;

    onSave: (
        data: Omit<
            loan,
            | "id"
            | "loan_id"
            | "emi"
            | "status"
            | "approval_status"
            | "created_at"
        >
    ) => void;

    customers: customer[];

    loan?: loan | null;
};

const loanTypes = [
    "Personal",
    "Home",
    "Vehicle",
    "Education",
    "Business",
    "Gold",
    "Other",
];

const purposes = [
    "car",
    "radio/TV",
    "education",
    "business",
    "furniture/equipment",
    "domestic appliances",
    "repairs",
    "vacation/others",
];

export default function LoanDialog({
    open,
    onClose,
    onSave,
    customers,
    loan,
}: Props) {

    const [form, setForm] = useState<
        Omit<
            loan,
            | "id"
            | "loan_id"
            | "emi"
            | "status"
            | "approval_status"
            | "created_at"
        >
    >({
        customer_id: 0,
        loan_type: "Personal",
        purpose: "car",
        loan_amount: 100000,
        interest_rate: 10,
        tenure_months: 12,
    });

    useEffect(() => {

        if (!loan) return;

        queueMicrotask(() => {

            setForm({
                customer_id: loan.customer_id,
                loan_type: loan.loan_type,
                purpose: loan.purpose,
                loan_amount: Number(loan.loan_amount),
                interest_rate: Number(loan.interest_rate),
                tenure_months: loan.tenure_months,
            });

        });

    }, [loan]);

    const handleChange = (
        e: React.ChangeEvent<HTMLInputElement>
    ) => {

        const { name, value } = e.target;

        setForm((prev) => ({

            ...prev,

            [name]:
                name === "customer_id" ||
                name === "loan_amount" ||
                name === "interest_rate" ||
                name === "tenure_months"
                    ? Number(value)
                    : value,

        }));

    };


    return (

            <Dialog
                open={open}
                onClose={onClose}
                fullWidth
                maxWidth="md"
            >

                <DialogTitle>

                    {loan ? "Edit Loan" : "New Loan"}

                </DialogTitle>

                <DialogContent>

                    <Grid
                        container
                        spacing={2}
                        sx={{ mt: 1 }}
                    >

                        <Grid size={{ xs: 12, md: 6 }}>

                            <TextField
                                select
                                fullWidth
                                name="customer_id"
                                label="Customer"
                                value={form.customer_id}
                                onChange={handleChange}
                            >

                                {customers.map((customer) => (

                                    <MenuItem
                                        key={customer.id}
                                        value={customer.id}
                                    >

                                        {customer.customer_id}
                                        {" - "}
                                        {customer.first_name}
                                        {" "}
                                        {customer.last_name}

                                    </MenuItem>

                                ))}

                            </TextField>

                        </Grid>

                        <Grid size={{ xs: 12, md: 6 }}>

                            <TextField
                                select
                                fullWidth
                                name="loan_type"
                                label="Loan Type"
                                value={form.loan_type}
                                onChange={handleChange}
                            >

                                {loanTypes.map((type) => (

                                    <MenuItem
                                        key={type}
                                        value={type}
                                    >

                                        {type}

                                    </MenuItem>

                                ))}

                            </TextField>

                        </Grid>

                        <Grid size={{ xs: 12, md: 6 }}>

                            <TextField
                                select
                                fullWidth
                                name="purpose"
                                label="Purpose"
                                value={form.purpose}
                                onChange={handleChange}
                            >

                                {purposes.map((purpose) => (

                                    <MenuItem
                                        key={purpose}
                                        value={purpose}
                                    >

                                        {purpose}

                                    </MenuItem>

                                ))}

                            </TextField>

                        </Grid>

                        <Grid size={{ xs: 12, md: 6 }}>

                            <TextField
                                fullWidth
                                type="number"
                                label="Loan Amount"
                                name="loan_amount"
                                value={form.loan_amount}
                                onChange={handleChange}
                            />

                        </Grid>

                        <Grid size={{ xs: 12, md: 6 }}>

                            <TextField
                                fullWidth
                                type="number"
                                label="Interest Rate (%)"
                                name="interest_rate"
                                value={form.interest_rate}
                                onChange={handleChange}
                            />

                        </Grid>

                        <Grid size={{ xs: 12, md: 6 }}>

                            <TextField
                                fullWidth
                                type="number"
                                label="Tenure (Months)"
                                name="tenure_months"
                                value={form.tenure_months}
                                onChange={handleChange}
                            />

                        </Grid>


                                        </Grid>

            </DialogContent>

            <DialogActions>

                <Button
                    onClick={onClose}
                >
                    Cancel
                </Button>

                <Button
                    variant="contained"
                    onClick={() => onSave(form)}
                >
                    Save
                </Button>

            </DialogActions>

        </Dialog>

    );

}