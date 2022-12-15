# Podemos definir el orden de los argumentos (argumentos por posición)

def resta(a, b):
    return a - b


print(resta(1, 2))

# Así:
print(resta(b=2, a=1))


def resta_sin_errores(a=None, b=None):
    if a is None or b is None:
        return print("Error, debes pasar dos valores númericos")
    return a - b


print(resta_sin_errores())
print(resta_sin_errores(2, 4))
