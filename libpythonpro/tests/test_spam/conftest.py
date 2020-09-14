import pytest

from libpythonpro.spam.db import Conexao


# fixtures que estarão disponíveis para todos os modulos dentro do pacote test_spam

@pytest.fixture(scope='session')
def conexao():
    #  Setup
    conexao_obj = Conexao()  # gerencia a autenticação (login e senha)
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    # Setup
    sessao_obj = conexao.gerar_sessao()  # efetua as operações (CRUD)
    yield sessao_obj
    #  Tear Down
    sessao_obj.roll_back()
    sessao_obj.fechar()
