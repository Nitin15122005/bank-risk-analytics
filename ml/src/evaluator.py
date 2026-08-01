"""
Model evaluation module.

Evaluates trained models using multiple metrics and
generates evaluation reports.
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

from src.constants import (
    FIGURES_DIR,
    METRICS_DIR,
)
from src.logger import logger


class Evaluator:

    def __init__(self):

        FIGURES_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        METRICS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    def evaluate(
        self,
        pipeline,
        X_test,
        y_test,
    ):

        logger.info("Evaluating model...")

        predictions = pipeline.predict(X_test)

        probabilities = pipeline.predict_proba(X_test)[:, 1]

        metrics = {

            "accuracy": accuracy_score(
                y_test,
                predictions,
            ),

            "precision": precision_score(
                y_test,
                predictions,
                zero_division=0,
            ),

            "recall": recall_score(
                y_test,
                predictions,
                zero_division=0,
            ),

            "f1_score": f1_score(
                y_test,
                predictions,
                zero_division=0,
            ),

            "roc_auc": roc_auc_score(
                y_test,
                probabilities,
            ),
        }

        logger.success("Evaluation Complete")

        for key, value in metrics.items():

            logger.info(
                f"{key:<12}: {value:.4f}"
            )

        # =====================================================
        # Classification Report
        # =====================================================

        report = classification_report(
            y_test,
            predictions,
            output_dict=True,
            zero_division=0,
        )

        report = pd.DataFrame(report).transpose()

        report.to_csv(
            METRICS_DIR / "classification_report.csv",
            index=True,
        )

        # =====================================================
        # Confusion Matrix
        # =====================================================

        cm = confusion_matrix(
            y_test,
            predictions,
        )

        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm,
        )

        disp.plot()

        plt.tight_layout()

        plt.savefig(
            FIGURES_DIR / "confusion_matrix.png",
            dpi=300,
        )

        plt.close()

        # =====================================================
        # ROC Curve
        # =====================================================

        RocCurveDisplay.from_predictions(
            y_test,
            probabilities,
            pos_label=2,
        )

        plt.tight_layout()

        plt.savefig(
            FIGURES_DIR / "roc_curve.png",
            dpi=300,
        )

        plt.close()

        return metrics