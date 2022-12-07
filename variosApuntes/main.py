# genera una lista de los nº de los quince primeros numeros que el nº elevado al cubo sea impares.


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


print(list(map(lambda li : li.capitalize(), languages)))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10, 11] #imprime hasta la lista de menor número de elementos

print(list( map(lambda x,y : x*y, a,b) ))


#zip es como flatMap en Java. Devuelve un iterable

a = ['PSP', 'AD', 'DI', 'PDMD']
n = [3.4, 2.5, 7.4, 6.6]

print(list(zip(a, n)))