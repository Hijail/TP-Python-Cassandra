"""Générateur de télémétrie synthétique — TP Data Engineering.

Objectif :
- générer des événements de jeu ;
- produire un fichier JSONL ;
- pouvoir injecter des données invalides pour tester le futur validateur.

Les étudiants doivent compléter les parties marquées TODO.
Compatible Python 3.9.
"""

from datetime import datetime, timezone
import json
import random
import uuid
from pathlib import Path
from typing import Optional


EVENT_TYPES = [
    "session_started",
    "level_completed",
    "player_death",
    "match_finished",
    "game_error",
]

VERSIONS = ["1.4.1", "1.4.2", "1.5.0"]


def generate_event(player_id: Optional[str] = None) -> dict:
    """Génère un événement de télémétrie synthétique."""
    event_type = random.choice(EVENT_TYPES)

    event = {
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "player_id": player_id or "player-{0:03d}".format(random.randint(1, 100)),
        "session_id": "session-{0}".format(uuid.uuid4().hex[:12]),
        "occurred_at": datetime.now(timezone.utc).isoformat(),
        "game_version": random.choice(VERSIONS),
    }

    # TODO 1 :
    # Ajouter les champs spécifiques selon event_type.
    #
    # level_completed :
    #   - level_id : "level-XX" (entre 1 et 20)
    #   - duration_seconds : entier entre 30 et 900
    #
    # player_death :
    #   - level_id : "level-XX" (entre 1 et 20)
    #   - cause : enemy, fall, trap ou unknown
    #
    # game_error :
    #   - error_code : NET_TIMEOUT, ASSET_MISSING ou AUTH_FAILED
    #
    # Les autres types d'événements peuvent conserver uniquement
    # les champs communs.

    return event


def write_events(
    path: str = "data/events.jsonl",
    count: int = 1000,
    corrupt: bool = False,
) -> None:
    """Écrit des événements au format JSONL.

    Si corrupt=True, le fichier doit contenir quelques événements invalides
    et une ligne JSON malformée afin de tester le validateur.
    """
    if count < 0:
        raise ValueError("Le nombre d'événements ne peut pas être négatif.")

    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)

    events = [generate_event() for _ in range(count)]

    if corrupt and events:
        # TODO 2 :
        # Injecter des anomalies dans les événements générés :
        # - événement 1 : supprimer le champ obligatoire player_id ;
        # - événement 2 : remplacer occurred_at par "date-invalide" ;
        # - événement 3 : remplacer event_type par "unknown_type" ;
        # - événement 4 : forcer event_type à "level_completed" et
        #   mettre duration_seconds à -10.
        #
        # Attention : vérifier qu'il y a suffisamment d'événements
        # avant de modifier les index 1, 2 et 3.

        pass

    with target.open("w", encoding="utf-8") as file:
        for event in events:
            file.write(json.dumps(event, ensure_ascii=False) + "\\n")

        if corrupt:
            # TODO 3 :
            # Ajouter une dernière ligne volontairement invalide en JSON.
            # Exemple de ligne malformée : {"broken_json":

            pass


if __name__ == "__main__":
    write_events()
    print("Fichier généré : data/events.jsonl")
