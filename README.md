# Historical Events App

This is a simple Python application to discover the main historical events of each country.

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
└── README.md
```

- `data/events.json`: Contains the historical events data in JSON format.
- `src/models.py`: Defines the `Event` data model.
- `src/data_loader.py`: Loads and saves the event data from/to the JSON file.
- `src/app.py`: The main application logic.

## Usage

To run the application, execute the following command from the root directory:

```bash
python3 -m src.app
```

The application will launch in interactive mode. You can enter the following commands:

- **View events for a country:** Enter the name of a country (e.g., `France`).
  - You will be prompted to enter an optional start and end year to filter the events.

- **Add a new event:** Enter `add`.
  - You will be prompted to enter the country, year, and a description for the new event.

- **Quit:** Enter `quit` to exit the application.
