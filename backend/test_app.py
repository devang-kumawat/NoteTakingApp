import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_get_notes(client):
    response = client.get('/notes')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_add_note(client):
    sample_note = {
        "id": "1",
        "text": "Test note",
        "color": "#ffffff",
        "time": 9999
    }
    response = client.post('/notes', json=sample_note)
    assert response.status_code == 201
    assert response.get_json()["id"] == "1"

def test_update_note(client):
    # Add the note first
    client.post('/notes', json={
        "id": "1",
        "text": "Original",
        "color": "#ffffff",
        "time": 0
    })

    updated_data = {
        "text": "Updated Note",
        "color": "#000000",
        "time": 123456789
    }
    response = client.put("/notes/1", json=updated_data)
    assert response.status_code == 200
    assert response.get_json()["text"] == "Updated Note"

def test_update_note_not_found(client):
    updated_data = {
        "text": "Doesn't matter",
        "color": "#000000",
        "time": 123456789
    }
    response = client.put("/notes/9999", json=updated_data)
    assert response.status_code == 404

def test_delete_note(client):
    client.post("/notes", json={
        "id": "temp",
        "text": "temp",
        "time": 0,
        "color": "#fff"
    })

    response = client.delete("/notes/temp")
    assert response.status_code == 204

def test_delete_note_not_found(client):
    response = client.delete("/notes/does-not-exist")
    assert response.status_code == 404

