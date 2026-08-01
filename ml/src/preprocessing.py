"""
Preprocessing module.

Creates the preprocessing pipeline used during both
training and inference.
"""

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler,
)

from src.logger import logger
from src.feature_engineering import FeatureEngineer
from src.schema import (
    NUMERICAL_FEATURES,
    CATEGORICAL_FEATURES,
)


class DataPreprocessor:

    def __init__(self):
        self.preprocessor = None

    def numeric_pipeline(self):

        logger.info("Building numeric preprocessing pipeline...")

        return Pipeline(
            steps=[
                (
                    "imputer",
                    SimpleImputer(strategy="median"),
                ),
                (
                    "scaler",
                    StandardScaler(),
                ),
            ]
        )

    def categorical_pipeline(self):

        logger.info("Building categorical preprocessing pipeline...")

        return Pipeline(
            steps=[
                (
                    "imputer",
                    SimpleImputer(strategy="most_frequent"),
                ),
                (
                    "encoder",
                    OneHotEncoder(
                        handle_unknown="ignore",
                        sparse_output=False,
                    ),
                ),
            ]
        )

    def build(self):

        logger.info("Creating preprocessing pipeline...")

        preprocessor = ColumnTransformer(
            transformers=[
                (
                    "num",
                    self.numeric_pipeline(),
                    NUMERICAL_FEATURES,
                ),
                (
                    "cat",
                    self.categorical_pipeline(),
                    CATEGORICAL_FEATURES,
                ),
            ],
            remainder="drop",
        )

        pipeline = Pipeline(
            steps=[
                (
                    "feature_engineering",
                    FeatureEngineer(),
                ),
                (
                    "preprocessing",
                    preprocessor,
                ),
            ]
        )

        logger.success("Preprocessing pipeline created.")

        return pipeline