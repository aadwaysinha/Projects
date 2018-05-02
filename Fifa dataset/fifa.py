import pandas as pd
import numpy as np
import matplotlib as mlt

fifa = pd.read_csv("complete.csv")

#Indices of independent variables: [3,5,6,7,9,10,11,13,]

#Indices contaioning data only about skillsets : [19,20,21,22,23,24,25,26]

x = fifa.iloc[:, 19:27]
y = fifa.iloc[:, 17:18]


#AIM: To predict the salary of a player based on his skillset using different types of regression models.
#What are the types of Regressions?
#Linear Regression
#Logistic Regression
#Polynomial Regression
#Stepwise Regression
#Ridge Regression
#Lasso Regression
#ElasticNet Regression

#Feature scaling our independent dataset
from sklearn.preprocessing import StandardScaler
ssX = StandardScaler()
ssY = StandardScaler()                          
x = ssX.fit_transform(x)
y = ssY.fit_transform(y)


#1. Linear Regression


from sklearn.cross_validation import train_test_split
xTrain1, xTest1, yTrain1, yTest1 = train_test_split(x, y, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LinearRegression
linearRegressor  = LinearRegression()
linearRegressor.fit(xTrain1, yTrain1)
yPred1 = linearRegressor.predict(xTest1) 

from sklearn.preprocessing import PolynomialFeatures
polyReg = PolynomialFeatures(degree=2)
xTrainPoly = polyReg.fit_transform(xTrain1)
polyReg.fit(xTrainPoly, yTrain1)
linReg2 = LinearRegression()
linReg2.fit(xTrainPoly, yTrain1)
yPredPoly = linReg2.predict(polyReg.fit_transform(xTest1))

from sklearn import metrics
print(metrics.r2_score(yTest1, yPredPoly))







