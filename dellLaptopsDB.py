# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:57:17 2018

@author: Aadway
"""

import pandas as pd
import numpy

laptops = pd.read_csv('laptops.csv', encoding='latin-1')

laptops = laptops[laptops.Company == 'Dell']

ramCol = laptops.Ram

t1 = ramCol.values

for i in range(len(t1)):
    R = t1[i]
    if len(R) == 4:
        t1[i] = t1[i][0] + t1[i][1]
    else:
        t1[i] = t1[i][0]
    
#t1 = pd.core.series.Series(t1)
laptops.Ram = t1    


laptops = laptops.drop(['Inches', 'ScreenResolution', 'Gpu', 'Weight'], axis = 1)

priceCol = laptops.Price_euros
t2 = priceCol.values
for i in range(len(t2)):
    t2[i] = float(t2[i])*81.58
    





Price = laptops.Price_euros
laptops = laptops.drop(['Price_euros'], axis=1)
laptops['Price'] = Price


priceCol = laptops.Price.values


for i in range(len(priceCol)):
    print(priceCol[i])
    
    if (priceCol[i]) <= 60000:
        priceCol[i] = 1
    elif priceCol[i] <=150000:
        priceCol[i] = 2
    else:
        priceCol[i] = 3
        
laptops.Price = priceCol

laptops = laptops.drop(['Company'], axis=1)
laptops = laptops.drop(['Unnamed: 0'], axis=1)


##Not needed anymore
features = laptops.iloc[:, [1,2,4,5]].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
for i in range(4):
    features[:,i] = labelencoder.fit_transform(features[:,i])
##Not needed anymore ^


testOne = laptops[laptops.Ram == '16']
testOne = laptops[laptops.Price == '1']

##These are the inputs for respective columns, if user hasn't specified any
##the API guy needs to take care of that and set those values to zero(only if not specified by the user)    
a = input()
b = input()
c = input()
d = input()
e = input()
f = input()

##API guy needs to return this list or dataframe in JSON back to the website
requiredDF = filterOut(laptops,a,b,c,d,e,int(f))

###Sample inputs
##Notebook
##Intel Core i3 6006U 2GHz
##16
##256GB SSD
##Windows 10
##1

laptopsSave = laptops

CPU = laptops.Cpu.values
for i in range(len(laptops.Cpu)):
    CPU[i] = CPU[i][11] + CPU[i][12]
    
l = ['i3', 'i5', 'i7'] 

laptops = laptops[laptops.Cpu in l]

mem = laptops.Memory.values
for i in range(len(mem)):
    s = mem[i]
    if '256' in s:
        mem[i] = '256GB'
    elif '128' in s:
        mem[i] = '128GB'
    elif '500' in s:
        mem[i] = '500GB'
    elif '1TB' in s:
        mem[i] = '1TB'
    elif '16' in s:
        mem[i] = '1GGB'
    else:
        mem[i] = '64GB'

laptops = laptops[laptops.Cpu != 'um']


laptops.to_csv('finalLaptops.csv', sep=',', encoding='utf-8')

newFile = pd.read_csv('finalLaptops.csv')


def filterOut(laptopDF, typeNameVal='0', cpuVal='0', ramVal='0', memoryVal='0', opsysVal='0', priceVal=0):
    df=laptops
    #print(typeNameVal, ramVal)
    if typeNameVal!='0':
        df = df[df.TypeName == typeNameVal]
    #print("HERE1", df)
    if cpuVal!='0':
        df = df[df.Cpu == cpuVal]
    #print("HERE2", df)
    if ramVal!='0':
        df = df[df.Ram == ramVal]
    #print("HERE3", df)
    if memoryVal!='0':
        df = df[df.Memory == memoryVal]
    #print(df)
    if opsysVal!='0':
        df = df[df.OpSys == opsysVal]
    #print(df)
    if priceVal!=0:
        df = df[df.Price == priceVal]
    return df 


from flask import flash

usersDict = {'manipalJpr@DELL':'manipalPassword', 'dell@DELL':'dellPassword',
         'ourTeam@DELL':'ourTeamPassword'}

def authenticate(user, password):
    global usersDict
    if user in usersDict:
        if password == usersDict[user]:
            flash('Premium user logged in')
            ##render funtion to form page
        else:
            flash('Incorrect password!')
            ##render function back to login page
    else:
        flash("This premium user doesn't exist')
        ##render function back to login page
            


