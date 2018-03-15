import pandas as pd
import numpy as np
import matplotlib as mlt

fifa = pd.read_csv("complete.csv")

#Indices of independent variables: [3,5,6,7,9,10,11,13,]

#Indices contaioning data only about skillsets : [19,20,21,22,23,24,25,26]

x = fifa.iloc[:,19:27]











