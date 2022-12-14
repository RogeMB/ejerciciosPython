print("Bienvenido, introduzca sólo valores enteros: ")
print("")
x = int(input("La distancia en metros: "))
y = int(input("Introduzca la velocidad máxima permitida: "))
z = int(input("Introduzca los segundos en recorrer el tramo: "))
velocidad = 0

# print(x, y, z)

while x != 0 and x != 0 and z != 0:
    if x <= 0 or y < 0 or z <= 0:
        print("ERROR")
    else:
        x /= 1000
        z /= 3600
        velocidad = x/z

        if y < velocidad < y * 1.2:
            print("MULTA")
        elif velocidad >= y * 1.2:
            print("PUNTOS")
        else:
            print("OK")

    print("")
    print("Empezamos de nuevo. Introduzca 0 en cada valor para salir.")
    print("")
    x = int(input("Introduczca la distancia en kilómetros: "))
    y = int(input("Introduzca la velocidad máxima permitida: "))
    z = int(input("Introduzca los segundos en recorrer el tramo: "))

if x == 0 and y == 0 and z == 0:
    print("")
    print("FIN DEL PROGRAMA.")
