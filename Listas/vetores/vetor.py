# Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos 
# pelos elementos intercalados dos dois outros vetores.

vetor_um = [x for x in range(10)]

vetor_dois = [x for x in range(10, 20)]

vetor = []

for i in range(len(vetor_um)):
    vetor.append(vetor_um[i])
    vetor.append(vetor_dois[i])

#Solução dois

vet = [elem for par in zip(vetor_um, vetor_dois) for elem in par]

print('Solucao 1')

print(vetor)

print('Solucao 2')

print(vet)