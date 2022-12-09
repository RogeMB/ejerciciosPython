# Realizar un programa que lea dos números por teclado y diga si son iguales, si son diferentes, si el primero es mayor
# que el segundo y si el segundo es mayor o igual que el primero

a = int(input("Diga un nº: "))
b = int(input("Diga otro nº: "))

print("\nIguales: ", a == b, "\nDiferentes: ", a != b, "\nPrimero mayor: ", a > b, "\nSegundo mayor o igual: ", b >= a)

# Pide una frase por teclado y determina si su longitud es mayor o igual que 3 y menor que 10

cadena = input("Escribe una frase: ")
resultado = True

if 3 <= len(cadena) < 10:
    resultado
else:
    resultado = False
    
print("¿La longitud de la frase es mayor o igual a 3 y menor a 10?", resultado)
