import pandas as pd
from xlsxwriter import workbook
data=[{'name':'PPA','Duration':3,'Fees':18000},{'name':'LB','Duration':2,'Fees':18300}]
df=pd.DataFrame(data)
print(df)


writer=pd.ExcelWriter('MarvellousPands.xlsx',engine='xlsxwriter')

df.to_excel(writer,sheet_name="sheet1")

writer.save()
