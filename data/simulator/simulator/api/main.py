from fastapi import FastAPI
from simulator.engine import simulate
from simulator.optimizer import predict_cost

app = FastAPI()

@app.get("/simulate")
def run(load: float, capacity: float, fuel_cost: float):
    sim = simulate(load, capacity)
    cost = predict_cost(capacity, fuel_cost)

    return {
        "simulation": sim,
        "cost": cost
    }
