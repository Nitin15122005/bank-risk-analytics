from app.ml.mapper import MLMapper
from app.ml.model_loader import ModelLoader


class Predictor:

    @staticmethod
    def predict(customer, loan):

        model = ModelLoader.load_model()

        df = MLMapper.to_dataframe(
            customer,
            loan,
        )

        prediction = int(model.predict(df)[0])

        probabilities = model.predict_proba(df)[0]

        bad_index = list(model.classes_).index(1)

        probability = float(probabilities[bad_index])

        risk_score = float(
            round(probability * 100, 2)
        )

        return {
            "prediction": (
                "Bad"
                if prediction == 1
                else "Good"
            ),
            "probability_of_default": probability,
            "risk_score": risk_score,
            "model_version": "v1.0.0",
        }