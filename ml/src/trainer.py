"""
Model Trainer.

Responsible for:
- Building preprocessing pipeline
- Training all enabled models
- Evaluating every model
- Selecting the best model
"""

import pandas as pd
from sklearn.pipeline import Pipeline

from src.config import config
from src.evaluator import Evaluator
from src.logger import logger
from src.models import ModelFactory
from src.preprocessing import DataPreprocessor


class ModelTrainer:

    def __init__(self):

        self.preprocessor = DataPreprocessor()

        self.model_factory = ModelFactory()

        self.evaluator = Evaluator()

        self.metric = config.training["evaluation_metric"]

    def train(self, split):

        logger.info("=" * 70)
        logger.info("MODEL TRAINING")
        logger.info("=" * 70)

        preprocessing_pipeline = self.preprocessor.build()

        models = self.model_factory.get_models()

        results = []

        best_pipeline = None

        best_model = None

        best_score = float("-inf")

        logger.info(f"Evaluation Metric : {self.metric}")

        logger.info(f"Models : {list(models.keys())}")

        for model_name, model in models.items():

            logger.info("-" * 70)

            logger.info(f"Training {model_name}")

            pipeline = Pipeline(

                steps=[

                    (
                        "preprocessing",
                        preprocessing_pipeline,
                    ),

                    (
                        "classifier",
                        model,
                    ),

                ]

            )

            pipeline.fit(

                split.X_train,

                split.y_train,

            )

            metrics = self.evaluator.evaluate(

                pipeline,

                split.X_test,

                split.y_test,

            )

            metrics["Model"] = model_name

            results.append(metrics)

            score = metrics[self.metric]

            logger.info(

                f"{model_name} {self.metric} : {score:.4f}"

            )

            if score > best_score:

                best_score = score

                best_pipeline = pipeline

                best_model = model_name

        logger.info("=" * 70)

        results = pd.DataFrame(results)

        columns = [

            "Model",

            "accuracy",

            "precision",

            "recall",

            "f1_score",

            "roc_auc",

        ]

        results = results[columns]

        results = results.sort_values(

            by=self.metric,

            ascending=False,

        ).reset_index(drop=True)

        logger.success("=" * 70)

        logger.success("TRAINING COMPLETED")

        logger.success("=" * 70)

        logger.success(f"Best Model : {best_model}")

        logger.success(

            f"{self.metric} : {best_score:.4f}"

        )

        logger.success("=" * 70)

        print()

        print(results)

        print()

        return (

            best_pipeline,

            best_model,

            results,

        )