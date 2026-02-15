def test_import_package():
    # Проверяем, что пакет импортируется (это базовый сигнал "проект живой")
    import shiftguard  # noqa: F401


def test_basic_math_smoke():
    # Просто чтобы pytest точно работал и не было "0 tests collected"
    assert 1 + 1 == 2

def test_preprocessing():
    from sklearn.model_selection import train_test_split
    import pandas as pd

    from preprocess import build_preprocessor

    df = pd.read_csv("data/raw/german_credit.csv")

    df["credit_risk"] = df["credit_risk"].map({1: 0, 2: 1})

    X = df.drop(columns=["credit_risk"])
    y = df["credit_risk"]

    numeric_features = [
        "duration_months",
        "credit_amount",
        "installment_rate",
        "residence_since",
        "age",
        "existing_credits",
        "num_dependents"
    ]

    categorical_features = [
        "checking_status",
        "credit_history",
        "purpose",
        "savings_status",
        "employment",
        "personal_status",
        "other_debtors",
        "property_magnitude",
        "other_payment_plans",
        "housing",
        "job",
        "own_telephone",
        "foreign_worker"
    ]

    preprocessor = build_preprocessor(numeric_features, categorical_features)

    X_transformed = preprocessor.fit_transform(X)

    print("Transformed shape:", X_transformed.shape)