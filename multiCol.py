import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

df = pd.read_csv("../spotify_dataset.csv")

df["Explicit"] = df["Explicit"].map({"Yes": 1, "No": 0}).fillna(0).astype(int)

allVars = ["Tempo", "Loudness (db)", "Energy", "Danceability", "Positiveness", "Explicit", "Good for Party", "Good for Work/Study", "Good for Exercise", "Popularity"]

numVars = allVars[0:5]

dummyVars = allVars[5:-1] 

def calc_vif(X):
    """
    Calculates VIF for each independent variable
    """
    X = add_constant(X)
    vif_data = pd.DataFrame()
    vif_data["Variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif_data.iloc[1:]


num = df[numVars].copy()

dum = df[dummyVars].copy()
        
X = pd.concat([num, dum], axis=1)

def outVIF():
    with open('vif.txt', 'w') as f:
        f.write(f"Multicoliniarity Calculation (VIF):\n{calc_vif(X)}")
    f.close()

outVIF()