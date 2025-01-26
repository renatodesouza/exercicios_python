# Contador de Palavras:
# Crie um programa que leia um texto e conte a frequência de cada palavra, 
# armazenando as informações em um dicionário. No final, exiba as palavras e suas respectivas quantidades.

texto = 'Meu texto esta aqui'

palavras = texto.split()

for i in range(len(palavras)):
    print(palavras.count(palavras[i]))