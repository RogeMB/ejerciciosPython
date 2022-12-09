# Dar la vuelta a la siguiente cadena y extraer sus diferentes componentes en diferentes variables. Genera una variable
# llamada cadena_formateada con: {nombre} ha sacado un {nota} en {materia}

cadena_corrupta = "airotsiH,6.7,aícraG nómaR"

cadena_volteada = cadena_corrupta[::-1]
print(cadena_volteada)

materia = cadena_volteada[17:]
print(materia)

nombre = cadena_volteada[:12]
print(nombre)

nota = cadena_volteada[13:16]
print(nota)

cadena_formateada = nombre + " ha sacado un " + nota + " en " + materia
print(cadena_formateada)