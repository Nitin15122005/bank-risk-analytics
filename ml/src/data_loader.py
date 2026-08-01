"""
Data Loader Module.

Responsible for:
- Loading the dataset
- Removing unwanted columns
- Validating the target column
- Displaying dataset summary
"""

from pathlib import Path

import pandas as pd

from src.constants import DATASET_PATH
from src.logger import logger
from src.schema import (
    DROP_COLUMNS,
    TARGET_COLUMN,
)


class DataLoader:

    def __init__(
        self,
        dataset_path: Path = DATASET_PATH,
    ):

        self.dataset_path = dataset_path

    def load(self) -> pd.DataFrame:

        logger.info("=" * 70)
        logger.info("LOADING DATASET")
        logger.info("=" * 70)

        if not self.dataset_path.exists():

            raise FileNotFoundError(
                f"Dataset not found:\n{self.dataset_path}"
            )

        dataframe = pd.read_csv(self.dataset_path)

        logger.success("Dataset Loaded Successfully")

        logger.info(f"Rows    : {dataframe.shape[0]}")
        logger.info(f"Columns : {dataframe.shape[1]}")

        dataframe = self.remove_unused_columns(dataframe)

        self.validate_target(dataframe)

        self.dataset_summary(dataframe)

        return dataframe

    def remove_unused_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        columns = [
            column
            for column in DROP_COLUMNS
            if isinstance(column, str) and column in dataframe.columns
        ]
        if columns:

            logger.info(
                f"Removing columns : {columns}"
            )

            dataframe = dataframe.drop(
                columns=columns,
            )

        return dataframe

    def validate_target(
        self,
        dataframe: pd.DataFrame,
    ):

        if TARGET_COLUMN not in dataframe.columns:

            raise ValueError(
                f"Target column '{TARGET_COLUMN}' not found."
            )

        logger.success("Target Column Verified")

    def dataset_summary(
        self,
        dataframe: pd.DataFrame,
    ):

        logger.info("=" * 70)
        logger.info("DATASET SUMMARY")
        logger.info("=" * 70)

        logger.info(f"Shape : {dataframe.shape}")

        logger.info("Columns:")

        for column in dataframe.columns:

            logger.info(f" • {column}")

        logger.info("=" * 70)


if __name__ == "__main__":

    loader = DataLoader()

    dataframe = loader.load()

    print(dataframe.head())