import pandas as pd

def summaryStats(genre, df, allVars):
    """
    Outputs the variable summary stats into summary_stats.txt
    """
    with open(f'{genre}_summary_stats.txt', 'w') as f:
        for var in allVars:
            f.write(f"{df[var].describe()}")
    f.close()