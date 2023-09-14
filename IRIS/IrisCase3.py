from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance


def euc(a,b):
    return distance.euclidean(a,b)


class MarvellousKNeighborsCassifier():
    def fit(self,trainingdata,trainingtarget):
        self.TrainingData=trainingdata
        self.TrainingTarget=trainingtarget

    def predict(self,TestData):
        predictions=[]
        for value in TestData:
            result=self.closest(value)
            predictions.append(result) 
        
        return predictions

    def closest(self,row):
        minimumdistance=euc(row,self.TrainingData[0])
        minimumindex=0


        for i in range(1,len(self.TrainingData)):
            Distnce=euc(row,self.TrainingData[i])
            if Distnce<minimumdistance:
                minimumdistance=Distnce
                minimumindex=i

        return self.TrainingTarget[minimumindex]
    
    


def MarvellousML():
    Dataset=load_iris()      #1 load the data

    Data = Dataset.data
    Target=Dataset.target

    #2:manipulate the data
    Data_train,Data_test, Target_train,Target_test=train_test_split(Data,Target,test_size=0.5)   #divide the data in four set

    Classifier=MarvellousKNeighborsCassifier()

    #3:Bulid the model
    Classifier.fit(Data_train,Target_train)

    #4:test the model
    predictions=Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test,predictions)

    #5:Improve---Missing

    return Accuracy

    

def main():
   Ret= MarvellousML()

   print("Accuracy of iris dataset with DecisionTreeClassifier4 is:",Ret*100)
   

if __name__ =="__main__":
    main()