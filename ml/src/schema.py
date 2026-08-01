"""
Dataset schema.

Single source of truth for dataset features.
"""

from src.config import config

# =============================================================================
# Dataset
# =============================================================================

TARGET_COLUMN = config.dataset["target"]

# =============================================================================
# Drop Columns
# =============================================================================

_drop_columns = config.features.get("drop_columns", [])

if isinstance(_drop_columns, dict):
    DROP_COLUMNS = list(_drop_columns.keys())
elif isinstance(_drop_columns, list):
    DROP_COLUMNS = _drop_columns
else:
    DROP_COLUMNS = []

# =============================================================================
# Raw Features
# =============================================================================

RAW_NUMERICAL_FEATURES = config.features["numerical"]

RAW_CATEGORICAL_FEATURES = config.features["categorical"]

# =============================================================================
# Engineered Numerical Features
# =============================================================================

ENGINEERED_NUMERICAL_FEATURES = [

    "Monthly Credit",

    "Log Credit Amount",

    "Credit Per Age",

    "Payment Burden",

    "Long Term Loan",

    "High Credit",

    "Very High Credit",

    "Young Borrower",

    "Senior Borrower",

    "Savings Available",

    "Checking Available",

    "Financial Stability",

]

# =============================================================================
# Engineered Categorical Features
# =============================================================================

ENGINEERED_CATEGORICAL_FEATURES = [

    "Age Group",

    "Loan Duration Category",

]

# =============================================================================
# Final Feature Lists
# =============================================================================

NUMERICAL_FEATURES = (
    RAW_NUMERICAL_FEATURES
    + ENGINEERED_NUMERICAL_FEATURES
)

CATEGORICAL_FEATURES = (
    RAW_CATEGORICAL_FEATURES
    + ENGINEERED_CATEGORICAL_FEATURES
)

ALL_FEATURES = (
    NUMERICAL_FEATURES
    + CATEGORICAL_FEATURES
)
