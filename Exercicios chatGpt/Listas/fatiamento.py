# Exercício 1:
# Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
# obtenha uma sublista contendo apenas os elementos do índice 3 ao 7 (inclusive).

lista_um = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_dois = lista_um[3:8]

print(lista_dois)


# Exercício 2:
# Dada a lista letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 
# obtenha uma sublista contendo os três primeiros elementos.

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

selecionadas = letras[:3]

print(selecionadas)


# Exercício 3:
# Dada a lista frutas = ['maçã', 'banana', 'laranja', 'manga', 'uva', 'abacaxi'], 
# obtenha uma sublista contendo os últimos dois elementos.

frutas = ['maçã', 'banana', 'laranja', 'manga', 'uva', 'abacaxi']

itens = frutas[-2:]

print(itens)

# Exercício 4:
# Dada a lista numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90], 
# obtenha uma sublista contendo todos os elementos de índices pares.

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

pares = numeros[0:9:2]

print(pares)

# Exercício 5:
# Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9], 
# obtenha uma sublista contendo todos os elementos de índices ímpares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

impares = numeros[1:8:2]

print(impares)

# Exercício 6:
# Dada a lista animais = ['gato', 'cachorro', 'pássaro', 'peixe', 'hamster'], 
# obtenha uma sublista contendo os elementos de índices 1 a 4 (não incluindo o índice 4).

animais = ['gato', 'cachorro', 'pássaro', 'peixe', 'hamster']

itens = animais[1:4]

print(itens)

# Exercício 7:
# Dada a lista numeros = [100, 200, 300, 400, 500, 600, 700], 
# obtenha uma sublista contendo todos os elementos exceto os dois primeiros.

numeros = [100, 200, 300, 400, 500, 600, 700]

itens = numeros[2:]

print(itens)

# Exercício 8:
# Dada a lista cores = ['vermelho', 'azul', 'verde', 'amarelo', 'preto', 'branco'], 
# obtenha uma sublista contendo todos os elementos exceto os dois últimos.

cores = ['vermelho', 'azul', 'verde', 'amarelo', 'preto', 'branco']

itens = cores[:-2]

print(itens)

# Exercício 9:
# Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
# obtenha uma sublista contendo todos os elementos a partir do índice 5 até o final.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

itens = numeros[5:]

print(itens)

# Exercício 10:
# Dada a lista vogais = ['a', 'e', 'i', 'o', 'u'], 
# obtenha uma sublista contendo todos os elementos exceto o primeiro e o último.

vogais = ['a', 'e', 'i', 'o', 'u']

itens = vogais[1:-1]

print(itens)

# Exercício 11:
# Dada a lista numeros = [2, 4, 6, 8, 10, 12, 14, 16], 
# obtenha uma sublista contendo os elementos do índice 2 ao 6 (não incluindo o índice 6).

numeros = [2, 4, 6, 8, 10, 12, 14, 16]

itens = numeros[2:6]

print(itens)

# Exercício 12:
# Dada a lista palavras = ['python', 'java', 'c++', 'javascript', 'ruby'], 
# obtenha uma sublista contendo os elementos do índice 1 ao 4 (não incluindo o índice 4).

palavras = ['python', 'java', 'c++', 'javascript', 'ruby']

itens = palavras[1:4]

print(itens)

# Exercício 13:
# Dada a lista numeros = [5, 10, 15, 20, 25, 30, 35, 40], 
# obtenha uma sublista contendo os elementos de índice 0, 2, 4, 6.

numeros = [5, 10, 15, 20, 25, 30, 35, 40]

itens = numeros[::2]

print(itens)

# Exercício 14:
# Dada a lista meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'], 
# obtenha uma sublista contendo os elementos de índice 6, 7, 8.

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

itens = meses[6:9]

print(itens)

# Exercício 15:
# Dada a lista numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90], 
# obtenha uma sublista contendo os elementos de índice 0 a 5 com passo 2.

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

itens = numeros[:6:2]

print('exercicio 15: ', itens)

# Exercício 16:
# Dada a lista cores = ['vermelho', 'azul', 'verde', 'amarelo', 'preto', 'branco'], 
# obtenha uma sublista contendo todos os elementos em ordem inversa.

cores = ['vermelho', 'azul', 'verde', 'amarelo', 'preto', 'branco']

itens = cores[::-1]

print(itens)

# obervacao Exercicio 16 nao consegui fazer

# Exercício 17:
# Dada a lista numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17], 
# obtenha uma sublista contendo todos os elementos de índice 2 ao final com passo 2.
# observacao o que voce quis dizer com todos elementos de indice 2, temos apenas um elemento por indice

numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17]

itens = numeros[2:3:2]

print(itens)

# Exercício 18:
# Dada a lista letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 
# obtenha uma sublista contendo todos os elementos de índice 1 a 6 com passo 2.

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

itens = letras[1:7:2]

print(itens)

# Exercício 19:
# Dada a lista numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 
# obtenha uma sublista contendo os três primeiros elementos e os dois últimos.

numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

itens = numeros[:3] + numeros[-2:]

print(itens)

# Exercício 20:
# Dada a lista frutas = ['maçã', 'banana', 'laranja', 'manga', 'uva', 'abacaxi'], 
# obtenha uma sublista contendo todos os elementos exceto os três primeiros e os dois últimos.

frutas = ['maçã', 'banana', 'laranja', 'manga', 'uva', 'abacaxi']

itens = frutas[3:4]
itens2 = frutas[3:-2]
print('exercicio 20: ', itens)
print('exercicio 2 20: ', itens2)

# Esses exercícios cobrem diversos aspectos do fatiamento de listas em Python, ajudando a praticar a manipulação e acesso a sublistas.