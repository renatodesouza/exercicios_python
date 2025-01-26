nome = 'renato'

print('ola %s tudo bem' %nome)

#Chamando funcoes dentro de f-strings
print(f'Olá {nome} o seu nome tem {len(nome)} letras')

preco = 30

#Realizando operacoes matematicas dentro de f-strings
print(f'O valor é: R${preco * 10:7.2f}')


idade = 40

#Utilizando aspas triplas para escrever strings de multiplas linhas

print(f"""
        Meu nome é {nome} eu tenho {idade} 
        anos e meu nome tem 
        {len(nome)} letras
""")

#Formatacao de casas decimais com f-strings

preco = 4.2

print(f'O valor do produto é {preco:.2f}')

valor1 = 12345

valor2 = 2345

print(f'{valor1 / valor2:.2f}')

