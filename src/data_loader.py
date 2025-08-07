import json
from typing import Dict, List
from src.models import Event

def load_events(filepath: str) -> Dict[str, List[Event]]:
    """Loads historical events from a JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)

    events_by_country = {}
    for country, events_data in data.items():
        events_by_country[country] = [Event(**event_data) for event_data in events_data]

    return events_by_country
