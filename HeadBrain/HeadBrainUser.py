import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousHeadBrainPredictor():
    #load data
    data=pd.read_csv('MarvellousHeadBrain.csv')

    print("Size if data set",data.shape)

    X=data["Head Size(cm^3)"].values
    Y=data["Brain Weight(grams)"].values

    #Least Sqaure method
    mean_x=np.mean(X)
    mean_y=np.mean(Y)

    n=len(X)

    numrator=0
    denomentor=0

    #Equation of line is y =mx +c

    for i in range(n):
        numrator+=(X[i]-mean_x)*(Y[i]-mean_y)
        denomentor+=(X[i]-mean_x)**2
    
    m=numrator/denomentor

    c=mean_y-(m*mean_x)

    print("Slope of regreesion line is",m)
    print("Y intercept of regreesion line is",c)

    max_x=np.max(X)+100
    min_x=np.min(X)-100

    #Dsiplay plotting of above points
    x=np.linspace(min_x,max_x,n)

    y=c+m*x

    plt.plot(x,y,color='#58b970',label='Regression line')

    plt.scatter(X,Y,color='#ef5423',label='scatter plot')

    plt.xlabel('Head size in cm3')

    plt.ylabel('Brain weight in gram')

    plt.legend()
    plt.show()

    #findout goodness of fit is R Sqaure
    ss_t=0
    ss_r=0

    for i in range(n):
        Y_pred=c+m*X[i]
        ss_t+=(Y[i]-mean_y)**2
        ss_r+=(Y[i]-Y_pred)**2
    
    r2=1-(ss_r/ss_t)

    print(r2)

def main():
    print("----Marvellous Infosystems ----")

    print("Head Brain Dataset")

    MarvellousHeadBrainPredictor()

if __name__=="__main__":
    main()