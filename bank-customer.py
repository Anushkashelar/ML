import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Churn_Modelling.csv")

df.head()

df.shape

df.describe()


df.isnull()

df.isnull().sum()

df.info()

df.dtypes

df.columns

df = df.drop(['RowNumber', 'Surname', 'CustomerId'], axis= 1)

df.head()

def visualization(x, y, xlabel):
 plt.figure(figsize=(10,5))
 plt.hist([x, y], color=['red', 'green'], label = ['exit', 'not_exit'])
 plt.xlabel(xlabel,fontsize=20)
 plt.ylabel("No. of customers", fontsize=20)
 plt.legend()


df_churn_exited = df[df['Exited']==1]['Tenure']
df_churn_not_exited = df[df['Exited']==0]['Tenure']


visualization(df_churn_exited, df_churn_not_exited, "Tenure")


df_churn_exited2 = df[df['Exited']==1]['Age']
df_churn_not_exited2 = df[df['Exited']==0]['Age']


visualization(df_churn_exited2, df_churn_not_exited2, "Age")


X = df[['CreditScore','Gender','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalar
y']]
states = pd.get_dummies(df['Geography'],drop_first = True)
gender = pd.get_dummies(df['Gender'],drop_first = True)


df = pd.concat([df,gender,states], axis = 1)


df.head()

X = df[['CreditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary','Male'
,'Germany','Spain']]


y = df['Exited']


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.30)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()


X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


X_train

X_test

import keras 


from keras.models import Sequential #To create sequential neural network
from keras.layers import Dense

classifier = Sequential()


classifier.add(Dense(activation = "relu",input_dim = 11,units = 6,kernel_initializer = "uniform"))


classifier.add(Dense(activation = "relu",units = 6,kernel_initializer = "uniform"))


classifier.add(Dense(activation = "sigmoid",units = 1,kernel_initializer = "uniform"))

classifier.compile(optimizer="adam",loss = 'binary_crossentropy',metrics = ['accuracy'])


classifier.summary() 


classifier.fit(X_train,y_train,batch_size=10,epochs=50)

y_pred =classifier.predict(X_test)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report


cm = confusion_matrix(y_test,y_pred)

cm


accuracy = accuracy_score(y_test,y_pred)

accuracy


plt.figure(figsize = (10,7))
sns.heatmap(cm,annot = True)
plt.xlabel('Predicted')
plt.ylabel('Truth')



print(classification_report(y_test,y_pred))

