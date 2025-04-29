import statsmodels.api as sm
import pandas as pd

def dfVars(df, numVars, dummyVars, depVar):
    num = df[numVars].copy()
    dum = df[dummyVars].copy()
    X = pd.concat([num, dum], axis=1)
    yVar = df[depVar]
    xVar = sm.add_constant(X)
    return yVar, xVar, X, num, dum