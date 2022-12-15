# Realizar una función llamada recortar(numero, minimo, maximo) que devuelva el límite inferior si el número es menor
# que el mínimo. Que devuelva el límite superior si el número es mayor que el máximo. Que devuelva el número sin cambios
# si no supera ningún límite

def recortar(numero, minimo, maximo):
    if numero > maximo:
        return maximo
    elif numero < minimo:
        return minimo
    return numero


print(recortar(5, 4, 9))



