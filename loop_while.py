"""
Loop while

while expressão_booleana:
    //execução do loop

O bloco while será repetido enquanto a expressão booleana for verdadeira.

Expressão boolenada é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5
"""

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# OBS: Em um loop while é importante que cuidemos do critério de parada.

# Exemplo 2

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou?')