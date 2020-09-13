import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


@pytest.fixture
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


def test_salvar_usuario(sessao):
    usuario = Usuario(nome="Wagner")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome="Wagner"), Usuario(nome="Herculano")]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
