dict_user = {
    'nombre': 'Pepito',
    'edad': 26,
    'com_fav': ['completos', 'papas fritas'],
}

dict_user['nombre'] = 'Pepito VIII'
dict_user['apellido'] = 'de la mancha'

print('dict_user')

for key in dict_user.keys():
    print(key, '=>', dict_user)