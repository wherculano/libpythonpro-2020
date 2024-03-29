from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars2.githubusercontent.com/u/26460999?v=4'
    resp_mock.json.return_value = {'login': 'wherculano', 'id': 26460999, 'node_id': 'MDQ6VXNlcjI2NDYwOTk5',
                                   'avatar_url': url,
                                   }

    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    # Teste utilizando Mock sem acesso a internet
    url = github_api.buscar_avatar('wherculano')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    # Teste de Integração utilizando a internet
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url
