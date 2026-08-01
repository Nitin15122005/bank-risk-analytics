from src.data_loader import DataLoader
from src.preprocessing import DataPreprocessor
from src.validator import DataValidator

loader = DataLoader()

df = loader.run()

validator = DataValidator()

validator.run(df)

X = df.drop(columns=["Credit Risk"])

y = df["Credit Risk"]

preprocessor = DataPreprocessor().build()

X_processed = preprocessor.fit_transform(X)

print("=" * 60)
print("Original Shape :", X.shape)
print("Processed Shape:", X_processed.shape)
print("=" * 60)