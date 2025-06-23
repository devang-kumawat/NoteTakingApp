from flask import jsonify, request

from models.note_model import Note
from extensions import db
notes = []  # In-memory storage

def get_notes_logic():
    notes = Note.query.all()
    result = [
        {"id": note.id, "text": note.text, "time": note.time, "color": note.color}
        for note in notes
    ]
    return jsonify(result), 200

def add_note_logic(request):

    data = request.get_json()
    new_note = Note(
        id = data['id'],
        text=data["text"],
        time=data["time"],
        color=data["color"]
    )
    db.session.add(new_note)
    db.session.commit()
    return jsonify(data), 201

def update_note_logic(id, request):
    data = request.get_json()
    note = db.session.get(Note, id)
    if not note:
        return jsonify({"error": "Note not found"}), 404
    
    note.text = data["text"]
    note.time = data["time"]
    note.color = data["color"]

    db.session.commit()

    return jsonify({
        "id": note.id,
        "text": note.text,
        "time": note.time,
        "color": note.color
    }), 200

def delete_note_logic(id):
    note = db.session.get(Note, id)

    if not note:
        return jsonify({"error": "Note not found"}), 404

    db.session.delete(note)
    db.session.commit()
    return "", 204
