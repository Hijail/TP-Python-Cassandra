CREATE KEYSPACE IF NOT EXISTS game_telemetry
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE game_telemetry;

CREATE TABLE IF NOT EXISTS events_by_player_day (
    player_id text,
    event_day date,
    occurred_at timestamp,
    event_id text,
    session_id text,
    event_type text,
    game_version text,
    payload text,
    PRIMARY KEY ((player_id, event_day), occurred_at, event_id)
) WITH CLUSTERING ORDER BY (occurred_at DESC, event_id ASC);

CREATE TABLE IF NOT EXISTS events_by_session (
    session_id text,
    occurred_at timestamp,
    event_id text,
    player_id text,
    event_type text,
    payload text,
    PRIMARY KEY ((session_id), occurred_at, event_id)
) WITH CLUSTERING ORDER BY (occurred_at ASC, event_id ASC);

CREATE TABLE IF NOT EXISTS errors_by_version_day (
    game_version text,
    event_day date,
    occurred_at timestamp,
    event_id text,
    player_id text,
    payload text,
    PRIMARY KEY ((game_version, event_day), occurred_at, event_id)
) WITH CLUSTERING ORDER BY (occurred_at DESC, event_id ASC);
