#Você vai implementar um sistema de cálculo de imposto para diferentes tipos de produtos em um e-commerce.

from abc import ABC, abstractmethod

class Imposto(ABC):
    @abstractmethod
    def calcular(self, preco):
        pass

class Eletronico(Imposto):
    def calcular(self, preco):
        return preco * 0.15
    
class Alimento(Imposto):
    def calcular(self, preco):
        return preco * 0.05
    
class Vestuario(Imposto):
    def calcular(self, preco):
        return preco * 0.12
    

#Uma classe GerenciadorImpostos (ou similar) que receba via injeção de dependência uma
#  lista de objetos Imposto e aplique todos eles a um determinado produto
#  (ou escolha o correto por alguma lógica externa).

class GerenciadorImpostos:
    def __init__(self, imposto: list[Imposto]):
        self._imposto = imposto
        
    def aplicar_para_todos(self, preco):
        resultado = []
        for imposto in self._imposto:
            resultado.append(imposto.calcular(preco))
        return resultado

alimentos = {'arroz':30, 'feijao':10}

eletronico = Eletronico()
alimento = Alimento()
vestuario = Vestuario()

gerenciador = GerenciadorImpostos([eletronico, alimento, vestuario])

respostas = gerenciador.aplicar_para_todos(50)

for r in respostas:
    print(r)