#Import Required data set
from sklearn import tree

#load the dataset
Features = [[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],[35,"Rough"],[92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"],[95,"Smooth"]]
Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket","Tennis","Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]

#decide the machine learing algorith
obj=tree.DecisionTreeClassifier()

#perform the trainning of model
obj=obj.fit(Features,Labels)

#perform the testing
print(obj.predict([[97,"Smooth"]]))

