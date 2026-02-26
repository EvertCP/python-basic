# Para crear una lista usamos corchetes []
# Creamos la lista llamada myFruitList y almacenamos los valores dentro de la lista
myFruitList = ["apple", "banana", "cherry"]

# Imprimimos la lista
print(myFruitList)

# Imprimimos el tipo de valor de la variable
print(type(myFruitList))

# Imprimimos la posicion 0  de la lista myFruitList
print(myFruitList[0])

# Imprimimos la posicion 1  de la lista myFruitList
print(myFruitList[1])

# Imprimimos la posicion 2  de la lista myFruitList
print(myFruitList[2])

# En Python podemos cambiar el valor asignado de una lista accediendo por su posicion
# Cambiamos el valor de la lista en su posicion 2 por "orange"
myFruitList[2] = "orange"

# Imprimimos la posicion 2 de la lista myFruitList y vemos el ultimo valor asignado
print(myFruitList)

# Para crear una tupla usamos parentesis ()
# Cramos la tupla llamada myFinalAnswerTuple y almacenamos los valores dentro de esta
myFinalAnswerTuple = ("apple", "banana", "pineapple")

# Imrpimimos la tupla
print(myFinalAnswerTuple)

# Imprimimos el tipo de valor de la variable
print(type(myFinalAnswerTuple))

# Imprimimos el valor que esta en la posicion 0 de la tupla myFinalAnswerTuple
print(myFinalAnswerTuple[0])

# Imprimimos el valor que esta en la posicion 1 de la tupla myFinalAnswerTuple
print(myFinalAnswerTuple[1])

# Imprimimos el valor que esta en la posicion 2 de la tupla myFinalAnswerTuple
print(myFinalAnswerTuple[2])

# Para crear un diccionario se utilizan {} y dentro de ellas se va a crear una clave y un valor, la clave, y el valor van separados por : y luego de cada clave:valor se separa del siguiente usando ,
# Creamos el diccionario myFavoriteFruitDictionary con las siguientes claves "Akua", "Saanvi", "Paulo" y sus correspondientes valores "apple", "banana", "pineapple"
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

# Imprimimos el diccionario completo
print(myFavoriteFruitDictionary)

# Imprimimos el tipo de variable de myfavoriteFruitDictionary
print(type(myFavoriteFruitDictionary))

# Imprimimos el valor da la clave "Akua"
print(myFavoriteFruitDictionary["Akua"])

# Imprimimos el valor de la clave "Saanvi"
print(myFavoriteFruitDictionary["Saanvi"])

# Imprimimos el valor de la clave "Paulo"
print(myFavoriteFruitDictionary["Paulo"])