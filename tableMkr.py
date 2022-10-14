import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import numpy as np


def add_table(df, psqltable):
    # Create and connect the sqlalchemy engine
    engine = create_engine("postgresql://postgres:123@localhost:5432/datosCulturaArg", echo=True, future=True)
    psqlcon = engine.connect()
    try:
        # Transform the dataframe to our sql table
        df.to_sql(name=psqltable, con=psqlcon, index=False)
        # Then .commit our connection so it doesn't rollback
        psqlcon.commit()
    # In case of error or exceptions print it out
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

