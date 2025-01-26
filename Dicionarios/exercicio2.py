#Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = {'nome':'renato', 'idade':40, 'cidade':'sao paulo'}

#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);

pessoa['idade'] = 41

#Adicione um campo de profissão para essa pessoa;

pessoa['profissao'] = 'ajudante'

#Remova um item do dicionário.

pessoa.pop('profissao')

print(pessoa)


#Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5

#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
if "idade" in pessoa.keys():
    print('sim')

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = 'Meu nome não é jhony, meu nome é pedro'

lst = frase.split()



