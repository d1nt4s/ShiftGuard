"""
Функции для обучения ML-моделей.
"""

import json
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from shiftguard.data.preprocess import build_preprocessor


def train_model(data: Any = None) -> Any:
    project_root = Path(__file__).resolve().parents[3]  
    data_path = project_root / "data" / "raw" / "german_credit.csv"
    artifacts_dir = project_root / "artifacts"
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    if not data_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {data_path}\n"
            "Put it into data/raw/german_credit.csv"
        )

    df = pd.read_csv(data_path)

    target_col = "credit_risk"
    if target_col not in df.columns:
        raise ValueError(f"Expected target column '{target_col}' in CSV")

    # ===== Target: сделаем бинарно 0/1 =====
    # В немецком кредите часто: 1=good, 2=bad (или наоборот).
    # Мы зафиксируем: дефолт/риск = 1, хороший = 0.
    y_raw = df[target_col].astype(int)
    # Считаем, что "2" — более рискованный класс (bad). Если окажется наоборот — потом поменяем.
    y = (y_raw == 2).astype(int)

    X = df.drop(columns=[target_col])

    # ===== Auto feature typing =====
    numeric_features = X.select_dtypes(include=["number"]).columns.tolist()
    categorical_features = [c for c in X.columns if c not in numeric_features]

    preprocessor = build_preprocessor(numeric_features, categorical_features)

    model = LogisticRegression(
        max_iter=2000,
        solver="liblinear",      # стабильный для small tabular
        class_weight="balanced", # полезно при дисбалансе 70/30
        random_state=42,
    )

    clf = Pipeline([
        ("preprocess", preprocessor),
        ("model", model),
    ])

    X_train, X_val, y_train, y_val = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    clf.fit(X_train, y_train)

    # proba для AUC
    val_proba = clf.predict_proba(X_val)[:, 1]
    val_pred = (val_proba >= 0.5).astype(int)

    auc = roc_auc_score(y_val, val_proba)
    f1 = f1_score(y_val, val_pred)

    metrics = {
        "auc": float(auc),
        "f1": float(f1),
        "n_train": int(len(X_train)),
        "n_val": int(len(X_val)),
        "positive_rate_train": float(y_train.mean()),
        "positive_rate_val": float(y_val.mean()),
        "threshold": 0.5,
        "numeric_features": numeric_features,
        "categorical_features": categorical_features,
    }

    print("=== Baseline metrics ===")
    print(json.dumps(metrics, indent=2, ensure_ascii=False))

    # Save pipeline (preprocess + model)
    model_path = artifacts_dir / "model_v1.pkl"
    joblib.dump(clf, model_path)

    metrics_path = artifacts_dir / "metrics_v1.json"
    metrics_path.write_text(json.dumps(metrics, indent=2, ensure_ascii=False), encoding="utf-8")

    schema_path = artifacts_dir / "schema_v1.json"
    schema_path.write_text(
        json.dumps(
            {"target": target_col, "numeric": numeric_features, "categorical": categorical_features},
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(f"\nSaved model to: {model_path}")
    print(f"Saved metrics to: {metrics_path}")
    print(f"Saved schema to: {schema_path}")
