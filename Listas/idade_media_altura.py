# Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

#Armazenar a idade e alturas dos alunos
import random

idades = [random.randint(10, 18) for _ in range(30)]

alturas = [round(random.uniform(1.40, 1.90), 2) for _ in range(30)]

alunos = list(zip(idades, alturas))

print(alunos)

for aluno in alunos:
    print(aluno)

