# Para verificar se um número é múltiplo de outro, 
# basta encontrar um número inteiro de modo que a
# multiplicação entre eles resulte no primeiro número
# para que um numero x seja multiplo de um numero y
# precisamos encontrar um numero que ao multiplicarmos por y resulte em x

# x = a * y

# Crie uma função que receba uma lista de números inteiros e retorne uma lista contendo apenas os múltiplos de 3.

def retorna_multiplos_de_tres(lista):
    lista_multiplos = [num for num in lista if num % 4 == 0]
    return lista_multiplos

lst = [x for x in range(1, 21)]

print(retorna_multiplos_de_tres(lst))

# Escreva um programa que verifique se um número fornecido pelo usuário é múltiplo de 4.
# num = int(input('Informe um número multiplo de 4: '))

# while num:
#     if num % 4 != 0:
#         num = int(input(f'O numero {num} nao é multiplo de 4, informe outro: '))
#     else:
#         print(f'O numero {num} é multiplo de 4.')
#         break
    

# Desenvolva uma função que receba uma tupla de números inteiros e retorne uma nova tupla contendo apenas os múltiplos de 5.
def retorna_multiplos_de_cinco(tupla):
    multiplos_de_cinco = [num for num in tupla if num % 5 == 0]
    return tuple(multiplos_de_cinco)

lst = [x for x in range(1, 51)]

print(retorna_multiplos_de_cinco(tuple(lst)))

# Crie um dicionário onde as chaves são números de 1 a 10 e os valores são listas dos múltiplos desses números até 100.
dic = {}

multiplos = []
for i in range(1, 11):
    for x in range(1, 5):
        if x % i == 0:
            multiplos.append(x)
    dic[i] = multiplos
    

print(dic)

# Escreva um programa que gere uma lista de todos os múltiplos de 7 menores que 100.

# Crie uma função que receba uma lista de números inteiros e retorne a soma dos múltiplos de 6 encontrados na lista.

# Escreva um programa que receba um número inteiro do usuário e verifique se ele é múltiplo de 8 ou de 9.

# Desenvolva uma função que receba um dicionário com números inteiros como
# chaves e listas de números inteiros como valores, e retorne um novo dicionário contendo apenas os múltiplos de 10 nas listas de valores.

# Crie uma lista de tuplas onde cada tupla contém um número e seus múltiplos até 50.

# Escreva uma função que receba uma lista de números inteiros e retorne a quantidade de múltiplos de 11 presentes na lista.

# Crie um programa que solicite ao usuário um número e exiba todos os seus múltiplos menores que 100.

# Desenvolva uma função que receba duas listas de números inteiros e retorne uma lista
# contendo os múltiplos de 12 que estão presentes em ambas as listas.

# Escreva um programa que leia uma lista de números inteiros e crie um novo dicionário 
# onde as chaves são os números e os valores são booleanos indicando se são múltiplos de 13.

# Crie uma função que receba uma lista de tuplas, onde cada tupla contém dois números inteiros, 
# e retorne uma nova lista de tuplas contendo apenas as tuplas onde o primeiro número é múltiplo do segundo.

# Desenvolva um programa que receba uma lista de números inteiros e crie um dicionário 
# onde as chaves são os números e os valores são listas dos seus múltiplos até 100.

# Escreva uma função que receba uma lista de números inteiros e retorne uma lista de tuplas, 
# onde cada tupla contém um número e a quantidade de seus múltiplos presentes na lista.

# Crie um programa que gere uma lista de todos os múltiplos de 15 menores que 200.

# Desenvolva uma função que receba um dicionário com listas de números inteiros como valores e 
# retorne um novo dicionário contendo apenas as listas onde todos os números são múltiplos de 14.

# Escreva um programa que receba uma lista de números inteiros e exiba todos os números que são múltiplos de 2 e 3 simultaneamente.

# Crie uma função que receba uma lista de números inteiros e retorne um dicionário onde as chaves 
# são os números e os valores são a soma dos seus múltiplos menores que 50.

