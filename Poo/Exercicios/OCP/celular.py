from abc import ABC, abstractmethod


class Celular(ABC):
    @abstractmethod
    def tocar(self):
        pass

class FoneOuvido(Celular):
    def tocar(self):
        print(f'Reproduzindo no fone de ouvido')

class AutoFalante(Celular):
    def tocar(self):
        print(f'Reproduzindo no auto falante externo')

class Reproduzir:
    def __init__(self, celular: Celular):
        self.celular = celular
    
    def play(self):
        self.celular.tocar()

fone = FoneOuvido()

reproduzir = Reproduzir(fone)

reproduzir.play()