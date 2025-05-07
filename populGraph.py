import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import dataframe

def popGraph(genre):
    df = dataframe.createDF(genre)
    pop = df["Popularity"]

    sns.histplot(pop, kde=True, bins=30)
    plt.xlabel("Popularity Index")
    plt.ylabel("Frequency")
    plt.title(f"{genre}: Histogram of Popularity")
    plt.axvline(x=0, color='black', linestyle='--')
    plt.savefig(f'{genre}_populGraph.png')
    plt.show()

popGraph(" ")
popGraph("rock")
popGraph("pop")
popGraph("rap")