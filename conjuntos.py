"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria dos Conjuntos da Matemática.
- Em Python os Conjuntos são chamados de Sets.

Da mesma forma que na matemática, Sets, ou seja, conjuntos, não possuem valores duplicados. Sets não possuem valores ordenados.
Elementos não são acessados via índice, ou seja, conjuntos não são indexados.
Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles, sem se preocupar com chaves,
valores e ítens duplicados.
Os conjuntos são referências em Python com chaves {}.

Diferença entre conjuntos (sets) e mapas (dicionários):
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor.
    - Conjuntos não respeitam a ordem dos elementos, mas cria uma ordenação própria.
"""

# Definindo um conjunto
# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Temos valores repetidos, mas não aparecem no terminal, é ignorado sem gerar erros.

print(s)
print(type(s))

# Forma 2, mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s)) # Os números repetidos foram ignorados.

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


# Além de não termos valores duplicados, não temos ordem

lista = [99, 2, 34, 23, 12, 1, 44, 5]
print(f'Lista: {lista}')

tupla = (99, 2, 34, 23, 12, 1, 44, 5)
print(f'Tupla: {tupla}')

dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario}')

conjunto = {99, 2, 34, 23, 12, 1, 44, 5}
print(f'Conjunto: {conjunto}')

s = {99, 2, 34, 23, 12, 1, 44, 5}

# Assim como todo outro conjunto python, podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets
# Imagine que fizemos um formulário de cadastro de visitantes em um museu, e os visitantes informaram manualmente a cidade de onde vieram.
# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades temos

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4) # Duplicidade não gera erro, simplesmente é ignorado.
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}

# Forma 1
s.remove(3) # Não é índice, é o valor a ser removido. Se o valor removido não existir, gera erro. Nenhum valor pe retornado.
print(s)

# Forma 2
s.discard(2) # Se o valor removido não existir, nenhum erro é gerado. Não acontece nada.
print(s)

# Copiando um conjunto para outro
s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy (modifica só um conjunto)
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy (os dois conjuntos são modificados)

novo = s
novo.add(4)

print(novo)
print(s)

# Métodos Matemáticos de Conjuntos

