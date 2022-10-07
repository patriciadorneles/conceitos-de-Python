""""
Recebendo dados do usuário
"""
# Entrada de Dados
 print("Qual seu nome?")
 nome = input() # Input -> Entrada

# Processamento

#Saída de dados
 print('Seja bem-vindo(a) %s' % nome)

 print("Qual sua idade?")
 idade = input()

# Processamento

# Saída
 print("A %s tem %s anos" % (nome, idade))

# Maneira mais moderna de fazer a mesma coisa que a cima:
print("Qual seu nome?")
nome = input()
print("Qual sua idade?")
idade = input()
print("Seja bem-vindo(a) {0}".format(nome))
print("A {0} tem {1} anos".format(nome,idade))