from flask import Flask
from flask_cors import CORS
from extensions import db
from routes.note_routes import note_routes
from models.note_model import Note

from dotenv import load_dotenv  # 👈 for .env
from config import Config       # 👈 for config class

load_dotenv()  # 🔐 Load env vars from .env

app = Flask(__name__)
app.config.from_object(Config)  # 👈 Apply config class

CORS(app, origins=["https://note-frontend-9vcp.onrender.com"])

db.init_app(app)

app.register_blueprint(note_routes)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
