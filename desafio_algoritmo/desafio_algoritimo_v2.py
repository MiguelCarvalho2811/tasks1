#!/home/miguel/curso-python/bin/python3
import sys
import math

numero = input('Digite um número inteiro positivo de qualquer tamanho: ')
try:
    numero = int(numero)
    if numero < 0:
        print('Numero invalido')
        sys.exit(2)
except:
    print('Você inseriu um valor inválido')
    sys.exit(2)

print(f"Vamos trabalhar com o numero {numero}")
print(type(numero))
digitos = int(math.log10(numero))+1
result = list()
while digitos > 2:
    last_digit = numero % 10
    result.append(last_digit)
    nms_restantes = numero // 10
    numero = nms_restantes
    digitos = int(math.log10(nms_restantes))+1
else:        
    result.append(numero % 10)
    result.append(numero // 10)  

while result:
    print(result.pop())
