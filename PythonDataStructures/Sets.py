MySet={1,2,3}

MySet2={1,2,9}

#Agregar objeto en set
MySet.add(4)
MySet.add(1)#Ignora este comando por que ya esta en el set
print(MySet)

#MySet - MySet2
print(MySet-MySet2)

#Mostrar todos los objetos
print(MySet|MySet2)

#Mostrar todos los objetos que comparten
print(MySet&MySet2)

#Mostrar objetos que no se comparten en los sets
print(MySet^MySet2)
