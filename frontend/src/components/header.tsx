import { useNavigate } from "react-router-dom";

import {
    AppBar,
    Avatar,
    Box,
    IconButton,
    Menu,
    MenuItem,
    Toolbar,
    Typography,
} from "@mui/material";

import { useState } from "react";

export default function Header() {

    const navigate = useNavigate();

    const [anchorEl, setAnchorEl] =
        useState<null | HTMLElement>(null);

    function openMenu(
        event: React.MouseEvent<HTMLElement>
    ) {

        setAnchorEl(event.currentTarget);

    }

    function closeMenu() {

        setAnchorEl(null);

    }

    function logout() {

        localStorage.removeItem("token");

        navigate("/login");

    }

    return (

        <AppBar
            position="fixed"
            elevation={1}
            color="inherit"
        >

            <Toolbar>

                <Box sx={{ flexGrow: 1 }}>

                    <Typography
                        variant="h6"
                        sx={{
                            color: "primary.main",
                            fontWeight: 700,
                        }}
                    >
                        Bank Risk Analytics
                    </Typography>

                    <Typography
                        sx={{
                            color: "text.secondary",
                            fontSize: 14,
                        }}
                    >
                        AI-Powered Credit Risk Assessment Platform
                    </Typography>

                </Box>

                <IconButton onClick={openMenu}>

                    <Avatar
                        sx={{
                            bgcolor: "primary.main",
                        }}
                    >
                        N
                    </Avatar>

                </IconButton>

                <Menu
                    anchorEl={anchorEl}
                    open={Boolean(anchorEl)}
                    onClose={closeMenu}
                >

                    <MenuItem disabled>

                        Nitin Sharma

                    </MenuItem>

                    <MenuItem
                        onClick={() => {

                            navigate("/dashboard");

                            closeMenu();

                        }}
                    >
                        Dashboard
                    </MenuItem>

                    <MenuItem
                        onClick={logout}
                    >
                        Logout
                    </MenuItem>

                </Menu>

            </Toolbar>

        </AppBar>

    );

}