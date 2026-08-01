"""
Custom Feature Engineering Transformer.

Creates additional features while remaining fully compatible
with sklearn Pipelines.
"""

import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin

from src.logger import logger


class FeatureEngineer(BaseEstimator, TransformerMixin):

    def __init__(self):

        self.credit_threshold = None
        self.high_credit_threshold = None

    def fit(self, X, y=None):

        logger.info("Learning feature engineering parameters...")

        self.credit_threshold = X["Credit amount"].median()

        self.high_credit_threshold = (
            X["Credit amount"].quantile(0.90)
        )

        logger.success("Feature engineering parameters learned.")

        return self

    def transform(self, X):

        logger.info("Applying feature engineering...")

        X = X.copy()

        # ==========================================================
        # Safe Duration
        # ==========================================================

        duration = X["Duration"].clip(lower=1)

        # ==========================================================
        # Age Group
        # ==========================================================

        X["Age Group"] = pd.cut(
            X["Age"],
            bins=[0, 25, 35, 50, float("inf")],
            labels=[
                "Young",
                "Adult",
                "Middle",
                "Senior",
            ],
        )

        # ==========================================================
        # Monthly Credit
        # ==========================================================

        X["Monthly Credit"] = (
            X["Credit amount"] / duration
        )

        # ==========================================================
        # Log Credit Amount
        # ==========================================================

        X["Log Credit Amount"] = np.log1p(
            X["Credit amount"]
        )

        # ==========================================================
        # Credit Per Age
        # ==========================================================

        X["Credit Per Age"] = (
            X["Credit amount"] /
            X["Age"].clip(lower=1)
        )

        # ==========================================================
        # Payment Burden
        # ==========================================================

        X["Payment Burden"] = (
            X["Monthly Credit"] /
            X["Age"].clip(lower=1)
        )

        # ==========================================================
        # Long Term Loan
        # ==========================================================

        X["Long Term Loan"] = (
            X["Duration"] > 24
        ).astype(int)

        # ==========================================================
        # High Credit
        # ==========================================================

        X["High Credit"] = (
            X["Credit amount"] >
            self.credit_threshold
        ).astype(int)

        # ==========================================================
        # Very High Credit
        # ==========================================================

        X["Very High Credit"] = (
            X["Credit amount"] >
            self.high_credit_threshold
        ).astype(int)

        # ==========================================================
        # Young Borrower
        # ==========================================================

        X["Young Borrower"] = (
            X["Age"] < 30
        ).astype(int)

        # ==========================================================
        # Senior Borrower
        # ==========================================================

        X["Senior Borrower"] = (
            X["Age"] >= 60
        ).astype(int)

        # ==========================================================
        # Loan Duration Category
        # ==========================================================

        X["Loan Duration Category"] = pd.cut(
            X["Duration"],
            bins=[0, 12, 24, 48, float("inf")],
            labels=[
                "Short",
                "Medium",
                "Long",
                "Very Long",
            ],
        )

        # ==========================================================
        # Savings Available
        # ==========================================================

        X["Savings Available"] = (
            X["Saving accounts"]
            .fillna("Unknown")
            .isin(
                [
                    "little",
                    "moderate",
                    "rich",
                ]
            )
        ).astype(int)

        # ==========================================================
        # Checking Available
        # ==========================================================

        X["Checking Available"] = (
            X["Checking account"]
            .fillna("Unknown")
            .isin(
                [
                    "little",
                    "moderate",
                    "rich",
                ]
            )
        ).astype(int)

        # ==========================================================
        # Financial Stability
        # ==========================================================

        X["Financial Stability"] = (
            X["Savings Available"] +
            X["Checking Available"]
        )

        logger.info(
            f"Dataset shape after feature engineering: {X.shape}"
        )

        logger.success(
            "Feature engineering completed."
        )

        return X