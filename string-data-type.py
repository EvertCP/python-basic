# Creamos una variable myString y dentro de ella guardamos el texto "this is a string"
myString = "This is a string"

# Imprmimos el valor de la variable myString
print(myString)

# Imprimimos y mostramos el tipo de la variable myString
print(type(myString))

# Imprimimos el valor de la variable y lo concatenamos con otro string y despues mostramos en forma de string el tipo de la variable myString
print(myString + " is of the data type " + str(type(myString)))

# Creamos la barioable firstString y dentro de ella guardamos el valor de "water"
firstString = "Water"

# Creamos la barioable secondString y dentro de ella guardamos el valor de "fall"
secondString = "fall"

# Creamos la variable thirdString y dentro de ella concatenamos las otras 2 variables
thirdString = firstString + secondString

# Imprimimos el valor de la variable thirdString
print(thirdString)

# Creamos la variable name y usando la funcion input vamos a almacenar lo que escriba el usuario en consola
name = input("What is your name? ")

# Imprimimos el valor de la variable name
print(name)

# Creamos la variable color y usando la funcion input vamos a almacenar lo que el usuario escriba en consola
color = input("What is your favorite color?  ")

# Creamos la variable animal y usando la funcion input vamos a almacenar lo que el usuario escriba en consola

animal = input("What is your favorite animal?  ")

# Para imprimir usando format, vamos a poner un corchete por cada variable y el format va a poner el valor de las variables en el orden que las estamos usando
print("{}, you like a {} {}!".format(name,color,animal))