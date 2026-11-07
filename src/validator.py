"""Validation des événements — exercice étudiant."""
REQUIRED_FIELDS = {"event_id", "event_type", "player_id", "session_id", "occurred_at", "game_version"}
ALLOWED_TYPES = {"session_started", "level_completed", "player_death", "match_finished", "game_error"}

def validate_event(event: dict) -> list[str]:
    # TODO: implémenter les contrôles de champs, type, date et durée.
    raise NotImplementedError
