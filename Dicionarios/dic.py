dic = {'nome':'renato'}

print(dic['nome'])

print(dic.keys())

print(dic.values())

from pprint import pprint

pprint(dir(dic))

('clear',
 'copy',
 'fromkeys',
 'get',
 'items',
 'keys',
 'pop',
 'popitem',
 'setdefault',
 'update',
 'values')

print(dic.get('nome'))

#Remove os itens do dicionario retornando o valor da chave
print(dic.pop('nome'))

#Remove os itens de um dicionario retornando uma tupla com chave e valor
#print(dic.popitem())

#Adiciona uma nova chave valor ao dicionario
dic['sobrenome'] = 'lucas'

print(dic.get('sobrenome'))

#Atualiza chave ou valor do dicionario
dic.update({'sobrenome':'Souza'})

print(dic)