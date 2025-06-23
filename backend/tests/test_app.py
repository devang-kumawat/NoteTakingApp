import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from extensions import db
from models.note_model import Note

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # in-memory test DB
    with app.app_context():
        db.create_all()
    client = app.test_client()
    yield client
    with app.app_context():
        db.drop_all()  # cleanup

def test_add_note(client):
    sample = {
        "id": "test1",
        "text": "test note",
        "time": 123456,
        "color": "#ffffff"
    }
    res = client.post("/notes", json=sample)
    assert res.status_code == 201
    assert res.get_json()["id"] == "test1"

def test_get_notes(client):
    res = client.get("/notes")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_update_note(client):
    updated = {
        "text": "Updated",
        "time": 654321,
        "color": "#000000"
    }
    client.post("/notes", json={"id": "test2", "text": "Old", "time": 1, "color": "#fff"})
    res = client.put("/notes/test2", json=updated)
    assert res.status_code == 200
    assert res.get_json()["text"] == "Updated"

def test_delete_note(client):
    client.post("/notes", json={"id": "test3", "text": "temp", "time": 0, "color": "#ccc"})
    res = client.delete("/notes/test3")
    assert res.status_code == 204
