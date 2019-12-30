MyList=[1,2,4,5]

#Agregar algo al final
MyList.append("hola")
print(MyList)

#Agregar algo en un cierto índice
MyList.insert(1,"mundo")
print(MyList)

#Remover un objeto pasado
MyList.remove("mundo")
print(MyList)

#Regresar y quitar un objeto de un indice o el ultimo
MyList.pop()
MyList.pop(0)
print(MyList)

#Quitar un objeto de la lista sin regresarlo
del MyList[0]
print(MyList)

#Voltear una lista
MyList.reverse()
print(MyList)

#Copiar lista
MyCopy = MyList.copy()
print(MyCopy)
