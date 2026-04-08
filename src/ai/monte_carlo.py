import pandas as pd
from src.simulation.race_simulator import simulate_race

def monte_carlo_strategy(drivers, runs=10):
    results = []

    for i in range(runs):
        log = simulate_race(drivers)
        df = pd.DataFrame(log)

        final = df[df["Lap"] == df["Lap"].max()]

        for _, row in final.iterrows():
            results.append({
                "Driver": row["Driver"],
                "FinishTime": row["CumulativeTime"]
            })

    return pd.DataFrame(results)

def summarise_strategy(mc_df):
    return mc_df.groupby("Driver")["FinishTime"].mean().reset_index()
