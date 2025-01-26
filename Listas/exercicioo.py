
import itertools

# Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
# compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = [x for x in range(10)]

vetor2 = [x for x in range(10, 20)]

vetor3 = []

#Solucao 1

for i in range(len(vetor1)):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(vetor3)


#Solucao 2
vetor4 = [(vetor1[i], vetor2[i]) for i in range(len(vetor1))]

vetor4 = list(itertools.chain(*zip(vetor1, vetor2)))


print(vetor4)


# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor5 = list(itertools.chain(*zip(vetor1, vetor2, vetor4)))

print(f'Esse é o vetor 5: {vetor5}')