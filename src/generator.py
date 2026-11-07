
"""Générateur de télémétrie synthétique — à compléter si souhaité."""

from datetime import datetime, timezone
import json
import random
import uuid
from pathlib import Path
from typing import Dict, Any


EVENT_TYPES = [
    "session_started",
    "level_completed",
    "player_death",
    "match_finished",
    "game_error",
]

GAME_VERSIONS = ["1.4.1", "1.4.2", "1.5.0"]


def generate_event(player_id: str) -> Dict[str, Any]:
    """Génère un événement de télémétrie synthétique."""
    return {
        "event_id": str(uuid.uuid4()),
        "event_type": random.choice(EVENT_TYPES),
        "player_id": player_id,
        "session_id": str(uuid.uuid4()),
        "occurred_at": datetime.now(timezone.utc).isoformat(),
        "game_version": random.choice(GAME_VERSIONS),
    }


def write_events(
    path: str = "data/events.jsonl",
    count: int = 1000,
) -> None:
    """Génère des événements et les écrit au format JSON Lines."""
    if count < 0:
        raise ValueError("Le nombre d'événements doit être positif ou nul.")

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        for _ in range(count):
            player_id = "player-{0:03d}".format(random.randint(1, 100))
            event = generate_event(player_id)
            file.write(json.dumps(event, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    write_events()
