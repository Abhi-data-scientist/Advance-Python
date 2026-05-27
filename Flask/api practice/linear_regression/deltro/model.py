import numpy as np 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('insurance - insurance.csv')

le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['smoker'] = le.fit_transform(df['smoker'])
df['region'] = le.fit_transform(df['region'])

x = df.drop(columns=['charges'])
y = df['charges']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

lr = LinearRegression()

lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)

r2_score(y_pred, y_test)


import joblib 
joblib.dump(lr, 'lr_model.pkl')
print("Model saved as lr_model.pkl")