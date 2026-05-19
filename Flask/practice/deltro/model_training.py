import numpy as np 
import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


df = pd.read_csv('tips - tips.csv')
print(df.head(3))

df.drop(columns=['day', 'size'], inplace=True)

le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['smoker'] = le.fit_transform(df['smoker'])
df['time'] = le.fit_transform(df['time']) 

x = df.drop(columns=['smoker'])
y = df['smoker']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

print(df['smoker'].value_counts())

smote = SMOTE(random_state=42)
x_train_balanced, y_train_balanced = smote.fit_resample(x_train, y_train)
# print("Before SMOTE:", Counter(y_train))
# print("After SMOTE:", Counter(y_train_balanced))

sc = StandardScaler()
x_train_balanced_scaled = sc.fit_transform(x_train_balanced)
x_test_scaled = sc.transform(x_test)

lr = LogisticRegression()
lr.fit(x_train_balanced_scaled, y_train_balanced)

# y_pred = lr.predict(x_test_scaled)

# print(accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))

import joblib 
joblib.dump(lr, 'lr_model.pkl')
print('model saved as lr_model.pkl')


