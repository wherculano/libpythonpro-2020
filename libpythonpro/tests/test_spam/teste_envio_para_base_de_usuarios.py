import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtde_emails_enviados = 0
        self.parametros_de_envio = None

    def enviar_email(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtde_emails_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome="Wagner", email="wagherculano@hotmail.com"),
            Usuario(nome="Herculano", email="herculano@example.com")
        ],
        [
            Usuario(nome="Wagner", email="wagherculano@hotmail.com"),
        ],
    ]
)
def test_envio_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'wagherculano@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
    assert len(usuarios) == enviador.qtde_emails_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Wagner", email="wagherculano@hotmail.com")
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'herculano@example.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
    assert enviador.parametros_de_envio == (
        'herculano@example.com',
        'wagherculano@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
