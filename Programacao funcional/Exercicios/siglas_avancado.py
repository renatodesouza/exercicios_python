
# Raciocinado por alguns segundos
# Crafting complex acronyms

# I’m developing advanced Portuguese exercises for creating acronyms, focusing on unique structures like disregarding prepositions and using multi-word names. Each exercise will have specific descriptions and expected outputs.

# A seguir, apresento 5 exercícios mais avançados sobre siglas, que vão desafiar seu domínio do tema e o uso de técnicas complementares, como expressões regulares e manipulação de strings com hífens e números. Boa prática!

# Exercício 1: Siglas com Filtro Adicional de Tamanho
# Descrição:
# Dada uma lista de nomes compostos, gere as siglas utilizando a primeira letra de cada palavra, mas ignore:

# Palavras presentes em uma lista de preposições/conectores (por exemplo: "da", "de", "do", "e").
# Palavras que tenham menos de 3 caracteres.

nomes = ["Universidade Federal de Minas Gerais", "Instituto de Pesquisas Tecnológicas", "Escola Técnica de Administração", "Faculdade Impacta de Tecnologia", "Tec Vestuário"]

# Saida ['UFMG', 'IPT', 'ETA']

preposicoes = ["da", "de", "do", "e"]

print(list(map(lambda frase: "".join([palavra[0] for palavra in frase.split() if palavra.lower() not in preposicoes and len(palavra) > 3]), nomes)))

# Exercício 2: Siglas com Inversão de Ordem
# Descrição:
# Dada uma lista de nomes, gere uma sigla para cada nome, mas utilizando a última letra de cada palavra (em vez da primeira) e depois invertendo a ordem dessas letras para formar a sigla.

# Exemplo:
# Entrada:

# nomes = ["Centro de Tecnologia", "Instituto Nacional", "Serviço Público"]
# Saída esperada (convertendo e invertendo as letras):

# Para "Centro de Tecnologia":
# Últimas letras (ignorando palavras como "de" se desejado): "O", "E", "A" → Invertendo: "AEO"
# Para "Instituto Nacional":
# "O", "L" → Invertendo: "LO"
# Para "Serviço Público":
# "O", "O" → Invertendo: "OO"

nomes = ["Centro de Tecnologia", "Instituto Nacional", "Serviço Público"]

print(list(map(lambda frase: "".join([palavra[-1] for palavra in frase.split()])[::-1].upper(), nomes)))


