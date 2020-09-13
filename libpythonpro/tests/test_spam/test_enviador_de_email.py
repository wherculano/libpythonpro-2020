from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar_email(
        'wagherculano@hotmail.com',
        'renzo@python.pro.br',
        'Aula sobre TDD',
        'Criando primeiro TDD com Baby Steps')
    assert 'wagherculano@hotmail.com' in resultado
