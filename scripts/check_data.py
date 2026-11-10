"""Comprueba que el dataset esté en su lugar y tenga la forma esperada.

El dataset no se versiona en este repositorio. Se descarga desde Kaggle
("Customer Churn", archivo telecom_churn.csv):

    https://www.kaggle.com/datasets/barun2104/telecom-churn

y se guarda como data/telecom_churn.csv. Con la CLI de Kaggle configurada:

    kaggle datasets download -d barun2104/telecom-churn -p data --unzip

Uso:
    python scripts/check_data.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "telecom_churn.csv"
EXPECTED_ROWS = 3333
EXPECTED_COLUMNS = [
    "Churn",
    "AccountWeeks",
    "ContractRenewal",
    "DataPlan",
    "DataUsage",
    "CustServCalls",
    "DayMins",
    "DayCalls",
    "MonthlyCharge",
    "OverageFee",
    "RoamMins",
]


def main() -> int:
    if not DATA_PATH.exists():
        print(f"No se encontró {DATA_PATH}.\n{__doc__}", file=sys.stderr)
        return 1

    df = pd.read_csv(DATA_PATH)
    problems = []
    if list(df.columns) != EXPECTED_COLUMNS:
        problems.append(f"columnas distintas a las esperadas: {list(df.columns)}")
    if len(df) != EXPECTED_ROWS:
        problems.append(f"{len(df)} filas en lugar de {EXPECTED_ROWS}")

    if problems:
        print("El archivo no coincide con el dataset esperado: " + "; ".join(problems), file=sys.stderr)
        return 1

    print(f"Dataset correcto: {len(df)} filas, {df.shape[1]} columnas, {df['Churn'].mean():.2%} de churn.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
