# Tuplas. Son inmutables. Permiten menos métodos. Dan menos errores difíciles de localizar. Útiles para programas
# grandes

tupla = (100, "Hola", [1, 2, 3], -50)

# Permiten slicing

print(len(tupla[1]))

print(tupla.index(100))

# A partir de una tupla, imprime:

# El último elemento de la tupla.
# El número de elementos que tiene la tupla.
# La posición donde se encuentra el número 123 de la tupla.
# Una lista con los primeros tres elementos de la tupla.
# El elemento que hay en la posición con índice 4 de la tupla.
# El número de veces que aparece el número 4 en la tupla.

tupla = ("hola", 123, 4, 128, 4, 256, "adios", "sí", -50, 3.14)

print(tupla[-1])
print(len(tupla))
print(tupla.index(123))
print(list(tupla[:3]))
print(tupla[4])
print(tupla.count(4))
