import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error

dataset_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')

#Separate target features (y) from input features (X)
y = data.quality
X = data.drop('quality', axis = 1)

#Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=23, stratify=y)

#Preprocessing
pipeline = make_pipeline(preprocessing.StandardScaler(), RandomForestRegressor(n_estimators=100))
hyperparameters = {'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'], 
                   'randomforestregressor__max_depth': [None, 5,3,1]}

#Tune model using cross-validation pipeline
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
clf.fit(X_train, y_train)

#Evaluate model pipeline on test data
pred = clf.predict(X_test)

mse = mean_squared_error(y_test, pred)
mae = mean_absolute_error(y_test, pred)

with open("metrics.txt", "a") as f:
    print("The Mean Squared Error is " + str(mse), file=f)
    print("The Mean Absolute Error is " + str(mae), file=f)