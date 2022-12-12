# Anotaciones:
# Conjuntos: colecciones desordenadas de elementos únicos. Útil para eliminar elementos duplicados.
# Soportan operaciones matemáticas avanzadas.

conjunto1 = set()
conjunto2 = {1, 2, 3}
conjunto2.add(0)
conjunto2.add(7)
conjunto2.add(6)
conjunto2.add(4)
conjunto2.add(9)

conjunto2.add('H')
conjunto2.add('A')
conjunto2.add('Z')
conjunto2.add('b')
conjunto2.add('O')
conjunto2.add('s')
conjunto2.add('R')

print(conjunto2)

# Conversiones de lista a conjunto

lista = [1, 2, 3, 3, 2, 1]

print(lista)

conjunto = set(lista)
lista = list(conjunto)

print(lista)  # Hemos quitado todos los repetidos de golpe

grupo_dos = {'Hector', 'Juan', 'Mario'}
print('Hector' not in grupo_dos)

cadena = "Al pan pan y al vino vino"
print(set(cadena))  # nos transforma la cadena en un conjunto sin caracteres repetidos y lo desordena


# Ejercicio:
# Dado el conjunto grupo, añadir los usuarios Ana, Ramón, Marta, Eric y David. Elimina luego a Mario, Miguel y Ramón.

grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

lista2 = ["Ana", "Ramón", "Marta", "Eric", "David"]

for i in lista2:
    grupo.add(i)

print(grupo)

lista3 = ["Mario", "Miguel", "Ramón"]

for i in lista3:
    if i in grupo:
        grupo.remove(i)

print(grupo)
