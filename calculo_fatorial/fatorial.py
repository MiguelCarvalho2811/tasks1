#!/home/miguel/curso-python/bin/python3
import sys
n_informado = input(f'Informe um número inteiro positivo: ')

try:
    n = int(n_informado)
except ValueError:
    print('Insira um valor válido')
    sys.exit(1)

if n <= 0:
    print('Insira um valor válido')
    sys.exit(1)

else:
    fatorial = 1
    n_informado = int(n_informado)
    for i in range(1, n_informado + 1):
        fatorial *= i
    print(f'O fatorial de {n_informado} é {fatorial}')