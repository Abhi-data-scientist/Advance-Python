import numpy as np 
import pandas as pd 

df = pd.read_csv('Churn_Modelling - Churn_Modelling.csv')

df = df.drop(columns=['RowNumber', 'CustomerId', 'Surname'])


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Geography'] = le.fit_transform(df['Geography'])
df['Gender'] = le.fit_transform(df['Gender'])

x = df.drop(columns=['Exited'])
y  = df['Exited']
print(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.20)

from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
x_train_smote, y_train_smote = smote.fit_resample(x_train, y_train)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train_smote, y_train_smote)

y_pred = lr.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

print('Accuracy is : ', accuracy)

import joblib
joblib.dump(lr, 'lr_model.pkl')
print('Logistic model is saved as lr_model.pkl')