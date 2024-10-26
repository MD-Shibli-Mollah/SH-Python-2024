from flask.testing import FlaskClient
import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_bank(client: FlaskClient):
    response = client.post('/banks', json={
        'name': 'Test Bank',
        'location': 'Test Location'
    })
    assert response.status_code == 201  # Assert successful creation (201 Created)
    data = json.loads(response.data)
    assert data.get('message') == "Bank created successfully"  # Assert success message

def test_get_all_banks(client: FlaskClient):
    response = client.get('/banks')
    assert response.status_code == 200  # Assert successful response (200 OK)
    data = json.loads(response.data)

def test_get_specific_bank(client: FlaskClient):
    response = client.get('/banks/11')
    assert response.status_code == 200  # Assert successful response (200 OK)
    data = json.loads(response.data)
    assert data.get('name') == 'Capital One'  # Assert Bank Name

def test_update_bank(client: FlaskClient):
    response = client.put('/banks/24', json={
        'name': 'Updated Bank',
        'location': 'Updated Location'
    })
    assert response.status_code == 200  # Assert successful update (200)
    data = json.loads(response.data)
    assert data.get('message') == "Bank updated successfully"  # Assert success message

def test_delete_bank(client: FlaskClient):
    response = client.delete('/banks/21')
    assert response.status_code == 200  # Assert successful Deletion (200)
    data = json.loads(response.data)
    assert data.get('message') == "Bank deleted successfully"  # Assert success message