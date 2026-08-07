import pandas as pd

def validate(df):
    rejected = df[df.isnull().any(axis=1)]
    valid = df.dropna()

    rejected.to_csv("data/rejected/rejected_orders.csv", index=False)

    return valid