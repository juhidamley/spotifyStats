from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import createVars
import dataframe
import spotVars

def calc_vif(X):
    """
    Calculates VIF for each independent variable
    """
    X = add_constant(X)
    vif_data = createVars.pd.DataFrame()
    vif_data["Variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif_data.iloc[1:]

def outVIF(X):
    """
    Outputs the VIF into vif.txt
    """
    with open('vif.txt', 'w') as f:
        f.write(f"Multicoliniarity Calculation (VIF):\n{calc_vif(createVars.X)}")
    f.close()

outVIF()