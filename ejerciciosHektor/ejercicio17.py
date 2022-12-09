# Diccionarios: Colecciones mutables con estructura mapeada clave valor con clave única. Se crean con {}. Muy utilizados.
# Podemos sobreescribir valores

colores = {'amarillo': 'yellow', 'azul': 'blue'}
colores['verde'] = 'green'
colores['amarillo'] = 'white'
del (colores['amarillo'])

print(colores)
edades = {'Hector': 27, 'Juan': 45, 'Maria': 34}

for clave in edades:
    print(clave, edades[clave])

for clave, valor in edades.items():
    print(clave, valor)

# INTENTAR NO PONER ACENTOS NI CARACTERES EXTRAÑOS EN LAS CLAVES DE LOS DICCIONARIOS

# Ejercicio
# modificar el diccionario de animales añadiendo perro, gato y rana (con su valor en inglés).
# Luego añadir el valor en inglés de caballo y vaca.
# Por último, elimina rana y vaca.


animales = {"caballo": "", "vaca": ""}

animales["perro"] = "dog"
animales["gato"] = "cat"
animales["rana"] = "frog"
print(animales)

animales["caballo"] = "horse"
animales["vaca"] = "cow"
print(animales)

del (animales["vaca"])
del (animales["rana"])
print(animales)
