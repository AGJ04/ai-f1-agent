import streamlit as st
import pandas as pd
import time

# -----------------------------------
# ⚙️ PAGE CONFIG
# -----------------------------------
st.set_page_config(layout="wide")

st.title("🏎️ AI Race Engineer — Replay Mode")

# -----------------------------------
# 📂 LOAD DATA
# -----------------------------------
try:
    df = pd.read_csv("race_log.csv")
except:
    st.error("❌ race_log.csv not found. Run main.py first.")
    st.stop()

# Ensure sorting
df = df.sort_values(["Lap", "Driver"])

laps = sorted(df["Lap"].unique())

# -----------------------------------
# 🎛️ CONTROLS
# -----------------------------------
st.sidebar.header("🎮 Replay Controls")

selected_lap = st.sidebar.slider(
    "Select Lap",
    min_value=min(laps),
    max_value=max(laps),
    value=min(laps)
)

play = st.sidebar.button("▶️ Play Replay")

speed = st.sidebar.slider(
    "Playback Speed (seconds)",
    min_value=0.05,
    max_value=1.0,
    value=0.2
)

# Session state for playback
if "lap" not in st.session_state:
    st.session_state.lap = selected_lap

# -----------------------------------
# ⏯️ AUTOPLAY LOGIC
# -----------------------------------
if play:
    for lap in laps:
        st.session_state.lap = lap
        time.sleep(speed)
        st.experimental_rerun()

# Use current lap
lap = st.session_state.get("lap", selected_lap)

lap_df = df[df["Lap"] == lap].copy()

# -----------------------------------
# 🧠 GAP TO LEADER
# -----------------------------------
if "CumulativeTime" in lap_df.columns:
    leader_time = lap_df["CumulativeTime"].min()
    lap_df["GapToLeader"] = lap_df["CumulativeTime"] - leader_time
else:
    lap_df["GapToLeader"] = 0

# -----------------------------------
# 🏁 LIVE POSITIONS
# -----------------------------------
st.subheader(f"🏁 Lap {lap} — Live Standings")

position_table = lap_df.sort_values("Position")[
    ["Driver", "Position", "LapTime", "GapToLeader"]
]

st.dataframe(position_table, use_container_width=True)

# -----------------------------------
# 📈 POSITION OVER TIME
# -----------------------------------
st.subheader("📊 Position Over Race")

if "Position" in df.columns:
    pivot_pos = df.pivot(index="Lap", columns="Driver", values="Position")
    st.line_chart(pivot_pos)

# -----------------------------------
# 📉 LAP TIME OVER TIME
# -----------------------------------
st.subheader("📈 Lap Time Trends")

pivot_lap = df.pivot(index="Lap", columns="Driver", values="LapTime")
st.line_chart(pivot_lap)

# -----------------------------------
# 📊 LAP TIMES THIS LAP
# -----------------------------------
st.subheader("⏱ Lap Times (Current Lap)")

lap_times = lap_df.set_index("Driver")["LapTime"]
st.bar_chart(lap_times)

# -----------------------------------
# 🎧 ENGINEER RADIO
# -----------------------------------
st.subheader("🎧 Engineer Radio (Live)")

for _, row in lap_df.sort_values("Position").iterrows():
    msg = row.get("EngineerMessage", "No message")
    st.write(f"**{row['Driver']} (P{row['Position']}):** {msg}")

# -----------------------------------
# 🎯 STRATEGY DECISIONS
# -----------------------------------
st.subheader("🧠 Strategy Decisions")

cols = ["Driver", "Decision", "TyreAge"]
available_cols = [c for c in cols if c in lap_df.columns]

st.dataframe(lap_df[available_cols], use_container_width=True)

# -----------------------------------
# 🔍 FULL DRIVER ANALYSIS
# -----------------------------------
st.sidebar.header("🔎 Driver Analysis")

driver = st.sidebar.selectbox("Select Driver", df["Driver"].unique())

driver_df = df[df["Driver"] == driver]

st.subheader(f"📊 {driver} — Full Race Analysis")

col1, col2 = st.columns(2)

with col1:
    st.line_chart(driver_df.set_index("Lap")["LapTime"])

with col2:
    if "Position" in driver_df.columns:
        st.line_chart(driver_df.set_index("Lap")["Position"])

# -----------------------------------
# 📜 LAST DECISIONS LOG
# -----------------------------------
st.subheader("📜 Recent Decisions")

recent = df[df["Lap"] <= lap].tail(10)

cols = ["Lap", "Driver", "Decision"]
available_cols = [c for c in cols if c in recent.columns]

st.dataframe(recent[available_cols], use_container_width=True)

# -----------------------------------
# ✅ FOOTER
# -----------------------------------
st.markdown("---")
st.caption("AI Race Engineer • Simulation + Replay System")