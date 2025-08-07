# Historical Events Web App

This is a web application to discover and manage historical events for various countries.

## Project Structure

```
.
├── data
│   └── events.json
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── data_loader.py
│   └── models.py
├── static
│   └── style.css
├── templates
│   ├── add_event.html
│   ├── base.html
│   ├── country_events.html
│   └── index.html
├── requirements.txt
└── README.md
```

- `data/events.json`: Contains the historical events data in JSON format.
- `src/app.py`: The main Flask application logic.
- `src/data_loader.py`: Loads and saves the event data from/to the JSON file.
- `src/models.py`: Defines the `Event` data model.
- `templates/`: Contains the HTML templates for the web interface.
- `static/`: Contains static files like CSS.
- `requirements.txt`: Lists the Python dependencies for the project.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the web application:**
    ```bash
    python3 src/app.py
    ```

3.  Open your web browser and navigate to `http://127.0.0.1:8080`.

## Web Interface

- **Home Page:** The main page displays a list of all countries with available historical data.
- **Country Events Page:** Clicking on a country will take you to a page displaying all its historical events. You can filter the events by a start and end year.
- **Add Event Page:** You can add new historical events through the "Add Event" page, which is accessible from the navigation bar.
