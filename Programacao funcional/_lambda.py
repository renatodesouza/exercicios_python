#Funções lambdas são funções anonimas que podem ter varias expressões mas escritas em uma unica linha

#lambda argumentos: expressão

#Exemplo de função que dobra um número
def dobrar(x):
    return x * 2

print(f'Utilizando uma função tradicional. {dobrar(2)}')

#Utilizando lambda
dobrar = lambda x: x * 2

print(f'Utilizando lambda. {dobrar(5)}')
