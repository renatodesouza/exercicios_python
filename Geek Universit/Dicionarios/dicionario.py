paises = {'br':'brasil', 'usa':'estados unidos', 'ag':'argentina'}


#Acessando valores atraves das chaves

print(paises['br'])

print(paises['ag'])

#Usando o metodo get para acessar os valores do dicionario
print(f"{'':-<10}Com o metodo get{'':->10}")

print(paises.get('br'))

print(paises.get('usa'))