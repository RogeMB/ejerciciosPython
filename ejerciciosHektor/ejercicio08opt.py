# Realiza un programa que guarde en una variable numero_magico el valor 12345679. Lea por pantalla otra numero_usuario
# entre el 1 y el 9. Multiplique el numero_usuario por 9. Multiplique el numero_magico por el numero_usuario.
# Finalmente, muestra el valor del numero_magico

numero_magico = 12345679

numero_usuario = int(input("Introduce un número entre el 1 y el 9: "))

while 1 > numero_usuario or numero_usuario > 9:
    numero_usuario = int(input("Introduce un número entre el 1 y el 9: "))

numero_usuario *= 9
numero_magico *= numero_usuario
print("El número mágico es: ", numero_magico)
