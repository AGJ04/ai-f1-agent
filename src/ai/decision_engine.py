from src.ai.agents import strategy_agent, tyre_agent, performance_agent

def aggregate_decision(tyre_age, position, gap, lap_time, threshold):
    decisions = []

    d1, c1 = strategy_agent(position, gap)
    d2, c2 = tyre_agent(tyre_age, threshold)
    d3, c3 = performance_agent(lap_time)

    decisions.append((d1, c1))
    decisions.append((d2, c2))
    decisions.append((d3, c3))

    # weighted decision
    decision_scores = {}
    for d, c in decisions:
        decision_scores[d] = decision_scores.get(d, 0) + c

    final_decision = max(decision_scores, key=decision_scores.get)

    return final_decision, decision_scores