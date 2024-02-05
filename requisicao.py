import requests
import json
print('HTTP ZERO - v1.0\nCONECTANDO...\n')

proto = 'https://'
urx = input('DIGITE O URL/IP:PORTA\n')
ref = input('DIGITE O URL/IP DO REFERER\n')



if urx == '':
  url = 'https://api.apifree.top'
else:
  url = f'{proto}{urx}'


if ref == '':
  referer = 'https://apifree.top'
else:
  referer = f'{proto}{ref}'


headers = {
    'User-Agent': 'Mozilla/5.0 (Safari; iOS)',
    'Referer': referer,
    'Accept-Language': 'pt-BR'
}


response = requests.get(url, headers=headers)
print('CONECTANDO...')

# Verifique o status da resposta
if response.status_code == 200:
    print('STATUS 200 - OK\n\nHEADERS:')
    #print(response.headers)
    for key, value in response.headers.items():
      print(f'{key}: {value}')

    tipo = response.headers.get('Content-Type')
    if tipo == "application/json":
      print('\n\nRESPOSTA DA API:')
      data = json.loads(response.text)
      for chave, valor in data.items():
        print(f'{chave}: {valor}')
    print(f'\n\nTIPO:\n{tipo}')
else:
    print(f'Erro na requisição. Código de status: {response.status_code}')