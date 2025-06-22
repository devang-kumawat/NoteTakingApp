from flask import jsonify, request

notes = []  # In-memory storage

def get_notes_logic():
    return jsonify(notes), 200

def add_note_logic(request):
    note = request.get_json()
    notes.append(note)
    return jsonify(note), 201

def update_note_logic(id, request):
    data = request.get_json()
    for note in notes:
        if note["id"] == id:
            note.update(data)
            return jsonify(note), 200
    return jsonify({"error": "Note not found"}), 404

def delete_note_logic(id):
    global notes
    new_notes = [note for note in notes if note["id"] != id]
    if len(new_notes) == len(notes):
        return jsonify({"error": "Note not found"}), 404
    notes = new_notes
    return "", 204
