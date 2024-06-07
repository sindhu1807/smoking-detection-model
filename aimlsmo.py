# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
df=pd.read_csv('smoking.csv')
df.drop

df


df.drop(df.index[range(10000,50000)],inplace=True)
df

df.dropna(inplace=True)
df

df.drop(df.index[range(10000,15692)],inplace=True)
df

gen=df['gender']
from sklearn.preprocessing import LabelEncoder
enc=LabelEncoder()
df['gender']=enc.fit_transform(df.gender)
df.head()

df['oral']=enc.fit_transform(df.oral)
df['tartar']=enc.fit_transform(df.tartar)
df.head()

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
x=df.iloc[:10000,:-1]
y=df.iloc[:10000,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=2)
print(x_train.shape)
y_train.shape
x_test.shape 

mr=LinearRegression()
mr.fit(x_train,y_train)
print(mr.intercept_)
print(mr.coef_)
y_pred=mr.predict(x_test)
y_pred
comp=pd.DataFrame(y_test)
comp
from sklearn.metrics import mean_squared_error,r2_score
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print(mse)
print(r2)

import pickle
pickle.dump(mr, open('mr.pkl','wb'))

mr=pickle.load(open('mr.pkl','rb'))
print(mr.predict([[0.0,0.0,40.0,155.0,60.0,81.3,1.2,1.0,1.0,1.0,114.0,73.0,94.0,215.0,82.0,73.0,126.0,12.9,1.0,0.7,18.0,19.0,27.0,0.0,0.0,1.0]]))
print(df.columns.values)


