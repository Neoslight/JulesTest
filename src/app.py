from flask import Flask, render_template, url_for, request, redirect
from src.models import db, Country, Event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

    start_year_str = request.args.get('start_year', '')
    end_year_str = request.args.get('end_year', '')

    start_year = int(start_year_str) if start_year_str.isdigit() else None
    end_year = int(end_year_str) if end_year_str.isdigit() else None

    if start_year:
        query = query.filter(Event.year >= start_year)
    if end_year:
        query = query.filter(Event.year <= end_year)

    events = query.order_by(Event.year).all()

    return render_template('country_events.html',
                           country=country,
                           events=events,
                           start_year=start_year or '',
                           end_year=end_year or '')

@app.route('/add', methods=['GET', 'POST'])
def add_event():
    """Handles adding a new event."""
    if request.method == 'POST':
        country_name = request.form['country']
        year_str = request.form['year']
        event_desc = request.form['event']

        if not country_name or not year_str.isdigit() or not event_desc:
            # Simple validation, could be improved with flashing messages
            return redirect(url_for('add_event'))

        year = int(year_str)

        # Find or create the country
        country = Country.query.filter_by(name=country_name).first()
        if not country:
            country = Country(name=country_name)
            db.session.add(country)
            db.session.commit()

        # Create the new event
        new_event = Event(year=year, event=event_desc, country_id=country.id)
        db.session.add(new_event)
        db.session.commit()

        return redirect(url_for('country_events', country_name=country.name))

    return render_template('add_event.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
