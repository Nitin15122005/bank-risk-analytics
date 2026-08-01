import {
    Box,
    List,
    ListItemButton,
    ListItemIcon,
    ListItemText,
} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";
import PeopleIcon from "@mui/icons-material/People";
import AccountBalanceIcon from "@mui/icons-material/AccountBalance";
import AssessmentIcon from "@mui/icons-material/Assessment";

import { Link } from "react-router-dom";

const drawerWidth = 240;

export default function Sidebar() {

    return (

        <Box
            sx={{
                width: drawerWidth,
                height: "100vh",
                bgcolor: "white",
                borderRight: "1px solid #E5E7EB",
                pt: 10,
                position: "fixed",
            }}
        >

            <List>

                <ListItemButton component={Link} to="/dashboard">

                    <ListItemIcon>
                        <DashboardIcon />
                    </ListItemIcon>

                    <ListItemText primary="Dashboard" />

                </ListItemButton>

                <ListItemButton component={Link} to="/customers">

                    <ListItemIcon>
                        <PeopleIcon />
                    </ListItemIcon>

                    <ListItemText primary="Customers" />

                </ListItemButton>

                <ListItemButton component={Link} to="/loans">

                    <ListItemIcon>
                        <AccountBalanceIcon />
                    </ListItemIcon>

                    <ListItemText primary="Loans" />

                </ListItemButton>

                <ListItemButton component={Link} to="/risk-assessments">

                    <ListItemIcon>
                        <AssessmentIcon />
                    </ListItemIcon>

                    <ListItemText primary="Risk Assessments" />

                </ListItemButton>

            </List>

        </Box>

    );

}