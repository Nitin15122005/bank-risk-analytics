"""
Main Training Script.

Run:

python -m src.train
"""

from src.artifact_manager import ArtifactManager
from src.data_loader import DataLoader
from src.logger import logger
from src.splitter import DataSplitter
from src.trainer import ModelTrainer
from src.validator import DataValidator


def main():

    logger.info("=" * 70)
    logger.info("BANK RISK ANALYTICS")
    logger.info("=" * 70)

    # ---------------------------------------------------------
    # Load Dataset
    # ---------------------------------------------------------

    loader = DataLoader()

    dataframe = loader.load()

    # ---------------------------------------------------------
    # Validate Dataset
    # ---------------------------------------------------------

    validator = DataValidator()

    validator.validate(
        dataframe,
    )

    # ---------------------------------------------------------
    # Split Dataset
    # ---------------------------------------------------------

    splitter = DataSplitter()

    split = splitter.split(
        dataframe,
    )

    # ---------------------------------------------------------
    # Train Models
    # ---------------------------------------------------------

    trainer = ModelTrainer()

    (
        best_pipeline,
        best_model,
        results,
    ) = trainer.train(
        split,
    )

    # ---------------------------------------------------------
    # Save Artifacts
    # ---------------------------------------------------------

    ArtifactManager().save(

        pipeline=best_pipeline,

        metrics=results,

        model_name=best_model,

    )

    logger.success("=" * 70)
    logger.success("TRAINING FINISHED")
    logger.success("=" * 70)

    print("\n")
    print(results)
    print("\n")


if __name__ == "__main__":

    main()