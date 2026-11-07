# Contrat d'événement

Un événement de télémétrie est un document JSON avec les champs communs suivants :

| Champ | Type | Règle |
|---|---|---|
| event_id | chaîne | identifiant stable de l'événement |
| event_type | chaîne | type autorisé |
| player_id | chaîne | identifiant pseudonyme du joueur |
| session_id | chaîne | identifiant de session |
| occurred_at | date ISO-8601 | idéalement UTC |
| game_version | chaîne | version du client/jeu |

Types autorisés : `session_started`, `level_completed`, `player_death`, `match_finished`, `game_error`.

Pour `level_completed`, `duration_seconds` est obligatoire et strictement positif.
Pour `game_error`, `error_code` est recommandé.

## Règles qualité
- Champ obligatoire absent → rejet.
- Type d'événement inconnu → rejet.
- Horodatage invalide → rejet.
- Durée de niveau absente, non numérique ou négative → rejet.
- Ligne JSON corrompue → rejet avec raison.
- Les événements rejetés doivent être conservés dans un fichier de quarantaine pour inspection.
