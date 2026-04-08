import pandas as pd

def compare_with_real(sim_df, real_laps):
    comparisons = []

    for driver in sim_df["Driver"].unique():
        sim_driver = sim_df[sim_df["Driver"] == driver]

        try:
            real_driver = real_laps.pick_driver(driver)
        except:
            continue

        real_avg = real_driver["LapTime"].dt.total_seconds().mean()
        sim_avg = sim_driver["LapTime"].mean()

        comparisons.append({
            "Driver": driver,
            "SimAvgLap": round(sim_avg, 2),
            "RealAvgLap": round(real_avg, 2),
            "Delta": round(sim_avg - real_avg, 2)
        })

    return pd.DataFrame(comparisons)