# Voltear la siguiente cadena y que resulte en una nueva cadena con: {Nombre Apellido} ha sacado un {Nota} de nota.

cadena = "zeréP nauJ,01"

cadena = cadena[::-1]

nombre_apellido = cadena[3:]

nota = cadena[:2]

print(nombre_apellido + " ha sacado un " + nota + " de nota.")
