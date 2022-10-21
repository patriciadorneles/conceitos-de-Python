"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com diferença de serem dinâmicos e
também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possuem tamanho fixo; ou seja: podemos criar a lista e ir adicionando alimentos (enquando tiver memória disponível);
- As listas não possuem tipo de dado fixo; ou seja: podemos colocar qualquer tipo de dado;
- As listas em Python são representadas por colchetes: []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contído na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

"""
Para adicionar elementos em listas, utilizamos a função append
"""
print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com o append só conseguimos adicionar 1 elemento por vez, mais de um da erro.

lista1.append([8, 3, 1])
print(lista1)

if [8, 3 ,1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44,67]) # Coloca cada elemento da lista como valor adicional a lista. O extend não aceita valor único, apenas interáveis (lista, string)
print(lista1)

# Podemos juntar duas listas
lista1.extend(lista2)
print(lista1)

# Copiar uma lista

lista6 = lista2.copy()
print (lista6)

# Remover o último elemento de uma lista
# O pop não somente remove o último elemento, mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice;
# OBS: Os elementos a direita deste índice serão deslocados para a esquerda;
# OBS2: Se não houver elemento no índice informado, dará erro.
lista5.pop(2)
print(lista5)

# Podemos repetir elementos em uma lista

# Podemos converter uma string em uma lista

curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)

# Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Interando sobre listas
for elemento in lista1:
    print(elemento)

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 9?
print(numeros.index(9))

# print(numeros.index(19)) gera erro, pois não possuímos 19 na lista

# Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
# print(numeros.index(5, 2)) # buscando a partir do índice 2

# Trabalhando com slice de lista com o parâmetro 'fim'
lista = [1, 2, 3, 4]
print(lista[:2]) #começa em 0, pega até o índice 2 - 1
print(lista[1:]) #iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de listas com o parâmetro 'passo'

print(lista[1::2]) #começa em 1, vai até o final, de 2 em 2
print(lista[::2]) #começa em 0, vai até o final, de 2 em 2

# Invertendo valores de uma lista

nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) # soma
print(max(lista)) # máximo valor
print(min(lista)) # mínimo valor
print(len(lista)) # tamanho da lista

# Desempacotamento de listas
lista = [1 , 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)