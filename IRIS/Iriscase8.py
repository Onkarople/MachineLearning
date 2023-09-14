from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt



def MarvellousKNeighborsCassifier():
    Dataset=pd.read_csv(r"C:\Users\Onkar Ople\Desktop\iris.csv")     #1 load the data
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

   

    df=pd.DataFrame(Dataset,columns=['sepal.length','sepal.width','petal.length','petal.width','variety'])
    df.plot(x='variety',y=['sepal.length','sepal.width','petal.length','petal.width'],kind="bar",colormap="winter")
    plt.show()
    plt.close()


    return Accuracy
    

def main():
   Ret= MarvellousKNeighborsCassifier()

   print("Accuracy of iris dataset with KNN is:",Ret*100)
   

if __name__ =="__main__":
    main()