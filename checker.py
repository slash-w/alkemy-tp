now = ['0', 'Cod_loc', 'Idprovincia', 'Iddepartamento', 'Categoria',
       'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'Piso', 'Cp',
       'Cod_area', 'Telefono', 'Mail', 'Web', 'Latitud', 'Longitud',
       'Tipolatitudlongitud', 'Fuente']

must = ['Idprovincia', 'Cod_loc', 'Iddepartamento', 'Categoria', 'Provincia',
'Localidad', 'Nombre', 'Domicilio', 'Cp', 'Cod_area', 'Telefono', 'Mail', 'Web']

'''for i in t:
    must.append(i.capitalize())'''

total = 0

for i in must:
    if i in now:
        total+=1
    else:
        print(i)

print('-----------')
print(len(must))
print(total)
print(must)