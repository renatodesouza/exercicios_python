# Foram anotadas as idades e alturas de 30 alunos. 
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

import random

idades = [random.randint(11, 17) for i in range(30)]

altura = [random.uniform(1.40, 1.70) for i in range(30)]

altura_arredondado = [round(altura, 2) for altura in altura]

media_alturas = sum(altura_arredondado) / len(altura_arredondado)

lista_alunos = [par for par in zip(idades, altura_arredondado)]

alunos = [idade for idade in range(len(idades)) if idades[idade] < media_alturas]




print(alunos)

print(lista_alunos)

print(round(media_alturas, 2))