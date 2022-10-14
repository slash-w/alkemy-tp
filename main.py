import scrapper as scr
import tableMkr as tbmkr
import pandas as pd


def normalize(old_columns):
    new_columns = []
    for s in old_columns:
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        new_columns.append(s)
    return new_columns


def counter(df, par, find, index_):
    funiq = pd.unique(df[par])
    arr = []
    for i in funiq:
        arr.append(df.loc[(df[index_] == find) & (df[par] == i)].shape[0])

    return arr


def adder(df, par, index_):
  funiq = pd.unique(df[par])
  arr = []
  for i in funiq:
    a = df.loc[df[par] == i]
    sum = a.sum()
    arr.append(sum[index_])
  return arr


def main():      
#    scr.sheet_to_csv('museos'       ,'Datos Argentina - Museos!A1:Z'                ,'https://docs.google.com/spreadsheets/d/1PS2_yAvNVEuSY0gI8Nky73TQMcx_G1i18lm--jOGfAA/edit#gid=514147473')      
#    scr.sheet_to_csv('cines'        ,'Datos Argentina - Salas de Cine!A1:Z'         ,'https://docs.google.com/spreadsheets/d/1o8QeMOKWm4VeZ9VecgnL8BWaOlX5kdCDkXoAph37sQM/edit#gid=1691373423')                       
#    scr.sheet_to_csv('bibliotecas'  ,'Datos Argentina - Bibliotecas Populares!A1:Z' ,'https://docs.google.com/spreadsheets/d/1udwn61l_FZsFsEuU8CMVkvU2SpwPW3Krt1OML3cYMYk/edit#gid=1605800889')   
    
    mus = pd.read_csv(scr.new_namer('museos'),      skiprows=1)
    cin = pd.read_csv(scr.new_namer('cines'),       skiprows=1)
    bib = pd.read_csv(scr.new_namer('bibliotecas'), skiprows=1)
    
    mus = mus.drop(columns=['0'])
    cin = cin.drop(columns=['0'])
    bib = bib.drop(columns=['0'])

    mus.columns = normalize(mus.columns.str.capitalize())
    cin.columns = normalize(cin.columns.str.capitalize())
    bib.columns = normalize(bib.columns.str.capitalize())

    mus = mus.rename(columns = {'Direccion':'Domicilio'})
    cin = cin.rename(columns = {'Direccion':'Domicilio'})
    bib = bib.rename(columns = {'Cod_tel':'Cod_area'})

#   --- GENERAL DATAFRAME ---
    df = pd.concat([mus,cin,bib])
    filter_df = ((mus.columns.intersection(cin.columns)).intersection(bib.columns))
    df = df[filter_df]



#   --- DATOS CINE DATAFRAME ---
    datos_cine_df = pd.DataFrame({
        'Provincia': [],
        'Cant_pantallas': [],
        'Cant_butacas': [],
        'Cant_espacios_incaa': []
    })

    datos_cine_df['Provincia'] =            pd.unique(cin['Idprovincia'])
    datos_cine_df['Cant_pantallas'] =       adder(cin, 'Idprovincia', datos_cine_df.columns.get_loc('Cant_pantallas')+1)
    datos_cine_df['Cant_butacas'] =         adder(cin, 'Idprovincia', datos_cine_df.columns.get_loc('Cant_butacas')+1)
    datos_cine_df['Cant_espacios_incaa'] =  counter(cin, 'Idprovincia', 'si', 'Espacio_incaa')

#    print(df)
    print(df.columns)
    print('------------------------------------------------------------------')
    print(datos_cine_df)

    tbmkr.add_table(df, 'Datos_Argentina')
    tbmkr.add_table()
    tbmkr.add_table(datos_cine_df, 'Datos_Cine')

main()