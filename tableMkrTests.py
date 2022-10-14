import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
import numpy as np

df = pd.read_csv('C:/Users/thepo/Python_Scripts/pyProjects/alkemy/bibliotecas/2022-octubre/bibliotecas-12-10-2022.csv',skiprows=1)

print(type(df))

engine = create_engine("postgresql://postgres:123@localhost:5432/datosCulturaArg", echo=True, future=True)
psqlcon = engine.connect()
psqltable = 'tabla_bibliotecas'

Session = sessionmaker(engine)
session = Session()

try:
    df.to_sql(name=psqltable, con=psqlcon, index=False)
    psqlcon.commit()
except ValueError as vx:
    print(vx)
    print('----------------')
except Exception as ex:
    print(ex)
    print('***************')
else:
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
finally:
    psqlcon.close()

'''
# NOT IN USE
# Note - This was meant to download the csvs files from the previously provided websites.
# They got changed to a google sheets so I decided to use the google sheets API since it
# felt most appropriate. 
def downloader(name, url):
  r = requests.get(url)
  new_name = new_namer(name)
  with open(new_name + '.csv', 'wb') as f:
    f.write(r.content)
  return new_name
'''
