# Comprensión listas --> primero lo que queremos guardar y luego el bucle for

lista = [letra for letra in 'casa']
print(lista)


lista2 = [numero**2 for numero in range(0, 11)]
print(lista2)


lista3 = [numero for numero in range(0, 11) if numero % 2 == 0]
print(lista3)

lista4 = [numero for numero in [numero**2 for numero in range(0, 11)] if numero % 2 == 0]
print(lista4)


# Ejercicio
# Utiliza to lo que sabes para generar una lista en una única línea llamada multiples que contenga todos los números
# múltiples comunes de 2, 3, 4 y 8 entre 0 y 500 (ambos incluidos). No puede contener números repetidos y estos deben
# estar ordenados de menor a mayor.

lista5 = [numero for numero in range(0, 501) if numero % 2 == 0 and numero % 3 == 0 and numero % 4 == 0 and numero % 8 == 0]
print(lista5.sort())
# se podría hacer con el mínimo común múltiplo de 2, 3, 4, 8 que es 24 --> numero %24 == 0
