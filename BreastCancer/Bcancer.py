


#Required Python Packages

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# File Paths

INPUT_PATH = "breast-cancer-wisconsin.data"
OUTPUT_PATH = "breast-cancer-wisconsin.csv"

  
# Headers

HEADERS = ["CodeNumber", "ClumpThickness","UniformityCellSize", "UniformityCellShape", "MarginalAdhesion","SingleEpithelialCellSize","BareNuclei", "BlandChromatin", "NormalNucleoli", "Mitoses", "CancerType"]





def read_data(path):
    data=pd.read_csv(path)
    return data


def get_headers(datset):
    return datset.columns.values


def add_headers(dataset,headers):
    dataset.columns=headers
    return dataset

def data_file_to_csv():
    headers= ["CodeNumber", "ClumpThickness","UniformityCellSize", "UniformityCellShape", "MarginalAdhesion","SingleEpithelialCellSize","BareNuclei", "BlandChromatin", "NormalNucleoli", "Mitoses", "CancerType"]

    dataset=read_data(INPUT_PATH)

    dataset=add_headers(dataset,headers)

    dataset.to_csv(OUTPUT_PATH,index=False)

    print("File saved...!")


def split_dataset(dataset,train_percentage,feature_headers,target_header):
    train_x,test_x_,train_y,test_y=train_test_split(dataset[feature_headers],dataset[target_header],train_size=train_percentage)

    return train_x,test_x_,train_y,test_y


def handel_missing_values(dataset,missing_values_header,missing_label):
    return dataset[dataset[missing_values_header]!=missing_label]



def random_forest_classifier(features,target):
    clf=RandomForestClassifier()
    clf.fit(features,target)
    return clf

def dataset_statistics(dataset):
    print(dataset.describe())
    



def main():

    dataset=pd.read_csv(OUTPUT_PATH)

    dataset_statistics(dataset)


    dataset=handel_missing_values(dataset,HEADERS[6],'?')

    train_x,test_x,train_y,test_y=split_dataset(dataset,0.7,HEADERS[1:1],HEADERS[-1])

    print("train_x shape::",train_x.shape)


    trained_model=random_forest_classifier(train_x,train_y)
    print("trained model::",trained_model)

    predictions=trained_model.predict(test_x)

    for i in range(0,205):
        print("Actual outcome :: {} and Predicted outcome::{}".format(list(test_y[i],predictions[i])))
    
    print("Train Accuracy::",accuracy_score(train_y,trained_model.predict(train_x)))
    print("Test Accuracy ::",accuracy_score(test_y,predictions))
    print("Confusion matrix",confusion_matrix(test_y,predictions))




if __name__=="__main__":
    main()