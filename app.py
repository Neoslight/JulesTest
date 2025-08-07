from flask import Flask, render_template, url_for, request, redirect
from src.models import db, Country, Event
import config
import datetime

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    """Main page, displays a list of countries."""
    countries = Country.query.order_by(Country.name).all()
    return render_template('index.html', countries=countries)

@app.route('/country/<country_name>')
def country_events(country_name):
    """Displays events for a specific country, with optional year filtering."""
    country = Country.query.filter_by(name=country_name).first_or_404()

    query = Event.query.filter_by(country_id=country.id)

    start_date_str = request.args.get('start_date', '')
    end_date_str = request.args.get('end_date', '')

    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date() if start_date_str else None
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date() if end_date_str else None

    if start_date:
        query = query.filter(Event.date_start >= start_date)
    if end_date:
        query = query.filter(Event.date_start <= end_date)

    events = query.order_by(Event.date_start).all()

    return render_template('country_events.html',
                           country=country,
                           events=events,
                           start_date=start_date_str,
                           end_date=end_date_str)

@app.route('/add', methods=['GET', 'POST'])
def add_event():
    """Handles adding a new event."""
    if request.method == 'POST':
        country_name = request.form.get('country')
        title = request.form.get('title')

        if not country_name or not title:
            # Simple validation, could be improved with flashing messages
            return redirect(url_for('add_event'))

        # Find or create the country
        country = Country.query.filter_by(name=country_name).first()
        if not country:
            country = Country(name=country_name)
            db.session.add(country)
            db.session.commit()

        # Convert date strings to date objects, handling empty strings
        date_start_str = request.form.get('date_start')
        date_end_str = request.form.get('date_end')
        date_start = datetime.datetime.strptime(date_start_str, '%Y-%m-%d').date() if date_start_str else None
        date_end = datetime.datetime.strptime(date_end_str, '%Y-%m-%d').date() if date_end_str else None

        # Convert lat/lon to float, handling empty strings
        lat_str = request.form.get('location_latitude')
        lon_str = request.form.get('location_longitude')
        lat = float(lat_str) if lat_str else None
        lon = float(lon_str) if lon_str else None

        # Create the new event
        new_event = Event(
            title=title,
            description=request.form.get('description'),
            date_start=date_start,
            date_end=date_end,
            date_descriptor=request.form.get('date_descriptor'),
            location_name=request.form.get('location_name'),
            location_latitude=lat,
            location_longitude=lon,
            event_type=request.form.get('event_type'),
            era=request.form.get('era'),
            country_id=country.id
        )
        db.session.add(new_event)
        db.session.commit()

        return redirect(url_for('country_events', country_name=country.name))

    return render_template('add_event.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
