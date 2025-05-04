from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import pandas as pd

def calc_vif(X):
    """
    Calculates VIF for each independent variable
    """
    X = add_constant(X)
    vif_data = pd.DataFrame()
    vif_data["Variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif_data.iloc[1:]

def outVIF(X, genre):
    """
    Outputs the VIF into vif.txt
    """
    with open(f'{genre}_vif.txt', 'w') as f:
        f.write(f"{genre} Multicoliniarity Calculation (VIF):\n{calc_vif(X)}")
    f.close()