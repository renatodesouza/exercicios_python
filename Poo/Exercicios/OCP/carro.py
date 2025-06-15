from abc import ABC, abstractmethod


class Automovel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Carro(Automovel):
    def ligar(self):
        print(f'Carro ligado')

class Moto(Automovel):
    def ligar(self):
        print(f'Moto ligada')

class Ignicao:
    def __init__(self, automovel: Automovel):
        self.automovel = automovel

    def girar_chave(self):
        self.automovel.ligar()

carro = Moto()

ignicao = Ignicao(carro)

ignicao.girar_chave()