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

type Props = {
    open: boolean;
    onClose: () => void;
    onSave: (
    data: Omit<customer, "id" | "customer_id">
) => void;
    customer?: customer | null;
};

const employmentTypes = [
    "Unemployed",
    "Unskilled",
    "Skilled",
    "Highly Skilled",
];

const housingOptions = [
    "own",
    "rent",
    "free",
];

const accountOptions = [
    "little",
    "moderate",
    "rich",
];

export default function CustomerDialog({
    open,
    onClose,
    onSave,
    customer,
}: Props) {

    const [form, setForm] = useState<
    Omit<customer, "id" | "customer_id">
>({
    first_name: "",
    last_name: "",
    email: "",
    phone: "",
    date_of_birth: "",
    gender: "male",
    employment_type: "Skilled",
    housing: "own",
    saving_account: "moderate",
    checking_account: "little",
    annual_income: "0",
    monthly_expenses: "0",
    employment_years: 0,
    credit_score: 700,
    branch_id: 1,
});

    useEffect(() => {

    if (!customer) return;

    queueMicrotask(() => {
        setForm(customer);
    });

}, [customer]);

    const handleChange = (
        e: React.ChangeEvent<HTMLInputElement>
    ) => {

        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });

    };

    return (

        <Dialog
            open={open}
            maxWidth="md"
            fullWidth
            onClose={onClose}
        >

            <DialogTitle>
                {customer ? "Edit Customer" : "New Customer"}
            </DialogTitle>

            <DialogContent>

                <Grid
                    container
                    spacing={2}
                    sx={{ mt: 1 }}
                >

                    {[
                        "first_name",
                        "last_name",
                        "email",
                        "phone",
                        "annual_income",
                        "monthly_expenses",
                        "employment_years",
                        "credit_score",
                    ].map((field) => (

                        <Grid size={{ xs: 12, md: 6 }} key={field}>

                            <TextField
                                fullWidth
                                label={field.replaceAll("_", " ")}
                                name={field}
                                value={form[field as keyof typeof form]}
                                onChange={handleChange}
                            />

                        </Grid>

                    ))}

                    <Grid size={{ xs: 12, md: 6 }}>

                        <TextField
                            fullWidth
                            type="date"
                            label="Date of Birth"
                            name="date_of_birth"
                            value={form.date_of_birth}
                            onChange={handleChange}
                            slotProps={{
                                inputLabel: {
                                    shrink: true,
                                },
                            }}
                        />

                    </Grid>

                    <Grid size={{ xs: 12, md: 6 }}>
                        <TextField
                            select
                            fullWidth
                            name="gender"
                            label="Gender"
                            value={form.gender}
                            onChange={handleChange}
                        >
                            <MenuItem value="male">Male</MenuItem>
                            <MenuItem value="female">Female</MenuItem>
                        </TextField>
                    </Grid>

                    <Grid size={{ xs: 12, md: 6 }}>
                        <TextField
                            select
                            fullWidth
                            name="employment_type"
                            label="Employment"
                            value={form.employment_type}
                            onChange={handleChange}
                        >
                            {employmentTypes.map((x) => (
                                <MenuItem key={x} value={x}>
                                    {x}
                                </MenuItem>
                            ))}
                        </TextField>
                    </Grid>

                    <Grid size={{ xs: 12, md: 6 }}>
                        <TextField
                            select
                            fullWidth
                            name="housing"
                            label="Housing"
                            value={form.housing}
                            onChange={handleChange}
                        >
                            {housingOptions.map((x) => (
                                <MenuItem key={x} value={x}>
                                    {x}
                                </MenuItem>
                            ))}
                        </TextField>
                    </Grid>

                    <Grid size={{ xs: 12, md: 6 }}>
                        <TextField
                            select
                            fullWidth
                            name="saving_account"
                            label="Saving"
                            value={form.saving_account}
                            onChange={handleChange}
                        >
                            {accountOptions.map((x) => (
                                <MenuItem key={x} value={x}>
                                    {x}
                                </MenuItem>
                            ))}
                        </TextField>
                    </Grid>

                    <Grid size={{ xs: 12, md: 6 }}>
                        <TextField
                            select
                            fullWidth
                            name="checking_account"
                            label="Checking"
                            value={form.checking_account}
                            onChange={handleChange}
                        >
                            {accountOptions.map((x) => (
                                <MenuItem key={x} value={x}>
                                    {x}
                                </MenuItem>
                            ))}
                        </TextField>
                    </Grid>

                </Grid>

            </DialogContent>

            <DialogActions>

                <Button onClick={onClose}>
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