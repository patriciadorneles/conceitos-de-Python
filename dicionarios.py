"""
Dicionários
São coleções do tipo chave/valor.
São representados por chaves {}.

Sobre Dicionários:
- Chave e valor são separados por dois pontos 'chave:valor';
- Tanto chave quanto valor podem ser de qualquer tipo de dado;
- Podemos misturar tipos de dados.
"""
# Forma mais comum para a criação de dicionários

print(type({}))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2, menos comum

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['eua'])

# Caso tentemos fazer um acesso utilizando uma chave que não existe, teremos erro

# Forma 2 - Acessando via get (Recomendada)

print(paises.get('br'))
print(paises.get('ru')) # Vai gerar um tipo nome, que representa o tipo sem tipo, conhecido como tipo vazio.

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

russia = paises.get('ru')

if russia:
    print('Encontrei o país')
else:
    print('Não encontrei o país')


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('br', 'Não encontrado')
print(f'Encontrei o país')


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print('br' in paises)
print('ru' in paises)
print('Estados Unicos' in paises)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário, como chaves de dicionários.
# Tuplas são interessantes de serem utilizadas como chave de dicionário, pois as mesmas são imutáveis.

localidades = {
    (35.6895, 39.6917): 'Escritório do Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'maio': 500}

receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário
# Forma 1

receita['maio'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# A forma de adicionar elementos ou atualizar dados em um dicionário é a mesma;
# Em dicionários, não podemos ter chaves repetidas. No exemplo do mês de maio, o valor foi apenas atualizados.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1

ret = receita.pop('mar') # Aqui percisamos sempre informar a chave, e caso não encontre o elemento, da erro
print(receita)

# Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']
print(receita) # Se a chave não existir irá gerar erro; Neste caso, o valor removiso não é retornado

# Por quê utilizar dicionários:
# - Carrinho de compras de e-commerces

carrinho = []

produto1 = ['Videogame', 1, 230.00]
produto2 = ['God of War', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber o índice de cada informação do produto.

# Forma 2 - Utilizando tuplas

produto1 = ('Videogame 2', 1, 230.00)
produto2 = ('God of War', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Forma 3 - Utilizando dicionários

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 230.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos do carrinho, e em cada produto podemos ter certeza sobre cada informação.

# Métodos de dicionários
# Limpar o dicinário (zerar dados)

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

d.clear()

print(d)

# Copiando um dicionário para outro

# Forma 1

d = dict(a=1, b=2, c=3)

novo = d.copy() # Deep copy

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 - Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(type(d))