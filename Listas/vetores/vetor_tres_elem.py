# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.


vetor_um = [x for x in range(10)]

vetor_dois = [x for x in range(10, 20)]

vetor_impar = [x for x in range(20) if x % 2 != 0]


resultado = [elem for par in zip(vetor_impar, vetor_dois, vetor_um) for elem in par]

print(resultado)
