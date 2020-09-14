import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome="Wagner", email="wagherculano@hotmail.com"),
            Usuario(nome="Herculano", email="wagherculano@hotmail.com")
        ],
        [
            Usuario(nome="Wagner", email="wagherculano@hotmail.com"),
        ],
    ]
)
def test_envio_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'wagherculano@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
    assert len(usuarios) == enviador.qtde_emails_enviados
