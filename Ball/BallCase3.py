#Import Required data set
from sklearn import tree

#load the dataset
#Rough 1
#Smooth 0
#Tennis  1
#Cricket 2

def BallPredictor():

    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    #decide the machine learing algorith
    obj=tree.DecisionTreeClassifier()

    #perform the trainning of model
    obj=obj.fit(Features,Labels)

    #perform the testing
    print(obj.predict([[97,0]]))


def main():
    print("-------------Ball predictor case study--------------")
    
    BallPredictor()

if __name__ =="__main__":
    main()