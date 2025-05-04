import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# gen_df = dataframe.createDF(" ")
# yVar, xVar, X, num, dum = cV.dfVars(gen_df, sV.numVars, sV.dummyVars, sV.depVar)

def normGraph(genre, yVar, xVar):
    model = sm.OLS(yVar, xVar).fit()

    standardized_residuals = model.get_influence().resid_studentized_internal

    sns.histplot(standardized_residuals, kde=True, bins=30)
    plt.xlabel("Standardized Residuals")
    plt.ylabel("Frequency")
    plt.title(f"{genre}: Histogram of Standardized Residuals")
    plt.axvline(x=0, color='black', linestyle='--')
    plt.savefig(f'{genre}_normGraph.png')
    plt.show()
