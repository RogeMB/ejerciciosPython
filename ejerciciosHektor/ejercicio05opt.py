# Dada la siguiente matriz:

matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

# Corregir para que el último elemento sea la suma de los anteriores elementos

matriz[1][-1] = sum(matriz[1][:-1])
matriz[-1][-1] = sum(matriz[-1][:-1])

print(matriz)
