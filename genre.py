import dataframe
import createVars as cV
import spotVars as sV
import sumStats as sS
import multiReg as mR
import multiCol as mC
import normGraph as nG

def genre_stats(genre):
    gen_df = dataframe.createDF(genre)
    yVar, xVar, X, num, dum = cV.dfVars(gen_df, sV.numVars, sV.dummyVars, sV.depVar)

    sS.summaryStats(genre, gen_df, sV.allVars)
    mR.outOLS(genre, xVar, yVar)
    mR.resPlot(genre, xVar, yVar)
    mC.calc_vif(X)
    mC.outVIF(X, genre)
    nG.normGraph(genre, yVar, xVar)

def uniquedf():
    gen_df = dataframe.createDF(" ")
    unique_values = gen_df["Genre"].value_counts()
    print(unique_values)

#genre_stats("pop")
#genre_stats("rock")
#genre_stats("rap")
#genre_stats(" ")
genre_stats("hip hop")
#uniquedf()