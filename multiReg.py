import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sb

def outOLS(genre, xVar, yVar):
    """
    Outputs the OLS regression into ols.txt
    """
    olsModel = sm.OLS(yVar, xVar).fit()
    with open(f'{genre}_ols.txt', 'w') as f:
        f.write(f"OLS Regression:\n{olsModel.summary()}")
    f.close()

def resPlot(genre, xVar, yVar):
    olsModel = sm.OLS(yVar, xVar).fit()
    residuals = olsModel.resid
    fitted_values = olsModel.fittedvalues

    sb.scatterplot(x=fitted_values, y=residuals)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel('Fitted Values')
    plt.ylabel('Residuals')
    plt.title(f'{genre} Residuals vs. Fitted Values')
    plt.savefig(f'{genre}_resPlot.png') 
    plt.show()