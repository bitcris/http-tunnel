def connect():
    import  conexao

def get():
    import requisicao


print('ESCOLHA O NÚMERO DA OPÇÃO:\n1 - CONNECT\n2 - GET')   

esc = int(input(''))

if esc == 1:
    connect()

elif esc == 2:
    get()    
