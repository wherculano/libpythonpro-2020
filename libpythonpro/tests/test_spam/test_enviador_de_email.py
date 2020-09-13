import pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com', 'wagherculano@hotmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar_email(
        remetente,
        'renzo@python.pro.br',
        'Aula sobre TDD',
        'Criando primeiro TDD com Baby Steps')
    assert remetente in resultado
