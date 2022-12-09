# Funciones anónimas --> Lambda. Funciones simples.


doblar = lambda num: num * 2
print(doblar(2))

impar = lambda num: num % 2 != 0
print(impar(3))

revertir = lambda cadena: cadena[::-1]
print(revertir("Hola"))

sumar = lambda x, y: x + y
print(sumar(3, 4))

numeros = [2, 5, 7, 10, 33, 42, 50]

print(list(filter(lambda numero: numero % 5 == 0, numeros)))

# Con map() aplicamos la condición a todos los elementos devolviendo un iterable de tipo map

lista2 = list(map(lambda numero: numero * 2, numeros))
print(lista2)

a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]
c = list(map(lambda x, y: x * y, a, b))


# Ejercicio
# Mapear una lista de números y dividir sus valores entre dos. Además, filtrar de la lista mapeada
# los que no sean múltiplos de 5

numeros2 = list(filter(lambda num: num % 5 == 0, map(lambda num: num/2, numeros)))
