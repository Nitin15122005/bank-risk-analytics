import { useEffect, useState } from "react";
import { Grid, Typography } from "@mui/material";

import DashboardCard from "../components/DashboardCard";
import RecentLoansTable from "../components/RecentLoansTable";
import RiskChart from "../components/RiskChart";

import GroupsIcon from "@mui/icons-material/Groups";
import AccountBalanceIcon from "@mui/icons-material/AccountBalance";
import WarningIcon from "@mui/icons-material/Warning";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";

import { customerService } from "../services/customer";
import { loanService } from "../services/loan";
import { riskService } from "../services/risk";

import type { customer } from "../types/customer";
import type { loan } from "../types/loan";
import type { riskAssessment } from "../types/risk";

export default function Dashboard() {

    const [customers, setcustomers] = useState<customer[]>([]);
    const [loans, setLoans] = useState<loan[]>([]);
    const [risks, setRisks] = useState<riskAssessment[]>([]);

    useEffect(() => {

        async function loadData() {

            try {

                const [
                    customerData,
                    loanData,
                    riskData,
                ] = await Promise.all([
                    customerService.getAll(),
                    loanService.getAll(),
                    riskService.getAll(),
                ]);

                setcustomers(customerData);
                setLoans(loanData);
                setRisks(riskData);

            } catch (err) {

                console.error(err);

            }

        }

        loadData();

    }, []);

    const highRisk =
        risks.filter(
            (r) => Number(r.risk_score) >= 70
        ).length;

    const avgRisk =
        risks.length === 0
            ? 0
            : (
                  risks.reduce(
                      (sum, r) => sum + Number(r.risk_score),
                      0
                  ) / risks.length
              ).toFixed(1);

    return (

        <>
            <Typography
                variant="h4"
                sx={{
                    fontWeight: 700,
                    mb: 4,
                }}
            >
                Dashboard
            </Typography>

            <Grid container spacing={3}>

                <Grid size={{ xs: 12, md: 3 }}>
                    <DashboardCard
                        title="customers"
                        value={customers.length}
                        color="#2563EB"
                        icon={<GroupsIcon />}
                    />
                </Grid>

                <Grid size={{ xs: 12, md: 3 }}>
                    <DashboardCard
                        title="Loans"
                        value={loans.length}
                        color="#2E7D32"
                        icon={<AccountBalanceIcon />}
                    />
                </Grid>

                <Grid size={{ xs: 12, md: 3 }}>
                    <DashboardCard
                        title="High Risk"
                        value={highRisk}
                        color="#D32F2F"
                        icon={<WarningIcon />}
                    />
                </Grid>

                <Grid size={{ xs: 12, md: 3 }}>
                    <DashboardCard
                        title="Average Risk"
                        value={`${avgRisk}%`}
                        color="#F57C00"
                        icon={<TrendingUpIcon />}
                    />
                </Grid>

                <Grid size={{ xs: 12, md: 8 }}>
                    <RecentLoansTable loans={loans} />
                </Grid>

                <Grid size={{ xs: 12, md: 4 }}>
                    <RiskChart risks={risks} />
                </Grid>

            </Grid>

        </>

    );

}