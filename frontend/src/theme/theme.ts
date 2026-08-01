import { createTheme } from "@mui/material/styles";

const theme = createTheme({

    palette: {

        mode: "light",

        primary: {
            main: "#0F62FE",
        },

        secondary: {
            main: "#16A34A",
        },

        background: {
            default: "#F8FAFC",
            paper: "#FFFFFF",
        },

        success: {
            main: "#16A34A",
        },

        warning: {
            main: "#F59E0B",
        },

        error: {
            main: "#DC2626",
        },

    },

    shape: {
        borderRadius: 14,
    },

    typography: {

        fontFamily:
            "'Inter','Segoe UI','Roboto',sans-serif",

        h4: {
            fontWeight: 700,
        },

        h5: {
            fontWeight: 700,
        },

        h6: {
            fontWeight: 600,
        },

        button: {
            textTransform: "none",
        },

    },

    components: {

        MuiCard: {

            styleOverrides: {

                root: {

                    boxShadow:
                        "0 2px 10px rgba(15,23,42,0.05)",

                    border:
                        "1px solid #E5E7EB",

                },

            },

        },

    },

});

export default theme;