# Exercício 3:
# Determine o próximo ano bissexto.
# Faça um programa que receba o ano atual e calcule qual será o próximo ano bissexto a partir dele.

import calendar


def calcula_proximo_ano_bissexto(ano_origem):
    bissexto = [ano for ano in range(ano_origem + 1, ano_origem + 5, 1) if calendar.isleap(ano)]

    return bissexto

ano_origem = 2003

print(calcula_proximo_ano_bissexto(ano_origem))

# for ano in range(ano_origem + 1, ano_origem + 5, 1):
#     if calendar.isleap(ano):
#         print(ano)
#         break
#     else:
#         continue


