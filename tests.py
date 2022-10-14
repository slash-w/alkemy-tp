import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import numpy as np


df1 = pd.DataFrame({'id': [1,2,3,4,5], 
                    'pelicula': ['toy story', 'bichos', 'django', 'batman', 'joker'], 
                    'rating': [5,3,4,4,3]})

df2 = pd.DataFrame({'id': [1,2,3,4,5], 
                    'pelicula': ['busco nemo', 'hormigas', 'marvel', 'batman', 'batman'], 
                    'rating': [1,5,3,3,3], 
                    'ventas': [500,100,200,300,400]})

df3 = pd.DataFrame({'id': [1,2,3,4,5], 
                    'pelicula': ['Avatar', 'bichos', 'django', 'lego batman', 'joker'], 

                    'edad_minima': [18, 18, 15, 0, 5]})

df = pd.concat([df1, df2, df3])

data = pd.DataFrame({
    'id':[],
    'cant_pelis':[]})
data['id'] = pd.unique(df['id'])
arr = []
for i in data['id']:
    a = df[df['id'] == i]
    print(f'Pelis {i}: ', a)
    arr.append(len(pd.unique(a['pelicula'])))
#    print('array: ', arr)
    print('--------------------------------------------')


data['cant_pelis'] = arr
print(data)



#a = ((df1.columns.intersection(df2.columns)).intersection(df3.columns))
#newdf = df[a]
#print(newdf)
#df.columns = df.columns.str.lower()

#df = df.rename(columns = {'edad_minima':'edad_requerida'})
#print(df)