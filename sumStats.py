import createVars

def summaryStats():
    """
    Outputs the variable summary stats into summary_stats.txt
    """
    with open('summary_stats.txt', 'w') as f:
        for var in createVars.allVars:
            f.write(f"{createVars.df[var].describe()}")
    f.close()

summaryStats()



