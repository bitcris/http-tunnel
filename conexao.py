import socket

print('PYTHON CONNECT V1.0\n')
defaultUrl = 'api.apifree.top'

url = input('URL/IP: ')

if url == "":
  url = defaultUrl

  


def tunnel():
  print(f'CONECTANDO A [ {url} ]...\n')

# Crie um soquete INET, com fluxo de dados (TCP)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((url, 80))

  origem = s.getsockname()
  destino = s.getpeername()
  

  print(f'ORIGEM\nIP: {origem[0]}\nPORTA: {origem[1]}\n\n')
  print(f'DESTINO\nIP {destino[0]}\nPORTA {destino[1]}')







tunnel()
