"""
Dataset splitting module.

Responsible for separating features and target,
and creating train/test splits.
"""

from dataclasses import dataclass

from sklearn.model_selection import train_test_split

from src.config import config
from src.logger import logger
from src.schema import TARGET_COLUMN


@dataclass
class DatasetSplit:

    X_train: object
    X_test: object

    y_train: object
    y_test: object


class DataSplitter:

    def __init__(self):

        self.test_size = config.training["test_size"]

        self.random_state = config.training["random_state"]

    def split(self, dataframe):

        logger.info("Splitting dataset...")

        # -----------------------------------------
        # Copy dataframe
        # -----------------------------------------

        df = dataframe.copy()

        # -----------------------------------------
        # Convert Target
        #
        # 1 = Good Customer
        # 2 = Bad Customer
        #
        # Convert to:
        #
        # 0 = Good
        # 1 = Bad
        # -----------------------------------------

        df[TARGET_COLUMN] = df[TARGET_COLUMN].replace(
            {
                1: 0,
                2: 1,
            }
        )

        # -----------------------------------------
        # Split Features & Target
        # -----------------------------------------

        X = df.drop(columns=[TARGET_COLUMN])

        y = df[TARGET_COLUMN]

        # -----------------------------------------
        # Train Test Split
        # -----------------------------------------

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=y,
        )

        logger.success("Dataset split completed.")

        logger.info(f"Training Samples : {len(X_train)}")

        logger.info(f"Testing Samples : {len(X_test)}")

        return DatasetSplit(
            X_train=X_train,
            X_test=X_test,
            y_train=y_train,
            y_test=y_test,
        )