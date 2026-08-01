"""
Model factory.

Creates machine learning models based on the
configuration file.
"""

from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from src.config import config
from src.logger import logger


class ModelFactory:

    def __init__(self):

        self.random_state = config.training["random_state"]

    def get_models(self):

        logger.info("Loading enabled models...")

        models = {}

        model_config = config.models

        if model_config["logistic_regression"]["enabled"]:

            models["Logistic Regression"] = LogisticRegression(
                random_state=self.random_state,
                max_iter=1000,
            )

        if model_config["decision_tree"]["enabled"]:

            models["Decision Tree"] = DecisionTreeClassifier(
                random_state=self.random_state,
            )

        if model_config["random_forest"]["enabled"]:

            models["Random Forest"] = RandomForestClassifier(
                random_state=self.random_state,
                n_estimators=300,
            )

        if model_config["gradient_boosting"]["enabled"]:

            models["Gradient Boosting"] = GradientBoostingClassifier(
                random_state=self.random_state,
            )

        logger.success(f"{len(models)} models loaded.")

        return models
