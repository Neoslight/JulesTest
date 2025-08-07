from typing import List, Dict
from src.models import Event
from src.data_loader import load_events

class HistoricalApp:
    def __init__(self, data_path: str):
        self.events_by_country: Dict[str, List[Event]] = load_events(data_path)

    def get_events_by_country(self, country: str) -> List[Event]:
        """Returns a list of historical events for a given country."""
        return self.events_by_country.get(country, [])

def main():
    """Main function to demonstrate the app's functionality."""
    app = HistoricalApp('data/events.json')

    country = "France"
    events = app.get_events_by_country(country)

    if events:
        print(f"Historical events for {country}:")
        for event in events:
            print(f"- {event.year}: {event.event}")
    else:
        print(f"No historical events found for {country}.")

if __name__ == "__main__":
    main()
