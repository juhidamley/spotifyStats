import pandas as pd
import sys

df = pd.read_csv("../spotify_dataset.csv")

allVars = ["Tempo", "Loudness (db)", "Energy", "Danceability", "Positiveness", "Explicit", "Good for Party", "Good for Work/Study", "Good for Exercise", "Popularity"]

dummyVars = [allVars[4:-1]]

numVars = [allVars[0:4]]

#print(df["Explicit"])

def dummify(col):
    '''
    Maps the "Yes" and "No" values in a column to their binary counterparts
    '''
    df[col] = df[col].map({"Yes": 1, "No": 0})


#print(df["Explicit"].head)

def summaryStats():
    with open('summary_stats.txt', 'w') as f:
        for var in allVars:
            f.write(f"{df[var].describe()}")
    f.close()

dummify("Explicit")
summaryStats()



