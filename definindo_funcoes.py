"""
Definindo Funções:

- Funções são pequenos trechos de código que realizam tarefas específicas.
- Exemplo: print(), len(), max(), min(), etc
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes.
obs: Se escrever uma função que realiza várias funções dentro dela, é interessante fazer uma verificação para que a função seja sempre simplificada.
"""

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

print(cores)

curso = 'Programação Python' # A variável do tipo string não tem append
print(curso)

cores.append('roxo')
print(cores)

cores.clear()
print(cores)


# DRY - Dont Repeat Yourself

"""
Em Python, a forma geral de definir uma função é:
def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> Sempre com letras maiusculas, se for nome composto, e separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
Neste bloco, pode ter ou não retorno da função.
obs: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo
uma função. Também abrimos o bloco de código com dois pontos : , que é utilizado em Python para definir blocos.
"""

# Definindo a primeira função

def diz_oi():
    print('oi!')

# Chamada para execução
diz_oi() # Não esquecer de utilizar parênteses ao executar uma função.

# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

cantar_parabens()

for n in range(5):
    cantar_parabens()

# Em Python podemos criar variáveis do tipo de uma função e executar essa função através da variável

cantar = cantar_parabens

cantar()