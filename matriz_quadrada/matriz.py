#!/home/miguel/curso-python/bin/python3

matriz = [
    [1, 2, 3, 5],
    [4, 5, 6, 7],
    [7, 8, 9, 9],
    [9, 1, 4, 3],
]
for indice, valor in enumerate(matriz):
    for indice1, valor1 in enumerate(valor):
        if indice == indice1:
            print(valor1)