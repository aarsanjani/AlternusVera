"""
Created on Tue Nov 18 16:54:40 2018

@author: gpandey
"""

#http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/smsSpamCollection.arff
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle as pkl    
import pandas as pd

messages = pd.read_csv('dataset/SMSSpamCollection', sep='\t',
                           names=["label", "message"])
messages.head()
messages.describe()
messages.groupby('label').describe()

messages['length'] = messages['message'].apply(len)
messages.head()

import string
from nltk.corpus import stopwords
# text preprocessing
def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

#NLP Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])

from sklearn.model_selection import train_test_split
msg_train, msg_test, label_train, label_test = \
train_test_split(messages['message'], messages['label'], test_size=0.2)
print(len(msg_train), len(msg_test), len(msg_train) + len(msg_test))

pipeline.fit(msg_train,label_train)

predictions = pipeline.predict(msg_test.head()) # predict cat
conf = pipeline.predict_proba(msg_test.head()) # predicting confidence
conf
predictions
from sklearn.metrics import classification_report
print(classification_report(predictions,label_test))
predictions
df = pd.read_csv('dataset/fake_real_dataset.csv')
#df['content'] = df['title'] + df['text']
import seaborn as sns
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')

def combine_column(tuple1):
    if(pd.notna(tuple1[1])):
        if(tuple1[1].strip(' \t\n\r') == ''):
            return 'NA spam'
        else:
            return tuple1[1]
    elif(pd.notna(tuple1[0])):
        if(tuple1[0].strip(' \t\n\r') == ''):
            return 'NA spam'
        else:
            return tuple1[0]   
    else:
            return 'NA spam'
       
#df.describe() 
#df['content'].describe() 
    #print(text)
df['content'] = df[['title', 'text']].apply(combine_column, axis=1)
#df['content1'] = df[['title', 'text']].apply(lambda x: ' '.join(x), axis=1)
df.head()
#dataset.shape()
output1 = pipeline.predict_proba(df['content'])

df['spam-score'] = output1[:,0]

df.to_csv('dataset/fake_real_dataset_spam.csv')