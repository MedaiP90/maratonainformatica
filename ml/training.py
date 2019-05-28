import pandas as pd  
import numpy as np  

from sklearn.linear_model import LinearRegression
from sklearn import metrics
from joblib import dump

dataset = pd.read_csv('GSSvocab.csv', low_memory=False)
dataset['yearb'] = dataset['year'] - dataset['age']
dataset = dataset.dropna(axis=0)

X = dataset[['yearb', 'vocab']].values # features
y = dataset['educ'].values # labels

# create the model
regressor = LinearRegression()  
regressor.fit(X, y)

# export the model for further use
dump(regressor, 'models/model.joblib')
