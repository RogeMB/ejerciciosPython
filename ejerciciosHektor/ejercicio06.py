# Input lee siempre cadenas de caracteres. Hay que castear (int) (float)

# Leer por teclado las variables: nombre, edad, numero_magico, apellido. Crear una cadena_final con el formato:
# NOMBRE APELLIDO: Tu número de la suerte es el EDAD*Numero_MAGICO


nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad (entero): "))
numero_magico = float(input("Introduce un número mágico (racional positivo): "))

cadena_final = nombre.upper() + " " + apellido.upper() + ": Tu número de la suerte es el " + str(edad * numero_magico)
print(cadena_final)
