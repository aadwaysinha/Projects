
import pandas as pd
import numpy as np
import urllib, json
import unicodedata


#Loading the data from the internet and converting it into a useful dataframe.
url = "http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/spam_ham.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
dataUF = pd.DataFrame(np.random.randint(low=0, high=10, size=(5572, 2)),
                   columns=['Message', 'Target'])

for index in range(5572):
    sentence = data[index]['v2']
    target = data[index]['v1']
    dataUF.iloc[index, 0] = sentence
    dataUF.iloc[index, 1] = target
             
##import json ( Didn't really work very well)
#s = '[{"i":"imap.gmail.com","p":"someP@ss"},{"i":"imap.aol.com","p":"anoterPass"}]'
#jdata = json.loads(s)
#index = 0
#for index in jdata:
    
    
    
#Frequency counter def
def countFreq(message, word):
    message = message.split(' ')
    count = 0
    for i in message:
        if i.lower() == word.lower():
            count+=1
    return count
    

    
#Making Features    

##How to convert UTF-8 to string type
#title = u"Klüft skräms inför på fédéral électoral große"
#import unicodedata
#title = unicodedata.normalize('NFKD', title).encode('ascii','ignore')



##Feature 1: Message length 
##Column 2
dataUF['MessageLength'] = 0
for i in range(5572):
    dataUF.iloc[i, 2] = len(dataUF.iloc[i, 0])
    
##Feature 2: Frequency of the letter 'I'. Spams don't generally convey messages in first person
##Column 3
dataUF['FreqOf:I:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freqI = countFreq(message, 'I')
    dataUF.iloc[i, 3] = freqI


##Feature 3: Frequency of the word 'Free'. Usually a lot of spam has these weird 'free' offers
##Column 4
dataUF['FreqOf:FREE:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'FREE')
    dataUF.iloc[i, 4] = freq
    
##Feature 4: Frequency of the word 'Love'
##Column 5
dataUF['FreqOf:LOVE:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'LOVE')
    dataUF.iloc[i, 5] = freq

##Feature 5: Frequency of the word 'You'
##Column 6
dataUF['FreqOf:YOU:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'YOU')
    dataUF.iloc[i, 6] = freq
               

##Feature 6: Frequency of the word 'Offer'
##Column 7
dataUF['FreqOf:OFFER:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'OFFER')
    dataUF.iloc[i, 7] = freq
              


#dataUF.drop(['FreqOf:MY:'], axis=1, inplace=True)


##Feature 8: Frequency of the word 'Extra'
##Column 9
dataUF['FreqOf:EXTRA:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'extra')
    dataUF.iloc[i, 8] = freq



##Feature 8: Frequency of the word 'Chances'
##Column 9
dataUF['FreqOf:CHANCES:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Chances')
    dataUF.iloc[i, 9] = freq


##Feature 9: Frequency of the word 'Save'
##Column 10
dataUF['FreqOf:SAVE:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Save')
    dataUF.iloc[i, 10] = freq
               
               

##Feature 10: Frequency of the word 'CONGRATULATIONS'
##Column 11
dataUF['FreqOf:CONGRATULATIONS:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'CONGRATULATIONS')
    dataUF.iloc[i, 11] = freq
               
               
##Feature 11: Frequency of the word 'LOL'
##Column 12
dataUF['FreqOf:LOL:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'LOL')
    dataUF.iloc[i, 12] = freq
               
               
##Feature 12: Frequency of the word 'ROFL'
##Column 13
dataUF['FreqOf:ROFL:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'ROFL')
    dataUF.iloc[i, 13] = freq
               

##Feature 13: Frequency of the word 'Special'
##Column 14
dataUF['FreqOf:SPECIAL:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Special')
    dataUF.iloc[i, 14] = freq
               
               
##Feature 14: Frequency of the word 'Prize'
##Column 15
dataUF['FreqOf:PRIZE:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Prize')
    dataUF.iloc[i, 15] = freq
               
               
##Feature 15: Frequency of the word 'Text'
##Column 16
dataUF['FreqOf:TEXT:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Text')
    dataUF.iloc[i, 16] = freq
               
               
               
##Feature 16: Frequency of the word 'Reply'
##Column 17
dataUF['FreqOf:REPLY:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Reply')
    dataUF.iloc[i, 17] = freq
               

##Feature 17: Frequency of the word 'Send'
##Column 18
dataUF['FreqOf:SEND:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Send')
    dataUF.iloc[i, 18] = freq
               
               
##Feature 18: Frequency of the word 'Will'
##Column 19
dataUF['FreqOf:WILL:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Will')
    dataUF.iloc[i, 19] = freq
               
               
##Feature 19: Frequency of the word 'Now'
##Column 20
dataUF['FreqOf:NOW:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Now')
    dataUF.iloc[i, 20] = freq
               
               
##Feature 20: Frequency of the word 'Call'
##Column 21
dataUF['FreqOf:CALL:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Call')
    dataUF.iloc[i, 21] = freq


##Feature 21: Frequency of the word 'Customer'
##Column 22
dataUF['FreqOf:CUSTOMER:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Customer')
    dataUF.iloc[i, 22] = freq
               

##Feature 22: Frequency of the word 'Service'
##Column 23
dataUF['FreqOf:SERVICE:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'Service')
    dataUF.iloc[i, 23] = freq               
               
               

##Feature 23: Frequency of the word 'Hi'
##Column 24
dataUF['FreqOf:HI:'] = 0

for i in range(5572):
    message = (dataUF.iloc[i, 0])
    message = unicodedata.normalize('NFKD', message).encode('ascii','ignore')
    freq = countFreq(message, 'HI')
    dataUF.iloc[i, 24] = freq 
               
               
               
x = dataUF.iloc[:, 2:25].values
y = dataUF.iloc[:, 1:2].values

from sklearn.preprocessing import LabelEncoder
scY = LabelEncoder()
y = scY.fit_transform(y)

from sklearn.cross_validation import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x,y,test_size=0.1,random_state=0)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)             #Best at 5 right now.
knn.fit(xTrain, yTrain)
yPred = knn.predict(xTest)

from sklearn.metrics import accuracy_score
score = accuracy_score(yPred, yTest)