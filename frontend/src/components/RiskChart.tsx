import {
    Card,
    CardContent,
    Typography,
} from "@mui/material";

import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    ResponsiveContainer,
} from "recharts";

import type { riskAssessment } from "../types/risk";

interface Props {
    risks: riskAssessment[];
}

export default function RiskChart({
    risks,
}: Props) {

    const data = [

        {
            name: "Good",
            value: risks.filter(
                r => r.prediction === "Good"
            ).length,
        },

        {
            name: "Bad",
            value: risks.filter(
                r => r.prediction === "Bad"
            ).length,
        },

    ];

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
                    Risk Distribution
                </Typography>

                <ResponsiveContainer
                    width="100%"
                    height={300}
                >

                    <PieChart>

                        <Pie
                            data={data}
                            dataKey="value"
                            outerRadius={90}
                        >

                            <Cell fill="#2E7D32" />
                            <Cell fill="#D32F2F" />

                        </Pie>

                        <Tooltip />

                    </PieChart>

                </ResponsiveContainer>

            </CardContent>

        </Card>

    );

}