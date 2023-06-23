#!/home/miguel/curso-python/bin/python3
import csv

todos = []
todos_devedores = []

with open('todos-os-clientes.csv', 'r') as file:
    with open('todos-os-clientes.csv', 'r') as saida:
        reader = csv.reader(file)
        next(reader)

        for pessoa in reader:
            todos.append(pessoa)

with open('devedores.csv', 'r') as arquivo:
    with open('devedores.csv', 'r') as saida:
        reader = csv.reader(arquivo)

        for pessoa in reader:
            todos_devedores.append(pessoa)

conjunto1 = set(map(tuple, todos))
conjunto2 = set(map(tuple, todos_devedores))
resultado = conjunto1.difference(conjunto2)
print('Total de adimplentes: {0}'.format(len(resultado)))
print(len(resultado) + len(conjunto2) == len(conjunto1))
final_result = []
for linha in resultado:
    nome = linha[0]
    pais = linha[3]
    final_result.append(f'Nome do devedor: {nome}')
    final_result.append(f'País do devedor: {pais}')
    final_result.append('')


with open('resultado.csv', 'w', newline='') as saida:
    writer = csv.writer(saida)
    for linha in final_result:
        writer.writerow([linha])





saida.close()

