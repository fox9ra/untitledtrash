import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
 
df = pd.read_excel('test2.xlsx', sheetname='Данные2')
 
print("Column headings:")
print(df.columns)
print(df['Unnamed: 5'])
