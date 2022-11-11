"""
Funções com parâmetro padrão (default paramters)

- Funções onde a passagem de parâmetro seja opcional;
"""

print("Geek University")
print() # Exemplo de função onde a passagem de parâmetro é opcional

def quadrado(numero):
    return numero ** 2
print(quadrado(3)) # Exemplo de função onde a passagem de parâmetro é obrigatória

def exponencial(numero, potencia):
    return numero ** potencia
print(exponencial(2, 3)) # Se o usuário passar apenas um atributo, será atribuído ao parâmetro número, e será calculado o quadrado.
#obs: Em funções Python, os parâmetros com valores default (padrão) devem sempre estar ao final da declaração.

# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 3, subtracao))

instrutor = 'Geek1' # Variável glocal

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}'

print(diz_oi()) # A variável local sobrepõe a global. Se puder, evitar o uso de variável global

total = 0

def incrementa():
   total = total + 1 # A variável está sendo utilizada para processamento sem ter sido inicializada, gerando erro.
    return total

total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variável global

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa()) # Vai até o número 3

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())


