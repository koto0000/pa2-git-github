import pytest
from app import app

@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_add_task_and_list(client):
    # Add a task
    resp = client.post('/add', data={'text': 'Tarea de prueba'}, follow_redirects=True)
    assert resp.status_code == 200
    # Check it appears
    assert b'Tarea de prueba' in resp.data
