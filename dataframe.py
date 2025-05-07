import pandas as pd

def dummify(col, df):
    '''
    Maps the "Yes" and "No" values in a column to their binary counterparts
    '''
    df[col] = df[col].map({"Yes": 1, "No": 0}).fillna(0).astype(int)
    return df

def standardize(col, df):
    """
    Transforms colums from 0 to 100 to 0 to 1 by dividing by 100
    """
    df[col] = df[col] / 100
    return df

def filter_by_genre(row, genre):
    return row['Genre'] == genre 

def createDF(genre):
    predf = pd.read_csv("../spotify_dataset.csv")
    predf = dummify("Explicit", predf)
    predf = standardize("Energy", predf)
    predf = standardize("Danceability", predf)
    predf = standardize("Positiveness", predf)
    predf = standardize("Popularity", predf)
    if genre == " ":
        return predf
    else:
        filtered_df = predf[predf.apply(lambda row: filter_by_genre(row, genre), axis=1)]
        return filtered_df