import type { ReactNode } from "react";

import {
    Avatar,
    Box,
    Card,
    CardContent,
    Typography,
} from "@mui/material";

interface Props {
    title: string;
    value: string | number;
    color: string;
    icon: ReactNode;
}

export default function DashboardCard({
    title,
    value,
    color,
    icon,
}: Props) {

    return (

        <Card
            sx={{
                borderRadius: 4,
                boxShadow: 2,
            }}
        >

            <CardContent>

                <Box
                    sx={{
                        display: "flex",
                        justifyContent: "space-between",
                        alignItems: "center",
                    }}
                >

                    <Box>

                        <Typography
                            variant="body2"
                            color="text.secondary"
                        >
                            {title}
                        </Typography>

                        <Typography
                            variant="h4"
                            sx={{
                                fontWeight: 700,
                            }}
                        >
                            {value}
                        </Typography>

                    </Box>

                    <Avatar
                        sx={{
                            bgcolor: color,
                            width: 56,
                            height: 56,
                        }}
                    >
                        {icon}
                    </Avatar>

                </Box>

            </CardContent>

        </Card>

    );

}