#Para remover caracteres que estão no meio da string
#podemos utilizar replace()

#Onde passamos para o replace dois argumentos, o primeiro é o caracter que queremos
#remover e o segunto o caracter pelo qual queremos substituir pode ser tambem uma string vazia

#String vazia
string = 'python é incri3vel'

nova_string = string.replace('3', '')

print(nova_string)

#-----------------------------------------------------------

#Aqui passamos o cracter '3' que sera substituido pelo 'i'
string = 'python é incr3vel'

nova_string = string.replace('3', 'i')

print(nova_string)