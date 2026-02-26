# Creamos la lista de varios tipos myMixedTypeList, en la cual se guardan diferentes tipos de datos
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# El ciclo for se encarga de mirar cada uno de los elementos de la lista
# Utilizamos el bucle for para recorrer la lista e imprimimos el tipo de cada elemento en ella
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))