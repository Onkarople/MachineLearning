import numpy as np
import pandas as pd
from copy import deepcopy
from matplotlib import pyplot as plt


def MarvellousKMean():
    print(".________________________")
    # Set three centers, the model shou!
    center_1 = np.array([1,1])  
    print(center_1)
    print("_____________________________")
    center_2 = np.array([5,5])
    print(center_2)
    print("______________________________")
    center_3 = np.array([8,1])
    print(center_3)
    print("________________________________ ")

    # Generate random data and center it to the three centers
    data_1 = np.random.randn(7, 2) + center_1   
    print("Elements of first cluster with size"+str(len(data_1)))
    print(data_1)

    print("_______________________________________")

    data_2 = np.random.randn(7,2) + center_2
    print("Elements of second cluster with size"+str(len(data_2)))
    print(data_2)

    print("_______________________________________")

    data_3 = np.random.randn(7,2) + center_3

    print("Elements of third cluster with size"+str(len(data_3)))
    print(data_3)
    print("________________________________________")
    data = np.concatenate((data_1, data_2, data_3), axis = 0)
    print("Size of complete data set"+str(len(data)))
    print(data)
    print("__________________________________________ ")

    plt.scatter(data[:,0], data[:,1], s=7)
    plt.title('Marvellous Infosystems : Input Dataset')

    plt.show()

    print("_____________________________________________")
    # Number of clusters

    k=3

    #Number of training data

    n = data.shape[0]

    print("Total number of elements are",n)
    print("_______________________________")
    # Number of features in the data

    c = data.shape[1]

    print("Total number of features are",c)

    print("___________________________________")


   # Generate random centers, here we us epresent the whole data
    mean = np.mean(data, axis = 0)
    print("Value of mean",mean)
    print("_____________________")

    # Calculate standard deviation
    std = np.std(data, axis = 0)
    print("Value of std",std)
    print("_________________________")
    centers = np.random.randn(k,c)*std + mean
    print("Random points are",centers)
    print("______________________________________")

    # Plot the data and the centers generated as random
    plt.scatter(data[:,0], data[:,1],c='r', s=7)
    plt.scatter(centers[:,0], centers[:,1], marker='*', c='g', s=150)
    plt.title("Marvellous Infosystems : Input Datase with random centroid *")
    plt.show()
    print("_________________________________________________________")
    
    centers_old = np.zeros(centers.shape)
    centers_new = deepcopy(centers)

    print("Values of old centroids")
    print(centers_old)
    print("______________________________________")

    print("Values of new centroids")
    print(centers_new)
    print("____________________________")

    data.shape
    clusters = np.zeros(n)
    distances = np.zeros((n,k))

    print("Initial distances are")
    print(distances)
    print("_________________________________")

    error=np.linalg.norm(centers_new -centers_old)
    print("value of error is",error)

    while error!=0:
        print("Value of error is ",error)

        print("Measure the distance to every center")
        for i in range(k):
            print("Iteration number",i)
            distances[:,i]=np.linalg.norm(data -centers[i],axis=1)

        clusters=np.argmin(distances,axis=1)

        centers_old=deepcopy(centers_new)
 
        for i in range(k):
            centers_new[i]=np.mean(data[clusters==i],axis=0)
        error=np.linalg.norm(centers_new-centers_old)
    
    centers_new


    plt.scatter(data[:,0],data[:1],s=7)
    plt.scatter(centers_new[:,0],centers_new[:,1],marker='*',c='g',s=150)
    plt.title('Marvellous Infosystems: FInal data with Centroid')
    plt.show()


def main():
    print("")
    MarvellousKMean()


if __name__=="__main__":
    main()

       
 
 
 
 
  
 
 
 
