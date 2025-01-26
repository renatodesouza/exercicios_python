nome = 'python'

#Todas maiusculas
print(nome.upper())

#------------------------------------------------
nome = 'PYTHON'

#Todas minusculas
print(nome.lower())

#------------------------------------------------
#Primeira letra maiuscula
print(nome.capitalize())

#------------------------------------------------
nome = 'titulo'
#Primeira letra maiuscula
print(nome.title())

#------------------------------------------------
#Todas as letras maiusculas
print(nome.swapcase())

#-----------------------------------------------------------------------
# removendo espaços
nome = '***   renato   ***'

#O método strip remove quando nao passamos nehum argumento ira remover os espacos no inicio e final
#no caso abaixo ele não irá remover por que os espacos estao no meio da string
print(nome.strip())

#Remove todos os espaços e *
print(nome.strip(' *'))

#Remove todos os * os espaços ficam
print(nome.strip('*'))

#Remove todos os * e espacos do lado esquerdo
print(nome.lstrip('* '))

#Remove todos os * do lado direito os espacos ficam
print(nome.rstrip('*'))

#---------------------------------------

mensagem = '   ola, mundo'

print(mensagem.strip())

#------------------------------------------------
#Neste caso o metodo strip recebe os argumentos que deve remover, mas irá somente remover
#os argumetos encontrados no inicio e final
texto = "---Python é incrível!---"
texto_limpo = texto.strip("-!")
print(texto_limpo)  # Saída: "Python é incrível"
