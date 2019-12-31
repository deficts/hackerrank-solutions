dict={'Diego':'A01633932','Santiago':'A01634433'}

#Agregar un par
dict['Gus']='A01635151'
print(dict)

#Eliminar un par
del dict['Diego']
print(dict)

#Obtener un valor con una llave
print(dict['Gus'])

#Recorrer diccionario
for i in dict:
    print(i+": "+dict[i])
