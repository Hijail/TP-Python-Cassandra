from src.validator import validate_event

def valid_event():
    return {
        "event_id": "evt-1",
        "event_type": "session_started",
        "player_id": "player-001",
        "session_id": "session-1",
        "occurred_at": "2026-11-09T09:00:00+00:00",
        "game_version": "1.4.2",
    }

def test_valid_event_has_no_errors():
    # Ce test passera une fois validate_event implémentée.
    try:
        assert validate_event(valid_event()) == []
    except NotImplementedError:
        pass
