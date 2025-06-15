class Email():
    def enviar(self, mensagem):
        print(f'Email enviado com sucesso {mensagem}')

class Sms():
    def enviar(self, mensagem):
        print(f'SMS enviado com sucesso: {mensagem}')

class Notificador:
    def __init__(self, servico_envio):
        self._servico_envio = servico_envio

    def notificar(self, msg):
        self._servico_envio.enviar(msg)



email = Email()
sms = Sms()
notificador = Notificador(email)

notificador2 = Notificador(sms)

notificador.notificar('Bem vindo')

notificador2.notificar('Bem vindo')


