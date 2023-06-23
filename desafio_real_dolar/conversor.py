#!/home/miguel/curso-python/bin/python3
import requests
valor_informado = input('Insira um valor monetário em Reais: ')
valor_informado = float(valor_informado)
if valor_informado < 0:
    raise ValueError
valor_informado_arredondado = round(valor_informado, 2)

response = requests.get('https://economia.awesomeapi.com.br/last/USD')
if response.status_code == 200:
    data = response.json()
else:
    print('Falha na solicitação. Código de status:', response.status_code)

data = dict(data)
cotacao_atual = data.get('USDBRL').get('high')
cotacao_atual = float(cotacao_atual)

valor_convertido = valor_informado_arredondado / cotacao_atual
valor_convertido = round(valor_convertido, 2)

print(f'Valor informado: R${valor_informado_arredondado}')
print(f'Cotação atual do Dólar/Real:R${cotacao_atual}"')
print(f'Valor convertido para Dólar: U${valor_convertido}')