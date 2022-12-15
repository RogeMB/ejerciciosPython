def tabla_cinco():
    for i in range(1, 11):
        print("5 * {} = {}".format(i, i * 5))


tabla_cinco()


# Podemos utilizar variables declaradas siempre antes de llamar a la función, incluso habiéndola definido. Pero ojo con
# esta práctica. Mejor llamar las variables como parámetro o llamarlas dentro de la función.

def test():
    print(l)


l = 10
test()


# El slicing es compatible con las llamadas a la función
def test_dos():
    return [1, 2, 3, 4, 5]


print(test_dos()[-1])
# para optimizar memoria:

lo = test_dos()
lo[-1]


def test_tupla():
    return "Una cadena", 20, [1, 2, 3]


cadena, numero, lista = test_tupla()

print(cadena)
print(numero)
print(lista)


# Argumentos: lo que le pasas a la función. Eso mismo que le pasas en la función luego se le llama Parámetros.

# Ejercicio:
# Realizar una función que reciba un número e imprima si es par o impar

def par_o_impar(numero):
    if numero % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")


par_o_impar(2)

