# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# Escreva um programa que, além de fazer as perguntas sobre o crime, 
# também armazene as respostas do usuário em uma lista e exiba todas as respostas no final.

perguntas = ['Telefonou para a vitíma', 'Esteve no local do crime', 'Mora perto da vitíma', 'Devia para a vitíma', 'Já trabalhou com a vítima']

respostas = []

sim = 0

nao = 0

print("Responda 's' para sim e 'n' para não: ")

for i in range(len(perguntas)):
    resposta = input(f'{perguntas[i]}: ').upper()
    
    respostas.append(resposta)

    if resposta == 'S':
        sim += 1
    else:
        nao += 1


if sim == 2:
    print('Você é considerado suspeito pelo crime. ')
elif sim == 3 or sim == 4:
    print('Você é considerado Cúmplice pelo crime. ')
elif sim == 5:
    print('Você é considerado Assassino pelo crime. ')
else:
    print('Você é considerado INOCENTE. ')

print('Suas respostas foram: ')

for r in range(len(respostas)):
    print(f'{perguntas[r]}: {respostas[r]}')