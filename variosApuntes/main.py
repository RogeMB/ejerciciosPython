# genera una lista de los nº de los quince primeros numeros que el nº elevado al cubo sea impares.
from functools import reduce

lista = [numero for numero in
         [numero ** 3 for numero in range(0, 15)]
         if numero % 2 == 1]  # != 0
print(lista)

languages = ['java', 'python', 'loquesea', 'scala']

cap_lang = [lang.capitalize() for lang in languages]
print(cap_lang)


def pares(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num


print([numero for numero in pares(10)])

p = pares(7)

print(next(p))
print(next(p))
print(next(p))
print(next(p))


def multiplo_de5(numero):  # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True  # Sólo devolvemos True si lo es


numeros = [2, 5, 10, 23, 50, 33]

f = filter(multiplo_de5, numeros)
l = list(f)
print(l)

multiplos_de_5 = list(filter(lambda x: x % 5 == 0, numeros))
print(multiplos_de_5)

print(list(map(lambda li: li.capitalize(), languages)))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10, 11]  # imprime hasta la lista de menor número de elementos

print(list(map(lambda x, y: x * y, a, b)))

# zip es como flatMap en Java. Devuelve un iterable

a = ['PSP', 'AD', 'DI', 'PDMD']
n = [3.4, 2.5, 7.4, 6.6]

print(list(zip(a, n)))

resultado2 = reduce(lambda x, y: x+y, range(1, 101))


array = ["Hola", "buenos", "días"]
print(reduce(lambda na, ma: na + " " + ma, array))



# d es un diccionario

dicci = {}
dicci["PM"] = 6.5
dicci["AD"] = 5.4



# contar las distintas ocurrencias de las letras


def count(characters):
    return reduce(reducer, map(lambda char: dict([[char, 1]]), characters))


def reducer(i, j):
    for k in j: i[k] = i.get(k, 0) + j.get(k, 0)
    return i


print
count('testing yeah it works')






for key in dicci.keys():
    print(key + " " + str(dicci[key]))

for k, v in dicci.item():
    print(k + " " + str(v))

print(reduce(lambda x, y: x+y, dicci.values())/len(dicci))

# realizar copias. Comprobar que una se hace copia nueva y otra la copia encima

dicci1 = {'a': 1, 'b': 2}
dicci2 = {'c': 3, 'd': 4}


d_copy = dicci1
del dicci1['a']
print(d_copy)


d2_copy = dict(dicci2)
del dicci2['c']
print(d2_copy)
