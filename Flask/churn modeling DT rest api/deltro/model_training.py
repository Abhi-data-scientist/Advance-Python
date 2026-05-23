import numpy as np 
import pandas as pd 

df = pd.read_csv('Churn_Modelling - Churn_Modelling.csv')


df.drop(columns=['RowNumber', 'CustomerId', 'Surname'], inplace = True)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Geography'] = le.fit_transform(df['Geography'])
df['Gender'] = le.fit_transform(df['Gender'])

x = df.drop(columns = ['Exited'])
y = df['Exited'] 

from sklearn.model_selection import train_test_split 
x_train, x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier() 
dt.fit(x_train , y_train) 

import joblib 

# Save the model
joblib.dump(dt, 'dt_model.pkl')
print("Model saved as dt_model.pkl")