import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sb
import createVars



olsModel = sm.OLS(createVars.yVar, createVars.xVar).fit()

def outOLS():
    """
    Outputs the OLS regression into ols.txt
    """
    with open('ols.txt', 'w') as f:
        f.write(f"OLS Regression:\n{olsModel.summary()}")
    f.close()

def resPlot():
    residuals = olsModel.resid
    fitted_values = olsModel.fittedvalues

    sb.scatterplot(x=fitted_values, y=residuals)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel('Fitted Values')
    plt.ylabel('Residuals')
    plt.title('Residuals vs. Fitted Values')
    plt.show()

outOLS()
#resPlot()