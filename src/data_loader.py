import json
from typing import Dict, List
from src.models import Event

import dataclasses

def load_events(filepath: str) -> Dict[str, List[Event]]:
    """Loads historical events from a JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)

    events_by_country = {}
    for country, events_data in data.items():
        events_by_country[country] = [Event(**event_data) for event_data in events_data]

    return events_by_country

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

def save_events(filepath: str, events_by_country: Dict[str, List[Event]]):
    """Saves historical events to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(events_by_country, f, cls=EnhancedJSONEncoder, indent=2)
