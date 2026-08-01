import {
    Card,
    CardContent,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow,
    Typography,
} from "@mui/material";

import type { loan } from "../types/loan";

interface Props {
    loans: loan[];
}

export default function RecentloansTable({
    loans,
}: Props) {

    return (

        <Card
            sx={{
                borderRadius: 4,
            }}
        >

            <CardContent>

                <Typography
                    variant="h6"
                    sx={{ mb: 2 }}
                >
                    Recent loans
                </Typography>

                <Table>

                    <TableHead>

                        <TableRow>

                            <TableCell>loan ID</TableCell>
                            <TableCell>Customer</TableCell>
                            <TableCell>Amount</TableCell>
                            <TableCell>Status</TableCell>

                        </TableRow>

                    </TableHead>

                    <TableBody>

                        {loans.map((loan) => (

                            <TableRow key={loan.id}>

                                <TableCell>{loan.loan_id}</TableCell>

                                <TableCell>
                                    {loan.customer_id}
                                </TableCell>

                                <TableCell>
                                    ₹{Number(loan.loan_amount).toLocaleString()}
                                </TableCell>

                                <TableCell>
                                    {loan.status}
                                </TableCell>

                            </TableRow>

                        ))}

                    </TableBody>

                </Table>

            </CardContent>

        </Card>

    );

}