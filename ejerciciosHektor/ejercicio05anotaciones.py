# Anotaciones:
# Listas. Mutables. Rápidas. Incluyen muchos métodos internos. Tienden a dar errores difíciles de hacer debugger.
# Bien para proyectos pequeños.


# Podemos utilizar slicing en listas
letras = ['a', 'b', 'c']
letras[:2] = ['A', 'B']
print(letras)

# Podemos vaciar listas:
letras = []

a = [1, 2, 3]
b = [4, 5, 6]
r = [a, b]

print(r[-1])
print(r[1][1])
print(len(r))


# Ejercicio:
# Modificar las dos siguientes listas. A la 1 añadirle 1234 y luego "Hola". A la 2 añadirle "Adiós" y luego 1234.
# Generar una lista 3 con todos los elementos de la 1 menos el último.
# Generar una lista 4 con los elementos de la 2 menos el primero y el último
# Generar una lista 5 con los elementos de la 4 más los de la 3

lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

lista1.append(1234)
lista1.append("Hola")
print(lista1)

lista2.append("Adiós")
lista2.append(1234)
print(lista2)

lista3 = lista1[:-1]
print(lista3)

lista4 = lista2[1:-1]
print(lista4)

lista5 = lista4 + lista3
print(lista5)
