import pytest
from falcon import testing

import app


@pytest.fixture(scope='module')
def client():
    return testing.TestClient(app.app)


def test_convert(client):
    result = client.simulate_post('/convert')
    assert result.status_code == 200
    assert result.json == {'message': 'Hi'}


def test_convert_method(client):
    assert client.simulate_get('/convert').status_code == 405
    assert client.simulate_put('/convert').status_code == 405
    assert client.simulate_delete('/convert').status_code == 405
