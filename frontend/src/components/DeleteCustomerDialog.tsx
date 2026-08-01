import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button,
} from "@mui/material";

type Props = {
    open: boolean;
    onClose: () => void;
    onDelete: () => void;
};

export default function DeleteCustomerDialog({
    open,
    onClose,
    onDelete,
}: Props) {

    return (

        <Dialog open={open} onClose={onClose}>

            <DialogTitle>
                Delete Customer
            </DialogTitle>

            <DialogContent>
                Are you sure you want to delete this customer?
            </DialogContent>

            <DialogActions>

                <Button onClick={onClose}>
                    Cancel
                </Button>

                <Button
                    color="error"
                    variant="contained"
                    onClick={onDelete}
                >
                    Delete
                </Button>

            </DialogActions>

        </Dialog>

    );

}