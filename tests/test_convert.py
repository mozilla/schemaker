import pytest
from falcon import testing

import app


with open('tests/example.schema.json') as f:
    TEST_SCHEMA = f.read()
with open('tests/example.schema.parquet-mr') as f:
    TEST_PARQUET_MR = f.read()


@pytest.fixture(scope='module')
def client():
    return testing.TestClient(app.app)


def test_happy(client):
    result = client.simulate_post(
        '/convert',
        headers={'content_type': 'application/json'},
        params={'output': 'parquet-mr'},
        body=TEST_SCHEMA
    )
    assert result.status_code == 200
    assert result.json == {'parquet-mr': TEST_PARQUET_MR}


def test_content_type(client):
    result = client.simulate_post('/convert')
    assert result.status_code == 400
    assert result.json == {
        'title': 'Bad request',
        'description': 'Content type must be `application/json`.',
    }

    result = client.simulate_post(
        '/convert',
        headers={'content_type': 'application/json; charset=UTF-8'},
        params={'output': 'parquet-mr'},
        body=TEST_SCHEMA
    )
    assert result.status_code == 200


def test_output_param(client):
    result = client.simulate_post(
        '/convert',
        headers={'content_type': 'application/json; charset=UTF-8'},
        body=TEST_SCHEMA
    )
    assert result.status_code == 400
    assert result.json == {
        'title': 'Bad request',
        'description': 'Invalid or missing output parameter.',
    }


def test_convert_method(client):
    assert client.simulate_get('/convert').status_code == 405
    assert client.simulate_put('/convert').status_code == 405
    assert client.simulate_delete('/convert').status_code == 405
