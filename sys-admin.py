# Importamos las librearias
import os
import subprocess

# Recibe un argumento tipo str para ejecutar un comando de Bash
os.system("ls")

# Funciona igual que os pero este es mas eficiente
# con el -l muestra los permisos de cada archivo
subprocess.run(["ls", "-l"])


subprocess.run(["ls","-l","README.md"])

# Ejecuta los comandos en consola e imprime desde donde se esta conectando
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Muestra lo que esta funcionando dentro del disco
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])