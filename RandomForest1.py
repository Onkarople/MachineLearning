import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier,RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


def Ense():

    dataset=load_iris()

    Data=dataset.data
    Target=dataset.target

    X_train,X_test,y_train,y_test=train_test_split(Data,Target,test_size=0.3,random_state=42)

    Kn=KNeighborsClassifier(n_neighbors=3)
    Dt=DecisionTreeClassifier(max_depth=3)
    Rn=RandomForestClassifier(n_estimators=20)

    vot=VotingClassifier(estimators=[('kn',Kn),('dt',Dt),('rn',Rn)],voting='soft')

    vot.fit(X_train,y_train)

    predict=vot.predict(X_test)

    Accuracy=accuracy_score(y_test,predict)

    print(Accuracy)


def main():
    Ense()

if __name__ == "__main__":
    main()