# data.py
from __future__ import annotations

from pathlib import Path
import pandas as pd

UCI_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"

# Имена колонок (20 features + 1 target) для german.data (категориальный вариант)
COLUMNS = [
    "checking_status",
    "duration_months",
    "credit_history",
    "purpose",
    "credit_amount",
    "savings_status",
    "employment",
    "installment_rate",
    "personal_status",
    "other_debtors",
    "residence_since",
    "property_magnitude",
    "age",
    "other_payment_plans",
    "housing",
    "existing_credits",
    "job",
    "num_dependents",
    "own_telephone",
    "foreign_worker",
    "credit_risk",  # target: 1=good, 2=bad (по описанию UCI)  [oai_citation:2‡archive.ics.uci.edu](https://archive.ics.uci.edu/ml/datasets/statlog%2B%28german%2Bcredit%2Bdata%29?utm_source=chatgpt.com)
]

def ensure_dirs() -> dict[str, Path]:
    root = Path(__file__).resolve().parents[1]
    data_dir = root / "data"
    raw_dir = data_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    return {"root": root, "data": data_dir, "raw": raw_dir}

def download_and_load() -> pd.DataFrame:
    # pandas умеет читать прямо по URL
    df = pd.read_csv(UCI_URL, sep=r"\s+", header=None, names=COLUMNS)
    return df

def main() -> None:
    paths = ensure_dirs()
    df = download_and_load()

    out_path = paths["raw"] / "german_credit.csv"
    df.to_csv(out_path, index=False)

    print("Saved:", out_path)
    print("Shape:", df.shape)
    print("Head:\n", df.head())
    print("\nTarget value counts:\n", df["credit_risk"].value_counts(dropna=False))

if __name__ == "__main__":
    main()