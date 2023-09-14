import pandas as pd

data = [[35,1,1],[47,1,1],[90,0,2],[48,1,1],[90,0,2],[35,1,1],[92,0,2],[35,1,1],[35,1,1],[35,1,1],[96,0,2],[43,1,1],[110,0,2],[35,1,1],[95,0,2]]

df=pd.DataFrame(data,columns=['Wight','Surface','Type'])

print(df)

df.to_csv('marvellous.csv')