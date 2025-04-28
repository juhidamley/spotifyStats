import pandas as pd

predf = pd.read_csv("../spotify_dataset.csv")

allVars = ["Tempo", "Loudness (db)", "Energy", "Danceability", "Positiveness", "Explicit", "Good for Party", "Good for Work/Study", "Good for Exercise", "Popularity"]

dummyVars = allVars[4:-1]

numVars = allVars[0:4]

def dummify(col, df):
    '''
    Maps the "Yes" and "No" values in a column to their binary counterparts
    '''
    df["Explicit"] = df["Explicit"].map({"Yes": 1, "No": 0}).fillna(0).astype(int)
    return df

df = dummify("Explicit", predf)


num = df[numVars].copy()

dum = df[dummyVars].copy()
        
X = pd.concat([num, dum], axis=1)