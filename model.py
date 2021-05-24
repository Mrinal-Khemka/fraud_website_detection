from enum import auto
import numpy as np
import pandas as pd
import sklearn
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
data=pd.read_csv("final.csv")
# data.plot(kind="hist",subplots=True,layout=(5,5),sharex=False)
# plt.show()
# print(data.describe())
# names=list(data.columns)
# correlation=data.corr()
# fig = plt.figure()
# ax = fig.add_subplot(111)
# cax = ax.matshow(correlation, vmin=-1, vmax=1)
# fig.colorbar(cax)
# ticks = np.arange(0,18,1)
# ax.set_xticks(ticks)
# ax.set_yticks(ticks)
# ax.set_xticklabels(names)
# ax.set_yticklabels(names)
# plt.show()
#shuffling dataset to get a better result
data=data.sample(frac=1).reset_index(drop=True)
#spliting  independent and dependent variable
X=np.array(data.iloc[:,1:-1])
Y=np.array(data.iloc[:,-1:])
#generating examples for training and testing of model
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=12)
# creating model using decisiontree
# model=DecisionTreeClassifier(max_depth=6);
# model.fit(x_train,y_train)
# y_pre=model.predict(x_train)
# print(accuracy_score(y_train,y_pre))
#creating model using randomforest(ensemble learning)
model=RandomForestClassifier(max_depth=20)
y_train=y_train.ravel()
model.fit(x_train,y_train)
y_pre=model.predict(x_test)
print(accuracy_score(y_test,y_pre))
# creating model using svm
# svm = SVC(kernel='rbf', C=1e10, random_state=12)
# svm.fit(x_train,y_train)
# y_pre=svm.predict(x_test)
# print(accuracy_score(y_test,y_pre))
def getPrediction(x):
    np_x=np.array(x).reshape(1,-1)
    return model.predict(np_x)
