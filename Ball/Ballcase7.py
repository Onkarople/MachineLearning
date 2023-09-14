#Import Required data set
from sklearn import tree
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#load the dataset
#Rough 1
#Smooth 0
#Tennis  1
#Cricket 2

def BallPredictor(wight,surface):

    data=pd.read_csv('marvellous.csv',index_col=0)

    features_names=['Wight','Surface']

    Weight=data.Wight
    Surface=data.Surface
    type=data.Type

    features=list(zip(Weight,Surface))

    #decide the machine learing algorith
    obj=tree.DecisionTreeClassifier()

    #perform the trainning of model
    obj=obj.fit(features,type)

    #perform the testing
    Ret=obj.predict([[wight,surface]])

    if Ret == 1 :
        print("Your object looks like tennis ball")
    else:
        print("object looks like cricket ball")


def main():
    print("-------------Ball predictor case study--------------")
    
    print("Please enter the weight of your object in grams")
    weight=int(input())

    print("please enter the type of surface of your object (Rough/Smooth) ")
    surface=input()

    if surface.lower()=="rough":
        surface=1
    elif surface.lower()=="smooth":
        surface=0
    else:
        print("Invalid type of surface")
        exit()
    

    BallPredictor(weight,surface)

if __name__ =="__main__":
    main()