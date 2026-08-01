from functools import lru_cache
from pathlib import Path
import sys

import joblib


class ModelLoader:

    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    ML_ROOT = PROJECT_ROOT / "ml"

    MODEL_PATH = (
        ML_ROOT
        / "trained_models"
        / "latest"
        / "model.pkl"
    )

    @classmethod
    @lru_cache(maxsize=1)
    def load_model(cls):

        print("PROJECT_ROOT:", cls.PROJECT_ROOT)
        print("ML_ROOT:", cls.ML_ROOT)
        print("MODEL_PATH:", cls.MODEL_PATH)

        if str(cls.ML_ROOT) not in sys.path:
            sys.path.insert(0, str(cls.ML_ROOT))

        print("\nFirst 5 sys.path entries:")
        for p in sys.path[:5]:
            print(p)

        return joblib.load(cls.MODEL_PATH)