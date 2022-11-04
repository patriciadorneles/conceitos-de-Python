"""
Funções com retorno:

- Algumas funções retornam, outras não. Exemplo de função que retorna: print(), pop(tira o último número da lista).
- Quando uma função não retorna nenhum valor, vai ser impresso None.
- Refatorar significa reescrever.
- Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da
função para outras funções.

"""

# Reformando a primeira função

def diz_oi():
    print('oi!')

diz_oi()

def diz_oi():
    return 'Oi '

alguem = 'Pedro!'

print(diz_oi() + alguem)