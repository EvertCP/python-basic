# Se va a crear un validador  para saber si podemos o no entrar a una fiesta, es importante agregar que para entrar a la fiesta debe ser amyor de edad
# Se crea la variable edad y en ella se va a guardar lo que escriba el usuario
edad = input("Escriba su edad: ")

# Convertimos la variable entrada a entero debido a que  cuando se escribe por consola el valor que se guarda es el de un texto
edad = int(edad)

# Vamos a comparar si la edad es mayor o igual a 18
if edad >= 18 :
    # Imprime que lo deja entrar
    print("puede entrar")
else :
    # Si no se cumple la condicion de ser  mayor de 18 imprime no puede entrar
    print("no puede entrar")

# Ahora se va a validar si la persona es amyor de edad y ademas tiene mas de $500
# Se crea la variable edad y en ella se guarda lo que escriba el usuario
edad = input("Escriba su edad: ")

# Convertimos la variable entrada a entero debido a que  cuando se escribe por consola el valor que se guarda es el de un texto
edad = int(edad)

# Se crea la variable dinero y en ella se guarda lo que escriba el usuario
dinero = input("Escriba su dinero: ")

# Convertimos la variable entrada a entero debido a que  cuando se escribe por consola el valor que se guarda es el de un texto
dinero = int(dinero)

# Vamos a comparar si la edad es mayor o igual a 18
if edad >= 18 :
    # Verificamos que cuenta con el dinero
    if dinero >= 500 :
         # Imprime que lo deja entrar
         print("Puede entrar")
    else:
        # Como no tiene el dinero no puede entrar
        print("no puede entrar")
else:
    # Como no tiene la edad no puede entrar
    print("No puede entrar")
    
    # Vamos a comparar si la edad es mayor o igual a 18 - version 2
if edad >= 18 and dinero >= 500 :
         # Imprime que lo deja entrar
         print("v2 Puede entrar")
else:
    print("v2 No puede entrar")

#--------------------------------------------------------    
# Condicional con multiples comparaciones
dinero = input("Escriba el dinero con el que cuenta: ")

# Convertimos la variable de str a int
dinero = int(dinero)

if dinero < 100 : 
    print("le compro unas galletas")
elif dinero >= 100 and dinero <= 200 :
    print("le compro unos chocolates")
elif dinero > 200 and dinero <= 300 :
    print("le compro 300 pricafresas")
else :
    print("le compro un peluche")
    
    
#-----------------------Laboratorio-------------------------
# Creamos la variable userReply y en ella guardamos lo que nos pide el usuario
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Si lo que hay dentro de la variable es exactamente igual a "yes"
if userReply == "yes":
    # Imprime que nos puede ayudar
    print("We can help you ship that package")
# De lo contrario dice que vuelva pronto
else:
    print("Please come back when you need to ship a package. Thank you.")
    
    
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope or copy): ")

if userReply == "stamps":
    print("We have many stamps desings to choos from.")
    
elif userReply == "envelope":
    print("We have many envelope desings to choos from.")
    
elif userReply == "copy":
    print("We have many copies desings to choos from.")
    
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")