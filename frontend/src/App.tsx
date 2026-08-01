import {
    BrowserRouter,
    Routes,
    Route,
    Navigate,
} from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Customers from "./pages/Customers";
import Loans from "./pages/Loans";
import RiskAssessments from "./pages/RiskAssessments";

import MainLayout from "./layouts/MainLayout";
import ProtectedRoute from "./components/ProtectedRoute";

function App() {
    return (
        <BrowserRouter>
            <Routes>

                <Route
                    path="/"
                    element={<Navigate to="/login" replace />}
                />

                <Route
                    path="/login"
                    element={<Login />}
                />

                <Route
                    element={
                        <ProtectedRoute>
                            <MainLayout />
                        </ProtectedRoute>
                    }
                >

                    <Route
                        path="/dashboard"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/customers"
                        element={<Customers />}
                    />

                    <Route
                        path="/loans"
                        element={<Loans />}
                    />

                    <Route
                        path="/risk-assessments"
                        element={<RiskAssessments />}
                    />

                </Route>

            </Routes>
        </BrowserRouter>
    );
}

export default App;