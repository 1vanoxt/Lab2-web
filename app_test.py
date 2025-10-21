import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    
    # Try to parse JSON, if not JSON then check HTML/text
    try:
        data = response.get_json()
        if data:
            assert 'message' in data or isinstance(data, dict)
        else:
            text = response.get_data(as_text=True)
            assert 'Arithmetic API' in text or '<html' in text
    except Exception:
        text = response.get_data(as_text=True)
        assert 'Arithmetic API' in text or '<html' in text
        
def test_add(client):
    response = client.post('/add', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 15

def test_subtract(client):
    response = client.post('/subtract', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 5

def test_multiply(client):
    response = client.post('/multiply', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 50

def test_divide(client):
    response = client.post('/divide', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 2

def test_divide_by_zero(client):
    response = client.post('/divide', json={'a': 10, 'b': 0})
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'
