class Enviador:
    def __init__(self):
        self.qtde_emails_enviados = 0

    def enviar_email(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Endereço de email inválido: {remetente}')
        self.qtde_emails_enviados += 1
        return remetente


class EmailInvalido(Exception):
    pass
