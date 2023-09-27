# -*- coding: utf-8 -*-
"""Fake News Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A9IhWHDAlrKFy81CWsUPNIX-K9HZgV3_#scrollTo=YrN_6lqAamPc

# Fake News Detection

### Dataset:
We'll call the dataset we'll utilise for this project news.csv. The shape of this dataset is 77964. The news is identified in the first column, the title and content are in the second and third columns, and the news's authenticity is indicated in the fourth column.

## Prerequisites

Need to install the following libraries with pip
"""

!pip install numpy pandas sklearn

"""Necessary imports"""

import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

"""Now, let’s read the data into a DataFrame, and get the shape of the data and the first 5 records"""

#Read the data
df=pd.read_csv('news.csv')

#Get shape and head
df.shape
df.head()

"""And get the labels from the DataFrame."""

#DataFlair - Get the labels
labels=df.label
labels.head()

"""Split the dataset into training and testing sets."""

#DataFlair - Split the dataset
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)

"""Initialize a TfidfVectorizer with stop words from the English language and a maximum document frequency of 0.7 (terms with a higher document frequency will be discarded). Stop words are the most common words in a language that are to be filtered out before processing the natural language data. And a TfidfVectorizer turns a collection of raw documents into a matrix of TF-IDF features.

Now, fit and transform the vectorizer on the train set, and transform the vectorizer on the test set.
"""

#DataFlair - Initialize a TfidfVectorizer
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

#DataFlair - Fit and transform train set, transform test set
tfidf_train=tfidf_vectorizer.fit_transform(x_train)
tfidf_test=tfidf_vectorizer.transform(x_test)

"""Next, we’ll initialize a PassiveAggressiveClassifier. This is. We’ll fit this on tfidf_train and y_train.

Then, we’ll predict on the test set from the TfidfVectorizer and calculate the accuracy with accuracy_score() from sklearn.metrics.
"""

#DataFlair - Initialize a PassiveAggressiveClassifier
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

#DataFlair - Predict on the test set and calculate accuracy
y_pred=pac.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

"""We got an accuracy of 93.37% with this model. Finally, let’s print out a confusion matrix to gain insight into the number of false and true negatives and positives."""

#DataFlair - Build confusion matrix
confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])

"""So with this model, we have 589 true positives, 587 true negatives, 42 false positives, and 49 false negatives.

# Conclusion

We started with a political dataset, a TfidfVectorizer, a PassiveAggressiveClassifier, and fitted our model. In the end, we were able to achieve an accuracy of 93.37%."""
