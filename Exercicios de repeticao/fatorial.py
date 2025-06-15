# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input("Informe um número para calcular seu fatorial: "))



for i in range(numero - 1, 0, -1):
   numero *= i

print(numero)

