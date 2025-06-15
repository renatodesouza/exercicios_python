import re


texto = "Meu numero é 12345"

# \d digitos de 0 a 9
# + mais de um digito

resultado = re.search(r"\d+", texto)

if resultado:
    print(f'Encontrado: {resultado.group()}')


resultado = re.search(r'\w+', texto)

if resultado:
    print(f'Resultado: {resultado.group()}')

#re.math verifica se o padrao ocorre no inico do string

resultado = re.match(r"Meu", texto)

if resultado:
    print(f'O texto começa com "Meu": {resultado.group()}')


#re.findall() retorna todas as ocorrencias de um padrao em uma lista

texto = "Tenho 3 cachorros e 2 gatos"

numeros = re.findall(r'\d+', texto)

print(f'Os números encontrados são: {numeros}')

#re.sub() substitui a ocorrencias do padrao por um valor

texto = "O preço é 100 reais ou pode ser parcelado por 10 x de 10"

novo_texto = re.sub(r'\d+', 'xxx', texto)

print(novo_texto)



