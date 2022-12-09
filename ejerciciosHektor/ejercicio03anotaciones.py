# Escribir una cadena que salga "Python es un lenguaje de programación moderno" a partir de las siguientes cadenas:

cadena1 = "moderno"
cadena2 = "Python"
cadena3 = "de programación"
cadena4 = "es un lenguaje"

cadena5 = cadena2 + " " + cadena4 + " " + cadena3 + " " + cadena1

print(cadena5)

# Notas:

# tabulación: \t
# salto de línea: \n

# Podemos escribir una cadena en raw (crudo) con una r delante

cadena_cruda = r"C:\nuevacarpeta\ejercicio03"
print(cadena_cruda)

# También podemos multiplicar cadenas
espacio = " "
cuatro_espacios = espacio * 4

# También podemos hacer que nos detecte espacios y tabulaciones con tripe comillas
texto = """ Esto saldrá de manera idéntica
a la que        escribamos todo."""
print(texto)

# Para voltear cadenas utilizamos [::-1]

# Podemos extraer índices de cadenas con []. Ejemplo [0], ejemplo [-3], ejemplo[2], ejemplo[:2], ejemplo[-2:]
# ejemplo[:], ejemplo[:99]

# Podemos utilizar slicing para coger múltiples índices, es decir, trozos determinados.
