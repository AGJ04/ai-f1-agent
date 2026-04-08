import matplotlib.pyplot as plt

def plot_lap_times(df):
    for driver in df["Driver"].unique():
        d = df[df["Driver"] == driver]
        plt.plot(d["Lap"], d["LapTime"], label=driver)

    plt.legend()
    plt.title("Lap Times")
    plt.savefig("lap_times.png")
    plt.close()


def plot_real_vs_sim(sim_df, real_laps):
    import matplotlib.pyplot as plt

    for driver in sim_df["Driver"].unique():
        try:
            real = real_laps.pick_driver(driver)
        except:
            continue

        sim = sim_df[sim_df["Driver"] == driver]

        plt.plot(sim["Lap"], sim["LapTime"], label=f"{driver} Sim")
        plt.plot(real["LapNumber"], real["LapTime"].dt.total_seconds(),
                 linestyle='dashed', label=f"{driver} Real")

    plt.legend()
    plt.title("Real vs Simulated Lap Times")
    plt.savefig("real_vs_sim.png")
    plt.close()