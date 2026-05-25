import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/generation_costs.csv")

X = df[["capacity", "fuel_cost"]]
y = df["total_cost"]

model = LinearRegression()
model.fit(X, y)

def predict_cost(capacity, fuel_cost):
    return model.predict([[capacity, fuel_cost]])[0]
