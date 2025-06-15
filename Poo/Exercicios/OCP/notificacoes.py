from abc import ABC, abstractmethod


class Notificacao(ABC):
    @abstractmethod
    def notificar(self, mensagem):
        pass

class Email(Notificacao):
    def notificar(self, mensagem):
        return f'{mensagem} por email.'
        

class Sms(Notificacao):
    def notificar(self, mensagem):
        return f'{mensagem} por sms'

class Push(Notificacao):
    def notificar(self, mensagem):
        return f'{mensagem} por push'

class GerenciadorDeNotificacoes:
    '''A notação : list[Notificacao] diz que canais devem ser uma 
    lista que iram implementar uma interface de Noficação'''
    def __init__(self, canais: list[Notificacao]):
        self._canais = canais

    def enviar_para_todos(self, mensagem):
        resultados = []
        '''Cada canal é uma interface de Notificacao ou instancia de Email, Sms e Push'''
        for canal in self._canais:
            resultados.append(canal.notificar(mensagem))
        return resultados

email = Email()
sms = Sms()
push = Push()

gerenciador = GerenciadorDeNotificacoes([email, sms, push])

respostas = gerenciador.enviar_para_todos("olá estou enviando a mensagem")

for r in respostas:
    print(r)