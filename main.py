import pandas as pd

# Config
from src.config import YEAR, GRAND_PRIX

# Data
from src.data.fastf1_loader import load_race_data

# Simulation
from src.simulation.race_simulator import simulate_race

# Analysis
from src.analysis.evaluator import evaluate
from src.analysis.visualisation import plot_lap_times, plot_real_vs_sim
from src.analysis.comparison import compare_with_real

# Monte Carlo
from src.ai.monte_carlo import monte_carlo_strategy, summarise_strategy

# Reporting
from src.reporting.report_generator import generate_report


def main():
    print("🚀 Starting AI Race Engineer Pipeline...\n")

    # -----------------------------------
    # 1. LOAD REAL RACE DATA (FastF1)
    # -----------------------------------
    print("📡 Loading FastF1 data...")
    laps, results = load_race_data(YEAR, GRAND_PRIX)

    drivers = results["Abbreviation"].dropna().tolist()[:5]
    print(f"✅ Loaded drivers: {drivers}\n")

    # -----------------------------------
    # 2. RUN SIMULATION
    # -----------------------------------
    print("🏎️ Running race simulation...")
    log = simulate_race(drivers)

    df = pd.DataFrame(log)
    df.to_csv("race_log.csv", index=False)
    print("✅ Simulation complete → race_log.csv\n")

    # -----------------------------------
    # 3. BASIC ANALYSIS
    # -----------------------------------
    print("📊 Evaluating performance...")
    insights = evaluate(df)

    for i in insights:
        print(" -", i)

    print("\n")

    # -----------------------------------
    # 4. VISUALISATIONS
    # -----------------------------------
    print("📈 Generating visualisations...")
    plot_lap_times(df)
    print(" - Saved: lap_times.png")

    # Real vs Sim
    print("📊 Comparing simulation vs real data...")
    comparison_df = compare_with_real(df, laps)
    comparison_df.to_csv("comparison.csv", index=False)

    plot_real_vs_sim(df, laps)
    print(" - Saved: real_vs_sim.png\n")

    # -----------------------------------
    # 5. MONTE CARLO STRATEGY ANALYSIS
    # -----------------------------------
    print("🎲 Running Monte Carlo simulations...")
    mc_df = monte_carlo_strategy(drivers, runs=10)

    summary = summarise_strategy(mc_df)
    summary.to_csv("monte_carlo_summary.csv", index=False)

    print("✅ Monte Carlo Summary:")
    print(summary, "\n")

    # -----------------------------------
    # 6. REPORT GENERATION
    # -----------------------------------
    print("📄 Generating PDF report...")
    generate_report(insights)
    print(" - Saved: report.pdf\n")

    # -----------------------------------
    # 7. FINAL OUTPUT SUMMARY
    # -----------------------------------
    print("🎉 PIPELINE COMPLETE\n")
    print("Generated files:")
    print(" - race_log.csv")
    print(" - comparison.csv")
    print(" - monte_carlo_summary.csv")
    print(" - lap_times.png")
    print(" - real_vs_sim.png")
    print(" - report.pdf\n")

    print("👉 Next step: run dashboard")
    print("streamlit run app/dashboard.py")


# -----------------------------------
# ENTRY POINT
# -----------------------------------
if __name__ == "__main__":
    main()