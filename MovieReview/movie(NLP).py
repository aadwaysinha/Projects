import pandas as pd
import numpy as np

dataset = pd.read_csv('movie.csv')

x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 0:1]

from sklearn.preprocessing import LabelEncoder
labelEncoderX = LabelEncoder()
dataset.iloc[:, 0] = labelEncoderX.fit_transform(dataset.iloc[:, 0])

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []

for i in range(0,2000):
    review = re.sub('[^a-zA-Z]', ' ', dataset.iloc[i, 1])
    review = review.lower()
    review = review.split()
    #ps = PorterStemmer()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
import pickle 
pickle_out = open('MoviePickleFileWithoutStemmer.pickle', 'wb')
pickle.dump(corpus, pickle_out)
pickle_out.close()    
    
scores = []  
  
for j in range(700, 900):
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(corpus).toarray()

from sklearn.cross_validation import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x,y,test_size=0.1,random_state=2) 

#Best accuracy = 77% 
#Max features = 1500 without stemming and test size being 10% at random state 2

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(xTrain, yTrain)

#from sklearn.neighbors import KNeighborsClassifier
#classifierKNN = KNeighborsClassifier(n_neighbors=5)
#classifierKNN.fit(xTrain, yTrain)
#yPred2 = classifierKNN.predict(xTest)

yPred = classifier.predict(xTest)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(yTest, yPred)

scores.append(classifier.score(xTest,yTest))

scores.sort(reverse=True)