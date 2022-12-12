# Operador lógico: not, and, or
# True and True = True,
# True and False = False, False and True = False, False and False = False,
# True or False = True, True or True = True, False or True = True, False or False = False
a = 10
b = 5

print(a * b - 2 ** b >= 20 and not (a % b) != 0)
print(False and not False)

nombre = input("Diga su nombre: ")
edad = int(input("Diga su edad: "))
expresion = nombre != "****" and (10 <= edad < 18) and (3 <= len(nombre) < 10)

print(expresion)

# Operador de asignación --> += -= *= /=  %=  **=

a = 0
a += 5
print(a)

a = 13

a %= 2
print(a)
