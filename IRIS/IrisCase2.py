from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def MarvellousDecisionTreeClassifier():
    Dataset=load_iris()      #1 load the data

    Data = Dataset.data
    Target=Dataset.target

    #2:manipulate the data
    Data_train,Data_test, Target_train,Target_test=train_test_split(Data,Target,test_size=0.5)   #divide the data in four set

    Classifier=DecisionTreeClassifier()

    #3:Bulid the model
    Classifier.fit(Data_train,Target_train)

    #4:test the model
    predictions=Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test,predictions)

    #5:Improve---Missing

    return Accuracy

    

def main():
   Ret= MarvellousDecisionTreeClassifier()

   print("Accuracy of iris dataset with DecisionTreeClassifier4 is:",Ret*100)
   

if __name__ =="__main__":
    main()