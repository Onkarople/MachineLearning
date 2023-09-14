from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics


def MarvellousSVM():

    #load datasets
    cancer=datasets.load_breast_cancer()

    print("Features od the cancer dataset:",cancer.feature_names)

    print("Labels of the cancer dataset:",cancer.target_names)

    print("Shape of dataset is :",cancer.data.shape)

    print("Firs 5 records are :")
    print(cancer.data[0:5])


    print("Target of dataset :",cancer.target)

    X_train,X_test,y_train,y_test=train_test_split(cancer.data,cancer.target,test_size=0.3,random_state=109)

    clf=svm.SVC(kernel='linear')

    clf.fit(X_train,y_train)

    y_pred=clf.predict(X_test)

    print("Accuracy of the model is ",metrics.accuracy_score(y_test,y_pred)*100)



def main():
    print("________Support vector Machine__________")

    MarvellousSVM()


if __name__ == "__main__":
    main()