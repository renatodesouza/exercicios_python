class A(object):
    def a1(self):
        print('a1')

class B(object):
    def b1(self):
        print('b1')
        #Criando a instancia de A dentro de B
        A().a1()

objetoB = B()

objetoB.b1()

#Exemplo dois
#Ao invés de criar sempre uma nova instância de A dentro de B eu posso injetar a dependência
#por parâmetro ou atributo

class C(object):
    def __init__(self, a_obj=None):
        #aceita um objeto A já criado ou cria um novo
        self._a = a_obj or A()

    def c1(self):
        print('c1')
        self._a.a1()

a_instancia = A()

c = C(a_instancia)

c.c1()


    
