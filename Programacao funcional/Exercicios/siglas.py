#Use map() para gerar siglas com as primeiras letras de cada palavra.
preposicoes = ["da", "de", "do", "e"]

def gera_siglas(frase):
    return "".join([palavra[0] for palavra in frase.split() if palavra.lower() not in preposicoes])


estados = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia", "Paraná"]


print(f'As siglas dos estados: {list(map(gera_siglas, estados))}')

# 2️⃣ Siglas de Empresas
# Dada a lista de nomes de empresas:

# empresas = ["Companhia Brasileira de Petróleo", "Banco Nacional de Crédito", "Associação de Tecnologia e Pesquisa"]
# Use map() para criar siglas com a primeira letra de cada palavra, ignorando palavras pequenas como "de", "da", "do", "e".


empresas = ["Companhia Brasileira de Petróleo", "Banco Nacional de Crédito", "Associação de Tecnologia e Pesquisa"]

print(f'As siglas das empresas é: {list(map(gera_siglas, empresas))}')


# 3️⃣ Siglas de Cursos Universitários
# Dada a lista de cursos:

# cursos = ["Engenharia da Computação", "Administração de Empresas", "Ciência de Dados", "Letras Português"]
# Use map() para gerar siglas com as iniciais de cada palavra relevante.

cursos = ["Engenharia da Computação", "Administração de Empresas", "Ciência de Dados", "Letras Português"]

print(f'As siglas dos cursos são: {list(map(gera_siglas, cursos))}')

# 4️⃣ Siglas de Nomes Próprios
# Dada a lista de nomes completos:

# nomes = ["Carlos Eduardo da Silva", "Ana Beatriz Ramos", "Fernando Henrique Cardoso"]
# Use map() para criar siglas com as iniciais de cada nome, ignorando conectores como "da" e "de".

# 📌 Exemplo esperado:

# "Carlos Eduardo da Silva" → "CES"
# "Ana Beatriz Ramos" → "ABR"
# "Fernando Henrique Cardoso" → "FHC"

nomes = ["Carlos Eduardo da Silva", "Ana Beatriz Ramos", "Fernando Henrique Cardoso"]

nomes_completos = [nome[0] for nome in nomes[0].split() if nome.lower() not in preposicoes]
print("".join(nomes_completos))
print(f'O resultados é: {nomes_completos}')


print(list(map(gera_siglas, nomes)))

# 5️⃣ Siglas de Países Compostos
# Dada a lista de nomes de países compostos:

# paises = ["Reino Unido", "Estados Unidos", "Nova Zelândia", "África do Sul"]
# Use map() para criar siglas com as primeiras letras de cada palavra importante.

# 📌 Exemplo esperado:

# "Reino Unido" → "RU"
# "Estados Unidos" → "EU"
# "Nova Zelândia" → "NZ"
# "África do Sul" → "AS"

paises = ["Reino Unido", "Estados Unidos", "Nova Zelândia", "África do Sul"]

print(list(map(lambda frase: "".join([palavra[0] for palavra in frase.split() if palavra.lower() not in preposicoes]), paises)))

#Solução dois

print(f'Solucao com a funcao gera_siglas: {list(map(gera_siglas, paises))}')