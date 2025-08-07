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
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Date fields
    date_start = db.Column(db.Date, nullable=True)
    date_end = db.Column(db.Date, nullable=True)
    date_descriptor = db.Column(db.String(100), nullable=True) # e.g., "Summer 1944"

    # Location fields
    location_name = db.Column(db.String(200), nullable=True)
    location_latitude = db.Column(db.Float, nullable=True)
    location_longitude = db.Column(db.Float, nullable=True)

    # Categorization
    event_type = db.Column(db.String(100), nullable=True) # e.g., "Battle", "Treaty"
    era = db.Column(db.String(100), nullable=True)

    # Foreign Key
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

    def __repr__(self):
        return f'<Event {self.title}>'
