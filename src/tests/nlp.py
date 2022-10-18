import numpy as np 
import pandas as pd 

# text processing libraries
import re
import string
import nltk
from nltk.corpus import stopwords

# sklearn 
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score
from sklearn import preprocessing, decomposition, model_selection, metrics, pipeline
from sklearn.model_selection import GridSearchCV,StratifiedKFold,RandomizedSearchCV

# matplotlib and seaborn for plotting
import matplotlib.pyplot as plt
import seaborn as sns

# File system manangement
import os

#Training data
train = pd.read_csv('songs.csv')
print('Training data shape: ', train.shape)
train.head()

#Missing values in training set
print(train.isnull().sum())

print(train['Lyrics'].value_counts())

sns.barplot(y=train['Lyrics'].value_counts()[:20].index,x=train['Lyrics'].value_counts()[:20], orient='h')