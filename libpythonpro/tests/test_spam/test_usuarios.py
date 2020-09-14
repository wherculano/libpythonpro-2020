from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome="Wagner", email="wagherculano@hotmail.com")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome="Wagner", email="wagherculano@hotmail.com"),
                Usuario(nome="Herculano", email="wagherculano@hotmail.com")]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
