"""
Project-wide constants.

Nothing should be hardcoded anywhere else in the project.
"""

from pathlib import Path

# -----------------------------------------------------------------------------
# Project Paths
# -----------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
METRICS_DIR = REPORTS_DIR / "metrics"

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

TRAINED_MODELS_DIR = PROJECT_ROOT / "trained_models"
LATEST_MODEL_DIR = TRAINED_MODELS_DIR / "latest"
VERSIONED_MODELS_DIR = TRAINED_MODELS_DIR / "versions"

LOG_DIR = PROJECT_ROOT / "logs"

# -----------------------------------------------------------------------------
# Dataset
# -----------------------------------------------------------------------------

DATASET_NAME = "german_credit_data.csv"

DATASET_PATH = RAW_DATA_DIR / DATASET_NAME

# -----------------------------------------------------------------------------
# Output Files
# -----------------------------------------------------------------------------

MODEL_FILE = LATEST_MODEL_DIR / "model.pkl"

FEATURE_COLUMNS_FILE = LATEST_MODEL_DIR / "feature_columns.json"

METADATA_FILE = LATEST_MODEL_DIR / "metadata.json"

METRICS_FILE = LATEST_MODEL_DIR / "metrics.json"