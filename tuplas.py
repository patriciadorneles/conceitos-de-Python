""""
Tuplas (tuple)

Tuplas são parecidas com listas. Existem basicamente duas diferenças: 1 - as tuplas são representadas por ()
2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera
uma nova tupla.


"""

# Cuidado 1: as tuplas são representas por (). mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla.
print(tupla3)

print(type(tupla3))

tupla4 = (4, ) # Isso é uma tupla
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))
# Podemos concluir que tuplas são definidas pelas vírgulas e não pelo uso do parênteses

# Podemos gerar uma tupla dinâmicamente com range(início, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotando de tupla:

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# Gera erro se colocarmos um número diferente de elementos para desempacotar

# Métodos para: adição e remoção de elementos das tuplas não existem, pois são imutáveis.

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação (junção) de tuplas:

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2
print(tupla1) # Tuplas são imutáveis, mas podemos sobrescrever seus valores

# Verificar se determinado elemento está contído na tupla

tupla6 = (1, 2, 3)
print(3 in tupla6)

# Interando sobre uma tupla

tupla7 = (1, 2, 3, 4)
for n in tupla7:
    print(n)

for indice, valor in enumerate(tupla7):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla8 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla8.count('c'))

# Dicas na utilização de tuplas:
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Interar com o while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificando em qual índice um elemento está na tupla

print(meses.index('Junho'))

# OBS: Caso o elemento não exista, será gerado um erro.

# Slicing
# tupla[início:fim:passo]

print(meses[5:])

# Por quê utilizar tuplas?
# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro (imutabilidade das tuplas).

# Copiando uma tupla para outra

tupla9 = (1, 2, 3)
print(tupla9)

nova = tupla9 # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla9)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla9)