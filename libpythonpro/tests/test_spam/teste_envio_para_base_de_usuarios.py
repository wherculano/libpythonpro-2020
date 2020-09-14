from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'wagherculano@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
    assert len(usuarios) == enviador.enviar_email.call_count  # verifica quantas vezes o metodo foi chamado


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Wagner", email="wagherculano@hotmail.com")
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'herculano@example.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
    enviador.enviar_email.assert_called_once_with(
        # verifica se o metodo foi chamado apenas uma vez com estes parametros
        'herculano@example.com',
        'wagherculano@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
