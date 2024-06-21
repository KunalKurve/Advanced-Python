# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:51:10 2024

@author: Administrator
"""

import pandas as pd
dummy_data1 = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}

df1 = pd.DataFrame(dummy_data1, columns = ['id', 'Feature1', 'Feature2']) 

dummy_data2 = {
        'id': ['1', '2', '6', '7', '8'],
        'Feature1': ['K', 'M', 'O', 'Q', 'S'],
        'Feature2': ['L', 'N', 'P', 'R', 'T']}
df2 = pd.DataFrame(dummy_data2, columns = ['id', 'Feature1', 'Feature2'])

df1['city']='Pune'
df2['city']="mumbai"


#combining two or more dataframes using concat functions
df3=pd.concat([df1,df2],ignore_index=True)
print(df3.loc[0])
dummy_data3 = {
        'id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'Feature3': [12, 13, 14, 15, 16, 17, 15, 12, 13, 23]}
df4 = pd.DataFrame(dummy_data3, columns = ['id', 'Feature3'])
df5=pd.merge(df3,df4,on="id",how="right")
# df5=pd.merge(df3,df4,left_on="id",right_on="id",how="outer")


df5.loc[len(df5.index)]=['12','S','X','Pune','15']
d={'id':12,'Feature1':'S1','Feature2':'x2','city':'YYY','Feature3':'45'}
df5=df5.append(d,ignore_index=True)