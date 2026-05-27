import numpy as np 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

df = pd.read_csv('insurance - insurance.csv')

le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['smoker'] = le.fit_transform(df['smoker'])
df['region'] = le.fit_transform(df['region'])

x = df.drop(columns=['charges'])
y = df['charges']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

rf = RandomForestRegressor()

rf.fit(x_train, y_train)

y_pred = rf.predict(x_test)

r2_score(y_pred, y_test)


import joblib 
joblib.dump(rf, 'rf_model.pkl')
print("Model saved as rf_model.pkl")