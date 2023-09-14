import pandas as pd
import numpy as np

df1={'one':pd.Series([1,2],index=['a','b'])}

df2={'two':pd.Series([1,2],index=['a','b'])}

data={'item1':df1,"item2":df2}

p=pd.Panel(data)

print(p)