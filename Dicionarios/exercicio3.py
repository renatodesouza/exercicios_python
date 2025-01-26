# Dicionários
# Crie um dicionário com 3 pares chave-valor e exiba todos os valores.
dici = {'nome':'renato', 'idade': 40, 'peso':80}

print(dici)

# Adicione um novo par chave-valor a um dicionário existente.
dici['altura'] = 1.88

print(dici)

# Remova um item de um dicionário.
dici.pop('idade')
print(dici)

# Verifique se uma chave está presente em um dicionário.

print('nome' in dici)

# Mescle dois dicionários em um.
dici1 = {'chave1':'valor1'}

dici2 = {'chave2':'valor2'}

dici1.update(dici2)

print(dici1)


# Exiba todas as chaves de um dicionário.
print(dici1.keys())

# Inverta as chaves e valores de um dicionário.
dici = {'chave':'um', 'chave2':'dois'}

novo_dici = {valor:chave for chave, valor in dici.items()}

print('---------Inverte valores e chaves---------------')

print(novo_dici)

# Dado um dicionário de nomes e idades, exiba o nome da pessoa mais velha.
pessoas = {'nome':'renato', 'idade':40, 'nome':'lucas', 'idade':35}



# Crie um dicionário onde as chaves são números de 1 a 5 e os valores são seus respectivos quadrados.
#Solução 1
dic = {}
for i in range(1, 6):
    dic[i] = i ** 2

print(dic)

#Solução 2

dic = {i: i ** 2 for i in range(1, 6)}

print(dic)

# Converta duas listas (uma de chaves e outra de valores) em um dicionário.
chaves = [i for i in range(1, 6)]

valores = [i ** 2 for i in range(1, 6)]

dici = {}

for i in range(1, len(chaves)):
    dici[chaves[i]] = valores[i]

print(dici)

# Dado um dicionário de produtos e seus preços, encontre o produto mais caro.


# Atualize o valor de uma chave existente em um dicionário.
dici = {'chave':'valor'}

dici['chave'] = 'valor2' 

print(dici)

# Dado um dicionário, crie uma lista de todas as chaves.
dici = {i: i**2 for i in range(1, 10)}

#Solucao 1
print(list(dici))

#Solucao 2
lista = [k for k in dici.keys()]

# for k in dici.keys():
#     lista.append(k)

print(lista)

# Encontre o tamanho de um dicionário.
print(len(dici))

# Dado um dicionário de nomes e idades, crie uma lista de nomes das pessoas com idade maior que 30.

# Faça a união de dois dicionários, somando os valores das chaves comuns.

# Converta um dicionário em uma lista de tuplas.
# Ordene um dicionário pelas chaves.
# Dado um dicionário de palavras e suas frequências, encontre a palavra mais frequente.
# Crie um dicionário a partir de uma string, onde as chaves são os caracteres e os valores são suas frequências na string.