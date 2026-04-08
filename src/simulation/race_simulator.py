import random
from src.simulation.vehicle_dynamics import tyre_degradation, fuel_effect
from src.ai.decision_engine import aggregate_decision
from src.config import TOTAL_LAPS, PIT_THRESHOLD, FUEL_EFFECT

def simulate_race(drivers):
    tyre_age = {d: 0 for d in drivers}
    times = {d: 0 for d in drivers}

    log = []

    for lap in range(1, TOTAL_LAPS + 1):
        for driver in drivers:
            tyre_age[driver] += 1

            gap = random.uniform(0, 3)
            position = random.randint(1, len(drivers))
            base_time = 90 + random.uniform(-1, 1)

            decision, scores = aggregate_decision(
                tyre_age[driver], position, gap, base_time, PIT_THRESHOLD
            )

            if decision == "pit":
                tyre_age[driver] = 0
                base_time += 5

            lap_time = base_time \
                + tyre_degradation(tyre_age[driver]) \
                - fuel_effect(lap, TOTAL_LAPS, FUEL_EFFECT)

            times[driver] += lap_time

            message = generate_engineer_message(decision, tyre_age[driver], gap, position)

            # Calculate positions
            sorted_drivers = sorted(times.items(), key=lambda x: x[1])

            positions = {driver: i+1 for i, (driver, _) in enumerate(sorted_drivers)}
            log.append({
                "Lap": lap,
                "Driver": driver,
                "Decision": decision,
                "LapTime": lap_time,
                "CumulativeTime": times[driver],
                "TyreAge": tyre_age[driver],
                "Position": positions[driver],
                "EngineerMessage": message
            })

    return log

from src.ai.explainer import generate_engineer_message