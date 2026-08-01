"""
Artifact Manager.

Responsible for saving:
- Trained Pipeline
- Metrics
- Metadata
- Feature Columns
"""

import json

import joblib
import pandas as pd

from src.constants import (
    FEATURE_COLUMNS_FILE,
    LATEST_MODEL_DIR,
    METADATA_FILE,
    METRICS_FILE,
    MODEL_FILE,
)
from src.logger import logger
from src.schema import (
    CATEGORICAL_FEATURES,
    NUMERICAL_FEATURES,
)


class ArtifactManager:

    def __init__(self):

        LATEST_MODEL_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(
        self,
        pipeline,
        metrics,
        model_name,
    ):

        logger.info("=" * 70)
        logger.info("SAVING ARTIFACTS")
        logger.info("=" * 70)

        # ---------------------------------------------------------
        # Save Pipeline
        # ---------------------------------------------------------

        joblib.dump(
            pipeline,
            MODEL_FILE,
        )

        logger.success(f"Saved Model : {MODEL_FILE}")

        # ---------------------------------------------------------
        # Save Metrics
        # ---------------------------------------------------------

        if isinstance(metrics, pd.DataFrame):

            metrics.to_csv(
                METRICS_FILE.with_suffix(".csv"),
                index=False,
            )

        else:

            with open(
                METRICS_FILE,
                "w",
            ) as file:

                json.dump(
                    metrics,
                    file,
                    indent=4,
                )

        logger.success("Metrics Saved")

        # ---------------------------------------------------------
        # Save Metadata
        # ---------------------------------------------------------

        metadata = {

            "best_model": model_name,

            "numerical_features": NUMERICAL_FEATURES,

            "categorical_features": CATEGORICAL_FEATURES,

            "total_features": len(
                NUMERICAL_FEATURES +
                CATEGORICAL_FEATURES
            )

        }

        with open(
            METADATA_FILE,
            "w",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
            )

        logger.success("Metadata Saved")

        # ---------------------------------------------------------
        # Save Feature Columns
        # ---------------------------------------------------------

        feature_columns = {

            "numerical": NUMERICAL_FEATURES,

            "categorical": CATEGORICAL_FEATURES,

        }

        with open(
            FEATURE_COLUMNS_FILE,
            "w",
        ) as file:

            json.dump(
                feature_columns,
                file,
                indent=4,
            )

        logger.success("Feature Columns Saved")

        logger.success("=" * 70)
        logger.success("ALL ARTIFACTS SAVED")
        logger.success("=" * 70)