from fastapi import FastAPI
import random

app = FastAPI(title="Smart Grid Simulator")

@app.get("/simulate")
def simulate():
    demand = random.randint(50, 150)
    supply = random.randint(60, 140)

    efficiency = supply / demand

    return {
        "demand": demand,
        "supply": supply,
        "efficiency": round(efficiency, 3),
        "status": "OPTIMAL" if efficiency > 1 else "STRESSED"
    }
