import pandas as pd

df = pd.read_csv("Dataset.csv")

print("Dataset shape:", df.shape)
print("\nFirst five titles:")
print(df[["title", "type", "listed_in"]].head())

print("\nMissing values:")
print(df.isnull().sum())