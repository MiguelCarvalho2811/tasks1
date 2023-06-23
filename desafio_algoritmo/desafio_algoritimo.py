#!/home/miguel/curso-python/bin/python3
import sys

numero = input('Digite um número inteiro positivo de qualquer tamanho: ')
try:
    numero = int(numero)
    print(type("Vamos trabalhar com o numero {0}".format(numero)))
except:
    print('Deu ruim')
    sys.exit(2)


