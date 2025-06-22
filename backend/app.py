from flask import Flask
from flask_cors import CORS
from extensions import db
from routes.note_routes import note_routes

app = Flask(__name__)
CORS(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from models.note_model import Note  # ✅ After db.init_app

app.register_blueprint(note_routes)

with app.app_context():
    db.create_all()
    

if __name__ == '__main__':
    app.run(debug=True)

