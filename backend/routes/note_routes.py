from flask import Blueprint, request,jsonify
from services.note_service import add_note_logic, get_notes_logic,update_note_logic, delete_note_logic

note_routes = Blueprint("note_routes", __name__)

@note_routes.route("/notes", methods=["GET"])
def get_notes():
    return get_notes_logic()

@note_routes.route("/notes", methods=["POST"])
def add_note():
    return add_note_logic(request)

@note_routes.route("/notes/<id>", methods=["PUT"])
def update_note(id):
    return update_note_logic(id, request)

@note_routes.route("/notes/<id>", methods=["DELETE"])
def delete_note(id):
    return delete_note_logic(id)