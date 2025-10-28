import pandas as pd

def confirmation_rates(df_calls: pd.DataFrame, df_incidents: pd.DataFrame) -> pd.DataFrame:
    confirmed = (df_calls
                 .merge(df_incidents[["incident_id","call_id","confirmed_type"]],
                        how="left", on="call_id"))
    rates = (confirmed
             .assign(is_confirmed=confirmed["confirmed_type"].notna())
             .groupby("call_type", as_index=False)["is_confirmed"].mean()
             .rename(columns={"is_confirmed":"confirmation_rate"}))
    return rates.sort_values("confirmation_rate", ascending=False)

if __name__ == "__main__":
    calls = pd.read_csv("data/clean/calls_2018_2021.csv")
    incidents = pd.read_csv("data/clean/incidents_2018_2021.csv")
    out = confirmation_rates(calls, incidents)
    out.to_csv("data/clean/confirmation_rates.csv", index=False)
    print("✅ wrote data/clean/confirmation_rates.csv")
