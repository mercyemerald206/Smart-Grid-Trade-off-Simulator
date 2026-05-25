def simulate(load, capacity):
    reliability = min(1.0, capacity / (load + 1e-6))
    efficiency = 0.9 - (capacity * 0.0005)

    return {
        "reliability": reliability,
        "efficiency": efficiency
    }
