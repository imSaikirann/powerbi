from __future__ import annotations

from pathlib import Path
import json

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


BASE_DIR = Path(__file__).resolve().parents[1]
CLEAN_DATA_PATH = BASE_DIR / "data" / "cleaned" / "hr_employee_data_clean.csv"
MODEL_REPORT_PATH = BASE_DIR / "data" / "processed" / "attrition_model_report.json"


def main() -> None:
    if not CLEAN_DATA_PATH.exists():
        raise FileNotFoundError(f"Missing cleaned dataset at {CLEAN_DATA_PATH}. Run clean_hr_data.py first.")

    frame = pd.read_csv(CLEAN_DATA_PATH, parse_dates=["date_of_joining", "exit_date"])
    frame["attrition_flag"] = frame["attrition"].map({"Yes": 1, "No": 0})

    feature_columns = [
        "age",
        "gender",
        "department",
        "job_role",
        "salary",
        "performance_rating",
        "attendance_percentage",
        "location",
        "tenure_years",
    ]
    X = frame[feature_columns]
    y = frame["attrition_flag"]

    categorical_columns = ["gender", "department", "job_role", "location"]
    numeric_columns = ["age", "salary", "performance_rating", "attendance_percentage", "tenure_years"]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                numeric_columns,
            ),
            (
                "categorical",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("encoder", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical_columns,
            ),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    report = classification_report(y_test, predictions, output_dict=True)
    summary = {
        "roc_auc": round(float(roc_auc_score(y_test, probabilities)), 4),
        "classification_report": report,
        "target_positive_rate": round(float(y.mean()), 4),
        "training_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
    }

    MODEL_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    MODEL_REPORT_PATH.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Attrition model report written to {MODEL_REPORT_PATH}.")


if __name__ == "__main__":
    main()
