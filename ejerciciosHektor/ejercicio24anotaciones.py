# Anotaciones
# Función decoradora: función que envuelve la ejecución de otra función y permite extender su comportamiento. Pensadas
# para ser reutilizadas.

def hola():
    return "Hola!"


def adios():
    return "Adios!"


def test(funcion):
    print(funcion())


def monitorizar(funcion):
    def decorar():
        print("\tSe va a ejecutar la función:", funcion.__name__)

        funcion()

        print("\tSe ha terminado la ejecución de la función: ", funcion.__name__)

    return decorar()


@monitorizar
def saludar():
    print("Buenos días!")


def pares(n):
    for numero in range(n + 1):
        if numero % 2 == 0:
            yield numero


lista3 = list(pares(10))
print(lista3)

lista4 = [numero for numero in pares(18)]  #
print(lista4)

# Podemos conseguir el primer elemento del iterable con next(), porque pares() devuelve
# una secuencia iterable (iterador), no exactamente una lista
print(next(pares(3)))  # devuelve el primer número que es 0


# Podemos transformar una lista o una cadena a iterable con iter()
iter(lista4)
next(lista4)

# Ejercicio

# Crea una función generadora llamada cuadrados(numero) que a partir de un número genere todos los números de 1 a X
# (ambos incluidos) y sus potencias de dos.


def cuadrados(numero):
    for i in range(1, numero+1):
        yield i, i**2


lista7 = []
for num in cuadrados(5):
    lista7.append(num)

print(lista7)
