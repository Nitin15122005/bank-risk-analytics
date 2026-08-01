"""
Dataset Validator.

Responsible for validating the dataset before training.
"""

import pandas as pd

from src.logger import logger
from src.schema import (
    RAW_CATEGORICAL_FEATURES,
    RAW_NUMERICAL_FEATURES,
    TARGET_COLUMN,
)


class DataValidator:

    def __init__(self):

        self.required_columns = (
            RAW_NUMERICAL_FEATURES +
            RAW_CATEGORICAL_FEATURES +
            [TARGET_COLUMN]
        )

    def validate(
        self,
        dataframe: pd.DataFrame,
    ):

        logger.info("=" * 70)
        logger.info("VALIDATING DATASET")
        logger.info("=" * 70)

        self.check_empty_dataframe(dataframe)

        self.check_required_columns(dataframe)

        self.check_duplicate_rows(dataframe)

        self.check_missing_values(dataframe)

        self.check_target(dataframe)

        logger.success("Dataset validation completed successfully.")

    def check_empty_dataframe(
        self,
        dataframe: pd.DataFrame,
    ):

        if dataframe.empty:

            raise ValueError(
                "Dataset is empty."
            )

        logger.success("Dataset is not empty.")

    def check_required_columns(
        self,
        dataframe: pd.DataFrame,
    ):

        missing_columns = [

            column

            for column in self.required_columns

            if column not in dataframe.columns

        ]

        if missing_columns:

            raise ValueError(
                f"Missing Columns : {missing_columns}"
            )

        logger.success("All required columns found.")

    def check_duplicate_rows(
        self,
        dataframe: pd.DataFrame,
    ):

        duplicates = dataframe.duplicated().sum()

        logger.info(
            f"Duplicate Rows : {duplicates}"
        )

    def check_missing_values(
        self,
        dataframe: pd.DataFrame,
    ):

        missing = dataframe.isnull().sum()

        missing = missing[missing > 0]

        if len(missing) == 0:

            logger.success("No missing values found.")

            return

        logger.warning("Missing Values Found")

        for column, value in missing.items():

            logger.warning(
                f"{column:<25} : {value}"
            )

    def check_target(
        self,
        dataframe: pd.DataFrame,
    ):

        logger.info("Target Distribution")

        logger.info(
            dataframe[TARGET_COLUMN].value_counts()
        )

        logger.success("Target column validated.")