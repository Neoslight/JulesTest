from typing import List, Dict
from src.models import Event
from src.data_loader import load_events, save_events

class HistoricalApp:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.events_by_country: Dict[str, List[Event]] = load_events(self.data_path)

    def get_events(self, country: str, start_year: int = None, end_year: int = None) -> List[Event]:
        """Returns a list of historical events for a given country, optionally filtered by year."""
        events = self.events_by_country.get(country, [])
        if start_year:
            events = [e for e in events if e.year >= start_year]
        if end_year:
            events = [e for e in events if e.year <= end_year]
        return events

    def add_event(self, country: str, year: int, event_desc: str):
        """Adds a new historical event and saves it."""
        event = Event(year=year, event=event_desc)
        if country not in self.events_by_country:
            self.events_by_country[country] = []
        self.events_by_country[country].append(event)
        self.events_by_country[country].sort(key=lambda e: e.year)
        save_events(self.data_path, self.events_by_country)
        print("Event added successfully.")

def main():
    """Main function to run the interactive historical events app."""
    app = HistoricalApp('data/events.json')

    print("Welcome to the Historical Events App!")
    print("Enter a country name to see its historical events, 'add' to add a new event, or 'quit' to exit.")

    while True:
        command = input("Enter a command (country name, 'add', or 'quit'): ").strip()

        if command.lower() == 'quit':
            break

        elif command.lower() == 'add':
            country = input("Enter the country: ").strip()
            year_str = input("Enter the year: ").strip()
            event_desc = input("Enter the event description: ").strip()

            if year_str.isdigit():
                year = int(year_str)
                app.add_event(country, year, event_desc)
            else:
                print("Invalid year. Please enter a number.")

        else:
            country = command
            start_year_str = input("Enter start year (optional, press Enter to skip): ").strip()
            end_year_str = input("Enter end year (optional, press Enter to skip): ").strip()

            start_year = int(start_year_str) if start_year_str.isdigit() else None
            end_year = int(end_year_str) if end_year_str.isdigit() else None

            events = app.get_events(country, start_year=start_year, end_year=end_year)

            if events:
                print(f"Historical events for {country}:")
                for event in events:
                    print(f"- {event.year}: {event.event}")
            else:
                print(f"No historical events found for {country} in the specified year range.")
        print()

if __name__ == "__main__":
    main()
