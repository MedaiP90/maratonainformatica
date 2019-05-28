from joblib import load
from sklearn.linear_model import LinearRegression

import pandas as pd

# load model
regressor = load('ml/models/model.joblib')

# create dataset for predictions
d = {'yearb': [1818, 2019, 1955, 1900, 1994, 1998], 'vocab': [2, 8, 6, 4, 9, 7]}
df = pd.DataFrame(data=d)
X = df[['yearb', 'vocab']].values

# predict
y_pred = regressor.predict(X)

# print values
for i in y_pred:
    print(i)
