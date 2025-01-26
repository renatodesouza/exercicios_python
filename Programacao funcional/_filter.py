#A função filter filtra os elementos de um iteravel com base em uma condição

numeros = [1, 2, 3, 4, 5, 6]

#Filtrando todos os elementos da lista numeros que são pares
print(list(filter(lambda x: x % 2 == 0, numeros)))