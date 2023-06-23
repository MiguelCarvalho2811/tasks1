#!/home/miguel/curso-python/bin/python3
import sys
import math

numero = input('Digite um número inteiro positivo de qualquer tamanho: ')
try:
    numero = int(numero)
    if numero < 0:
        raise ValueError
 except:
    print('Você inseriu um valor inválido')
    sys.exit(2)

print(f"Vamos trabalhar com o numero {numero}")
print(type(numero))
digitos = int(math.log10(numero))+1
while digitos >= 3:
    last_digit = numero % 10
    nms_restantes = numero // 10
    print(last_digit)
logic = nms_restantes
        print(logic)
        break

    else:
        pass
  
