import pandas as pd

df = pd.read_csv("../spotify_dataset.csv")

print(df["Explicit"])

def dummify(col):
    '''
    Maps the "Yes" and "No" values in a column to their binary counterparts
    '''
    df[col] = df[col].map({"Yes": 1, "No": 0})

dummify("Explicit")
print(df["Explicit"].head)

