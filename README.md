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
- `src/data_loader.py`: Loads the event data from the JSON file.
- `src/app.py`: The main application logic.

## How to Run

To run the application, execute the following command from the root directory:

```bash
python3 -m src.app
```

This will run the main function in `src/app.py` and print the historical events for France as an example.
