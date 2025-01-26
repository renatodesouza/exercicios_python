from functools import reduce

#Dada a lista numeros = [3, 6, 9, 12], use map() para calcular o triplo de cada número.

lista = [3, 6, 9, 12]

print(list(map(lambda x: x * 3, lista)))

#Melhorando e exercicio acima com list comprehension
triplicados = [x * 3 for x in lista]
print(f'Utilizando list comprehension {triplicados}')

#Dada a lista idades = [15, 22, 30, 17, 40], use filter() para encontrar apenas as idades maiores ou iguais a 18.

idades = [15, 22, 30, 17, 40]

print(list(filter(lambda x: x >= 18, idades)))

#Melhorando o exercicio acima com list comprehension
maiores_de_idade = [x for x in idades if x >= 18]

print(f'Idades maiores ou iguais a 18: {maiores_de_idade}')

#Dada a lista numeros = [4, 5, 2, 8], use reduce() para encontrar o produto de todos os números.

numeros = [4, 5, 2, 8]

produto_total = reduce(lambda x, y: x * y, numeros)

print(produto_total)