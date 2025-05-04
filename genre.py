import dataframe
import createVars as cV
import spotVars as sV
import sumStats as sS
import multiReg as mR
import multiCol as mC

def genre_stats(genre):
    gen_df = dataframe.createDF(genre)
    yVar, xVar, X, num, dum = cV.dfVars(gen_df, sV.numVars, sV.dummyVars, sV.depVar)

    sS.summaryStats(genre, gen_df, sV.allVars)
    mR.outOLS(genre, xVar, yVar)
    mR.resPlot(genre, xVar, yVar)
    mC.calc_vif(X)
    mC.outVIF(X, genre)

# genre_stats("pop")

