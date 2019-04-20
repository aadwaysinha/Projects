import pandas as pd
import random
import math

df = pd.read_csv('sheet1.csv')

df = df.drop(['NAME', 'Random', 'BEFORE ENDSEM', 'Unnamed: 11', 'SESSIONAL 1.1'], axis=1)

sesh2update = df['SESSIONAL 2']

for i in range(len(sesh2update)):
    if sesh2update[i] <= 0:
        sesh2update[i] = random.randint(0,5)
        print('changed value at:', i)
    elif sesh2update[i] > 15:
        sesh2update[i] = random.randint(13, 15)

df['SESSIONAL 2'] = sesh2update


df['afterSESH2'] = df['SESSIONAL 2']
updateafterSesh2 = df['afterSESH2']

for i in range(len(updateafterSesh2)):
    updateafterSesh2[i] = df['SESSIONAL 2'][i] + df['SESSIONAL 1'][i]

df['afterSESH2'] = updateafterSesh2


df = df.drop('ENDSEM', axis=1)



df['HESM'] = (df['SESSIONAL 1'] + df['SESSIONAL 2'] + df['INTERNALS'])*(40/60) - random.randint(0, 15)

hesmupdate = df['HESM']
for i in range(len(hesmupdate)):
    if hesmupdate[i] <=0:
        hesmupdate[i] = random.randint(5, 11)
    elif hesmupdate[i] > 40:
        hesmupdate[i] = random.randint(35, 40)
    hesmupdate[i] = math.floor(hesmupdate[i])

df['HESM'] = hesmupdate

df['TOTAL'] = df['SESSIONAL 1'] + df['SESSIONAL 2'] + df['INTERNALS']+df['HESM']

df = df.sort_values(by='TOTAL', ascending=False)

df['GRADE'] = df['TOTAL']


updateGrade = df['GRADE']
minWindowForAGrade = (len(updateGrade)-1)//10
print('mwg: ', minWindowForAGrade)
grade = ['A+', 'A', 'B', 'C', 'D', 'E', 'F']
totalM = df['TOTAL']

lTotalM = []
for i in range(len(totalM)):
    lTotalM.append(totalM[i])
lTotalM = sorted(lTotalM)
lTotalM.reverse()

currentGradePtr = 0
pos = 0
gradeList = lTotalM
addNumber = 0
while pos<len(updateGrade):
    lastMarkForCurrentGrade = lTotalM[pos+minWindowForAGrade]
    print(type(lastMarkForCurrentGrade))
    lastMarkForCurrentGrade = addNumber + lastMarkForCurrentGrade
    addNumber += 10
    print("LMFCG ", pos+minWindowForAGrade, ": ", lastMarkForCurrentGrade)
    for index, row in range(minWindowForAGrade):
        gradeList[pos] = grade[currentGradePtr]
        pos+=1
        if pos >= len(updateGrade):
            break
    while pos<len(updateGrade) and lTotalM[pos] == lastMarkForCurrentGrade:
        gradeList[pos] = grade[currentGradePtr]
        pos+=1
    currentGradePtr+=1
    if currentGradePtr > 6:
        while pos < len(updateGrade):
            gradeList.append('F')
            pos+=1

gradeList = pd.core.series.Series(gradeList)

df['GRADE'] = gradeList

finalGrade = list()
for i in range(0, 177):
    finalGrade.append(0)

for i in range(0, 20):
    finalGrade[i] = 'A+'

for i in range(20, 50):
    finalGrade[i] = 'A'

for i in range(50, 100):
    finalGrade[i] = 'B'

for i in range(100, 125):
    finalGrade[i] = 'C'
    
for i in range(125, 145):
    finalGrade[i] = 'D'
    
for i in range(145, 165):
    finalGrade[i] = 'E'

for i in range(165, 177):
    finalGrade[i] = 'F'

finalGrade = pd.core.series.Series(finalGrade)
df['GRADE'] = finalGrade


for i, row in df.iterrows():
    if row['TOTAL'] > 80:
        

    
df.to_csv('OOPJdata')

