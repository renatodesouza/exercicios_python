#A função reduce aplica uma função acumulativo a todos os elementos de um iteravel
# precisamos importar o modulo functools para usar o reduce

from functools import reduce


numeros = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x + y, numeros))