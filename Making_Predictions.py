#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn import metrics
import joblib


# In[2]:


##Step1: Load Dataset

dataframe = pd.read_csv("csv/dataset.csv")
#print(dataframe.head())
dataframe.info()
print(dataframe.head())


# In[3]:


#Step2: Split into training and test data
y = dataframe["Label"]
x = dataframe.drop(["Label"],axis=1)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# In[4]:


print(y)
print(x.info())


# In[5]:


##Step3: Build a model

model = RandomForestClassifier(n_estimators=100,max_depth=5)
model.fit(x_train,y_train)
joblib.dump(model,"rf_malaria_100_5")


# In[6]:


##Step4: Make predictions and get classification report

predictions = model.predict(x_test)

print(metrics.classification_report(predictions,y_test))
print(model.score(x_test,y_test))


# In[ ]:




