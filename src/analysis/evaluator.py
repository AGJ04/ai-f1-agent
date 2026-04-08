import pandas as pd

def evaluate(df):
    insights = []

    for driver in df["Driver"].unique():
        d = df[df["Driver"] == driver]

        avg = d["LapTime"].mean()
        pits = (d["Decision"] == "pit").sum()

        insights.append(f"{driver}: Avg Lap {avg:.2f}s, Pit Stops {pits}")

    return insights