# Siempre que importemos una libreria debe ir al principio del codigo
import random

# Un ciclo While es un bucle que va a recorre hasta que no se cumpla la condicion 

# Escriba la variable numero y se le pide que escriba el numero 0
numero = input("Ingrese el numero 0: ")

# Convertimos la variable numero de str a int
numero = int(numero)

# Se verifica que lo que hay en la variable numero sea menor que 10
while numero < 10 :
    # se incrementa el valor de numero
    numero = numero + 1
    # si numero es menor que 10, se imprime su valor
    print(numero)
    

# vamos a construir algo que nos muestre las tablas de multiplicar de un numero
# Escriba la variable numero y se le pide que escriba el numero 0
numero = input("Ingrese un numero: ")

# Convertimos la variable numero de str a int
numero = int(numero)

# multiplicador
multiplicador = 0

# Se verifica que lo que hay en la variable numero sea menor que 10
while multiplicador < 10 :
    # se incrementa el valor de multiplicador
    multiplicador = multiplicador + 1
    # Valor de multiplicacion
    multiplicacion = numero * multiplicador
    # si numero es menor que 10, se imprime su valor
    #print(numero, " * ", multiplicador, " = ", multiplicacion)
    print(f"{numero} * {multiplicador} = {multiplicacion}")

#---------------------Laboratorio---------------------------
# Se realizan 2 impresiones
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# La libreria random genera numero aleatorios desde un numero inicial hasta un numero final
number = random.randint(1,10)

# Se crea la varaible isGuessRight y se guarda un valor booleano (False)
isGuessRight = False

# Mientras la variable isGuessRight sea diferente de verdadero se ejcuta el codigo
while isGuessRight != True:
    # Se crea la variable guess y se guarda dentro de ella lo que escriba el usuario
    guess = input("Guess a number between 1 and 10: ")
    # Mientras el valor de la variable guess sea un entero exactamente igual al valor de la variable number 
    if int(guess) == number:
        # Imprime que ganamos
        print("You guessed {}. That is correct! You win!".format(guess))
        # La varaible isGuessRight se pasa a True para terminar el ciclo While
        isGuessRight = True
    # Si la variable guess no es exactamente igual a la variable isGuessRight imprime
    else:
        # Intentalo de nuevo
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
