"""
Funções com Parâmetros (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída.
"""

# Refatorando uma função

def quadrado_de_7():
    return 7*7
print(quadrado_de_7())

def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(9))
print(quadrado(5))

# Refatorando 2

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva a {aniversariante}!')

cantar_parabens('Patrícia')

# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada em uma função quantos parâmetros forem
# necessários. São separados por vírgula
# Exemplo

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))
print(multiplica(4, 5))
print(multiplica(2, 8))
print(outra(3, 2, 'Geek '))

# Obs: Se informarmos um número errado de parâmetros ou argumentos, teremos erro.

# Nomeando parâmetros

def nome_completo(string1, string2):
    return f'Seu nome completo é {string1} {string2}'
print(nome_completo('Patrícia', 'Dorneles'))

# Diferença entre parâmetros e argumeentos:
# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;
# A ordem dos parâmetros importa

# Argumentos Nomeados (KeyWord Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.
# Exemplo

nome = 'Patrícia'
sobrenome = 'Dorneles'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (keyword arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.

print(nome_completo(string1='Patricia', string2='Dorneles'))
print(nome_completo(string1='Dorneles', string2='Patrícia'))


