# Historical Events Web App

This is a web application to discover and manage historical events for various countries.

## Project Structure

```
.
├── app.py
├── data
│   └── events.json
├── instance
│   └── events.db
├── src
│   ├── __init__.py
│   ├── data_loader.py
│   ├── models.py
│   ├── static
│   │   └── style.css
│   └── templates
│       ├── add_event.html
│       ├── base.html
│       ├── country_events.html
│       └── index.html
├── migrate_data.py
├── requirements.txt
└── README.md
```

- `app.py`: The main Flask application logic.
- `data/events.json`: Contains the initial historical events data in JSON format.
- `instance/events.db`: The SQLite database file.
- `src/models.py`: Defines the SQLAlchemy database models.
- `src/templates/`: Contains the HTML templates for the web interface.
- `src/static/`: Contains static files like CSS.
- `migrate_data.py`: A script to create the database and populate it with data from `events.json`.
- `requirements.txt`: Lists the Python dependencies for the project.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Initialize the database:**
    Run the migration script to create the database and populate it with the initial data.
    ```bash
    python migrate_data.py
    ```

3.  **Run the web application:**
    ```bash
    python app.py
    ```

4.  Open your web browser and navigate to `http://127.0.0.1:8080`.

## Web Interface

- **Home Page:** The main page displays a list of all countries with available historical data.
- **Country Events Page:** Clicking on a country will take you to a page displaying all its historical events. You can filter the events by a start and end year.
- **Add Event Page:** You can add new historical events with detailed information through the "Add Event" page, which is accessible from the navigation bar.

## Data Model

The application uses a relational database to store information about countries and their historical events.

### Country
- `name`: The name of the country.

### Event
- `title`: The title of the event.
- `description`: A detailed description of the event.
- `event_type`: The type or category of the event (e.g., "Battle", "Treaty").
- `date_start` / `date_end`: The start and end dates for the event, allowing for both precise dates and periods.
- `date_descriptor`: A text field for non-precise dates (e.g., "Summer 1944").
- `location_name`: The name of the location or area.
- `latitude` / `longitude`: Precise coordinates for future mapping features.
- `era`: The historical era (e.g., "Renaissance").
