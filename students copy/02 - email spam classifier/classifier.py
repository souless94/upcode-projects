import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            
            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message
            
def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)
        
    return DataFrame(rows, index=index)

data = DataFrame({'message': [], 'class': []})

data = data.append(dataFrameFromDirectory(r'C:\Users\wen kai\Downloads\y4s1\upcode-python\upcode-python-flask\students copy\02 - email spam classifier\emails\spam', 'spam'))
data = data.append(dataFrameFromDirectory(r'C:\Users\wen kai\Downloads\y4s1\upcode-python\upcode-python-flask\students copy\02 - email spam classifier\emails\ham', 'ham'))

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

import pickle
filename_classifier = 'classifier.sav'
filename_vectorizer = 'vectorizer.sav'

pickle.dump(classifier, open(filename_classifier, 'wb'))
pickle.dump(vectorizer, open(filename_vectorizer, 'wb'))
