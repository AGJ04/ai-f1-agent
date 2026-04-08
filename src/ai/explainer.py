def generate_engineer_message(decision, tyre_age, gap, position):
    if decision == "pit":
        return f"Box now. Tyres at {tyre_age} laps, degradation critical."

    if decision == "push":
        return f"Push now. Gap {gap:.2f}s ahead, opportunity to gain position {position}."

    if decision == "conserve":
        return f"Manage tyres. Running P{position}, maintaining race pace."

    return "Maintain current strategy."