from extensions import db

class Note(db.Model):
    id = db.Column(db.String, primary_key=True)
    text = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    time = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "color": self.color,
            "time": self.time
        }
