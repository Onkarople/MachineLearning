from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import requests
from io import StringIO

def MarvellousKNeighborsCassifier():
    url=r"https://drive.google.com/file/d/1MB9FRX5sI4opsp3wLiyyJ5KhPMT_Cika/view?usp=sharing"
    Dataset=pd.read_csv(url,na_values=['?'])     #1 load the data
    df=pd.DataFrame(Dataset,columns=['sepal.length','sepal.width','petal.length','petal.width','variety'])
    data=df[["sepal.length","sepal.width","petal.length","petal.width"]]
    target=df[["variety"]]

    #2:manipulate the data
    Data_train,Data_test, Target_train,Target_test=train_test_split(data,target,test_size=0.5)   #divide the data in four set

    Classifier=KNeighborsClassifier()

    #3:Bulid the model
    Classifier.fit(Data_train,Target_train)

    #4:test the model
    predictions=Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test,predictions)

    #5:Improve---Missing

    return Accuracy

    

def main():
   Ret= MarvellousKNeighborsCassifier()

   print("Accuracy of iris dataset with KNN is:",Ret*100)
   

if __name__ =="__main__":
    main()