from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def MarvellousKNeighborsCassifier(data_path):
    Dataset=pd.read_csv(data_path,index_col=0)     #1 load the data
    df=pd.DataFrame(Dataset,columns=['Whether','Temperature','Play'])

    def Encoder(df):
        columnsToEncode=list(df.select_dtypes(include=['category','object']))
        le=LabelEncoder()
        for feature in columnsToEncode:
            try:
                df[feature]=le.fit_transform(df[feature])
            except:
                print("Error Encoding"+feature)
        return df
    
    df=Encoder(df)
    data=df[["Whether","Temperature"]]
    target=df[["Play"]]


    Classifier=KNeighborsClassifier(n_neighbors=3)

    #3:Bulid the model
    Classifier.fit(data,target)

    #4:test the model
    predictions=Classifier.predict([[1,0]])

    print(predictions)

    if predictions:
        print("you can play")
    else:
        print("No play")

    #Accuracy = accuracy_score(target,predictions)

    #5:Improve---Missing

    #return Accuracy

    

def main():
   Ret= MarvellousKNeighborsCassifier(r"C:\Users\Onkar Ople\Desktop\PlayPredictor.csv")

   #print("Accuracy of iris dataset with KNN is:",Ret*100)
   

if __name__ =="__main__":
    main()