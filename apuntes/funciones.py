from math import pi


def saludar(nombre, apellidos):
    print(f'Hola ${nombre} ${apellidos}, ¿qué tal estás?')


type(saludar)

saludar("Roge", 'Mohigefer')
saludar(apellidos='Mohigefer', nombre='Roge')  # asignación nominal


def carac_circunferencia(radio=1):
    area = pi * radio * radio
    longitud = 2 * pi * radio
    return area, longitud  # devuelve una tupla


tupla = carac_circunferencia(3)
print(tupla)

a, l = carac_circunferencia(4)
print(f'Área: {a}')

a2 = carac_circunferencia(5)
print(a2)


# varags --> igual que en java (los tres puntitos ...) . Son un número indeterminado de cosas que funcionan como un
# array (lista en python)

def listar(*elemn):
    for e in elemn:
        print(e)


listar('a', 'b', 'c')
print(listar())


def saludardos(saludo='Hola, ', *personas):
    for p in personas:
        print(f'{saludo} {p}')


saludardos('Ola ke ase, ', 'David', 'Durbán', 'Antonio')


def sumardos(*num):
    result = 0
    for e in num:
        result += e
    return result


l = [1, 2, 3, 4, 5]

# sumardos(l) # esto no se puede hacer

# aquí los referencia individualmente, y los suma correctamente
print(sumardos(*l))


def tonterida(*args):
    for t in args:
        print(t)


tupla = ("Hola", "Mundo", "Pythoners")

tonterida(tupla)
tonterida(*tupla)  # Aquí los referenciamos individualmente. Esto se llama unpacking


def funcion(**kwargs):
    for key in kwargs:
        print(f'key: {key}, value:{kwargs[key]}')


funcion(Luismi=7, Robe=8, Adri=9, Roge=9)

a = 4
b = 6
c, r = divmod(a, b) # nos devuelve el cociente y resto

print(f'Cociente: {c}, ; Resto: {r}')


# Mirar funciones recursivas, recursivas múltiples, documentación de funciones.
# Y Programación de funciones de hektor profe

# Buscar Built-in functions in Python y estudiarlas

