# Liste os anos bissextos em um intervalo de anos.
# Crie um programa que receba dois anos como entrada (início e fim) 
# e exiba todos os anos bissextos nesse intervalo, inclusive os limites.

import calendar
from datetime import datetime

#calendar isleap

def verifica_anos_bissextos_em_um_intervalo(ano_inicial, ano_final):
    '''Função que verifica a quantidade de anos bissextos entre dois anos'''

    ano_inicial, ano_final = corrige_intervalo(ano_inicial, ano_final)
    print(ano_inicial, ano_final)
    return[ano for ano in range(ano_inicial, ano_final + 1) if calendar.isleap(ano)]


def verifica_tipos(ano_inicial, ano_final):
    '''Função que verifica se os anos inicial e final são do tipo inteiro
        Parâmetros:
        ano_inicial (int): O ano inicial.
        ano_final (int): O ano final.

        Retorna:
        tuple: Os anos inicial e final, caso sejam válidos.

        Exceção:
        TypeError: Se algum dos valores não for um inteiro.'''
    if not isinstance(ano_inicial, int) or not isinstance(ano_final, int):
        raise TypeError("Os valores passados devem do tipo inteiro, um ano valido '2020'")
    return ano_inicial, ano_final


def corrige_intervalo(ano_inicial, ano_final):
    '''Função que verifica se o ano inicial é maior que o ano final,
        e caso seja verdade troca os valores para o calculo ser feito corretamente'''
    ano_inicial, ano_final = verifica_tipos(ano_inicial, ano_final)

    if ano_inicial > ano_final:
        ano_inicial, ano_final = ano_final, ano_inicial
    return ano_inicial, ano_final

        

ano_inicial = 2050
ano_final = 2024

print(verifica_anos_bissextos_em_um_intervalo(ano_inicial, ano_final))

# for ano in range(ano_inicial, ano_final + 1, 1):
#     if calendar.isleap(ano):
#         print(f'O ano {ano} é uma ano bissexto.')

