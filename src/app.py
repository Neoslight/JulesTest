from flask import Flask, render_template, url_for, request, redirect
from src.data_loader import load_events, save_events
from src.models import Event

app = Flask(__name__)
events_by_country = load_events('data/events.json')

@app.route('/')
def index():
    """Main page, displays a list of countries."""
    countries = sorted(list(events_by_country.keys()))
    return render_template('index.html', countries=countries)

@app.route('/country/<country_name>')
def country_events(country_name):
    """Displays events for a specific country, with optional year filtering."""
    start_year_str = request.args.get('start_year', '')
    end_year_str = request.args.get('end_year', '')

    start_year = int(start_year_str) if start_year_str.isdigit() else None
    end_year = int(end_year_str) if end_year_str.isdigit() else None

    events = events_by_country.get(country_name, [])
    if start_year:
        events = [e for e in events if e.year >= start_year]
    if end_year:
        events = [e for e in events if e.year <= end_year]

    # Sort events by year
    events.sort(key=lambda e: e.year)

    return render_template('country_events.html',
                           country=country_name,
                           events=events,
                           start_year=start_year or '',
                           end_year=end_year or '')

@app.route('/add', methods=['GET', 'POST'])
def add_event():
    """Handles adding a new event."""
    if request.method == 'POST':
        country = request.form['country']
        year_str = request.form['year']
        event_desc = request.form['event']

        if not country or not year_str.isdigit() or not event_desc:
            # Simple validation, could be improved with flashing messages
            return redirect(url_for('add_event'))

        year = int(year_str)

        event = Event(year=year, event=event_desc)
        if country not in events_by_country:
            events_by_country[country] = []

        events_by_country[country].append(event)
        events_by_country[country].sort(key=lambda e: e.year)
        save_events('data/events.json', events_by_country)

        return redirect(url_for('country_events', country_name=country))

    return render_template('add_event.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
