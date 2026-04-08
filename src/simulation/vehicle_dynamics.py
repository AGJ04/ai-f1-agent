def tyre_degradation(tyre_age):
    return tyre_age * 0.15

def fuel_effect(lap, total_laps, fuel_penalty):
    return (total_laps - lap) * fuel_penalty