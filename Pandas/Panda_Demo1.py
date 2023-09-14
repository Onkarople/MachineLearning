import pandas as pd

print("Empty data frame")
df=pd.DataFrame()
print(df)


print("Dataframe with list")
data=[1,2,3,5]
df=pd.DataFrame(data)
print(df)

print("Dataframe with lsit")
data=[['PPA',3],['LB',5],['python',5]]
df=pd.DataFrame(data,columns=['Name','Duration'])
print(df)


data=[{'name':'PPA','Duration':3},{'name':'LB','Duration':2}]
df=pd.DataFrame(data)
print(df)


d={'one':pd.Series([1,2,3],index=['a','b','c'])}
df=pd.DataFrame(d)
print(df)