import json
import os
from app import app
from src.models import db, Country, Event

def migrate_data():
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass  # It already exists

    with app.app_context():
        # Create the database and tables
        db.create_all()

        # Clear existing data to avoid duplicates on re-run
        Event.query.delete()
        Country.query.delete()
        db.session.commit()

        # Load data from JSON file
        try:
            with open('data/events.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Error: data/events.json not found. Cannot migrate data.")
            return

        # Populate the database
        for country_name, events_data in data.items():
            country = Country.query.filter_by(name=country_name).first()
            if not country:
                country = Country(name=country_name)
                db.session.add(country)
                db.session.commit()

            for event_data in events_data:
                event = Event(
                    year=event_data['year'],
                    event=event_data['event'],
                    country_id=country.id
                )
                db.session.add(event)

        db.session.commit()
        print("Database has been created and populated with data.")

if __name__ == '__main__':
    migrate_data()
