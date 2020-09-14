class Enviador:
    def enviar_email(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Endereço de email inválido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass
