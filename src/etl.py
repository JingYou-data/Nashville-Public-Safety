from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/clean")

def load_calls(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, parse_dates=["call_datetime"])
    df["zip"] = df["zip"].astype(str).str.zfill(5)
    return df

def monthly_counts(df: pd.DataFrame) -> pd.DataFrame:
    return (df
            .assign(month=df["call_datetime"].dt.to_period("M").dt.to_timestamp())
            .groupby(["month", "zip"], as_index=False)
            .size()
            .rename(columns={"size": "calls"}))

if __name__ == "__main__":
    calls = load_calls("data/clean/calls_2018_2021.csv")
    out = monthly_counts(calls)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out.to_csv(DATA_DIR / "calls_monthly_by_zip.csv", index=False)
    print("✅ wrote data/clean/calls_monthly_by_zip.csv")
