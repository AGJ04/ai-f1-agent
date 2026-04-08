def strategy_agent(position, gap):
    if gap < 1:
        return "push", 0.8
    return "conserve", 0.6

def tyre_agent(tyre_age, threshold):
    if tyre_age > threshold:
        return "pit", 0.95
    return "stay_out", 0.7

def performance_agent(lap_time):
    if lap_time > 92:
        return "push", 0.75
    return "conserve", 0.6