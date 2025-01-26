#A função map aplica uma função a todos os elemetos de um iteravel

numeros = [1, 2, 3, 4, 5]

print(list(map(lambda x: x * 2, numeros)))

print(list(map(lambda x: x ** 2, numeros)))