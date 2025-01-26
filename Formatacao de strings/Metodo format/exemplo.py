nome = ' renato'

idade = 40

print('------------Posicionais----------------------')

print('Meu nome é {} e tenho {} anos'.format(nome, idade))

#Exemplo posicionando os elementos com indice
print('Mwu nome é {0} e tenho {1}'.format(nome, idade))

#Exemplo com listas
dados_lista = ['renato', 40, 85.0]

#Explicar o operador de desempacotamento '*'
print('Meu nome é {0} e tenho {1} e meu peso é {2}'.format(*dados_lista))

#Exemplo com tupla
dados_tupla = ('renato', 40, 85.0)
print('Meu nome é {0} e tenho {1} e meu peso é {2}'.format(*dados_tupla))

#Atributos Nomeados

print("---------------Nomedados-----------------------")
nome = 'lucas'

idade = 45

peso = 80.0

print('Meu nome é {nome}, minha idade é {idade} anos e peso {peso}'.format(nome=nome, idade=idade, peso=peso))

#Passando um dicionario para kwargs

dados_dici = {'nome':'renato', 'idade':23, 'peso':84.8}

print('Meu nome é {nome} minha idade é {idade} e peso {peso}'.format(**dados_dici))

#Formatacao avancada
#***Largura do campo {:valor para tamanho da largura}
print('Meu nome é {:10} e minha idade é {}'.format(nome, idade))

#***Alinhamento 
#****** < a esquerda
print('Meu nome é {:<10} e minha idade é {}'.format(nome, idade))

#****** > a direita
print('Meu nome é {:>10} e minha idade é {}'.format(nome, idade))

#****** ^ centralizado
print('Meu nome é {:^10} e minha idade é {}'.format(nome, idade))

#***Preenchimento
#****** {:*}
print('Meu nome é {:*<10} e minha idade é {}'.format(nome, idade))

print('Meu nome é {:*>10} e minha idade é {}'.format(nome, idade))

print('Meu nome é {:*^10} e minha idade é {}'.format(nome, idade))

#***Formatacao de números decimais
#****** {:.2f}

valor = 256.365

print('O valor do produto é de {:.2f}'.format(valor))

print('O valor do produto é de {:>10.2f}'.format(valor))

print('O valor do produto é de {:0>10.2f}'.format(valor))




