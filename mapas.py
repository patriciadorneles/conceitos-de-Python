"""
Mapas -> São conhecidos em Python como Dicionários

Dicionários em python são representados por chaves {}

"""

receita = {'jan':100, 'fev':250, 'mar':400}
print(receita)

# Interar sobre Dicionários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
receita = {'jan':100, 'fev':250, 'mar':400}

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

print(receita.items())

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
#* Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))