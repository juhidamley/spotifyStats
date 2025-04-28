import config

def summaryStats():
    """
    Outputs the variable summary stats into summary_stats.txt
    """
    with open('summary_stats.txt', 'w') as f:
        for var in config.allVars:
            f.write(f"{config.df[var].describe()}")
    f.close()

summaryStats()



