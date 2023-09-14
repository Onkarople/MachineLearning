import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def Random_():

    dataset=load_iris()

    Data=dataset.data
    Target=dataset.target

    X_train,X_test,Y_train,Y_test=train_test_split(Data,Target,test_size=0.3)
    
    Rf=RandomForestClassifier()

    Rf.fit(X_train,Y_train)

    print(Rf.score(X_train,Y_train))

    predict=Rf.predict(X_test)

    Accuracy=accuracy_score(Y_test,predict)

    print(Accuracy)


def main():
    Random_()


if __name__ == "__main__":
    main()


