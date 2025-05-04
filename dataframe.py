import pandas as pd

def dummify(col, df):
    '''
    Maps the "Yes" and "No" values in a column to their binary counterparts
    '''
    df[col] = df[col].map({"Yes": 1, "No": 0}).fillna(0).astype(int)
    return df

def filter_by_genre(row, genre):
    return row['Genre'] == genre 

def createDF(genre):
    predf = pd.read_csv("../spotify_dataset.csv")
    predf = dummify("Explicit", predf)
    if genre == " ":
        return predf
    else:
        filtered_df = predf[predf.apply(lambda row: filter_by_genre(row, genre), axis=1)]
        return filtered_df