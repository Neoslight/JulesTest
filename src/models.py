from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    events = db.relationship('Event', backref='country', lazy=True)

    def __repr__(self):
        return f'<Country {self.name}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    event = db.Column(db.String(255), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

    def __repr__(self):
        return f'<Event {self.year} - {self.event}>'
