import statsmodels.api as sm
import config

depVar = 'Popularity'
yVar = config.df[depVar]

xVar = sm.add_constant(config.X)

olsModel = sm.OLS(yVar, xVar).fit()

def outOLS():
    """
    Outputs the OLS regression into ols.txt
    """
    with open('ols.txt', 'w') as f:
        f.write(f"OLS Regression:\n{olsModel.summary()}")
    f.close()

outOLS()