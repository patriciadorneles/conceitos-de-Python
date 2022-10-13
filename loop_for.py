"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

for item in interavel:
    //execução do loop


Utilizamos loops para interar sobre sequências ou sobre valores interáveis

Exemplo de interáveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1,10)
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1,10)  # Temos que transformar em uma lista

# Exemplo de for 1 ( Interando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Interando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Interanso sobre um range)
"""
range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
"""
for numero in range(1, 10):
    print(numero)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1,10)  # Temos que transformar em uma lista

"""
Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)
"""
for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)    # Quando não precisamos de um valor, podemos descartá-lo utilizando um underlite (_)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd):
    print(f'Imprimindo {n}')

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
    print(f'A soma é {soma}')

emoji_linha = 1
for num in range(0, 11):
    print('\U0001F60D' *(emoji_linha))
    emoji_linha = emoji_linha + 2