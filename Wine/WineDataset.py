from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def WinePredictor():
    wine=datasets.load_wine()

    X_train,X_test,y_train,y_test=train_test_split(wine.data,wine.target,test_size=0.3)

    knn=KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train,y_train)

    y_pred=knn.predict(X_test)

    print("Accuracy",100*metrics.accuracy_score(y_test,y_pred))


def main():
    WinePredictor()

if __name__=="__main__":
    main()

