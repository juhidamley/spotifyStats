import multiReg
import createVars

olsModel = sm.OLS(createVars.yVar, createVars.xVar).fit()

