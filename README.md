# Data Engineering & Big Data — M2
## Projet fil rouge : télémétrie d'un jeu vidéo connecté

### Prérequis
- Python 3.9+
- Docker Desktop ou Docker Engine + Docker Compose
- Environnement virtuel Python recommandé

### Démarrage de Cassandra
```bash
docker compose up -d
docker compose logs -f cassandra
```
Attendre que Cassandra soit prête. Puis :
```bash
docker exec -i game-cassandra cqlsh < cql/schema.cql
```

### Environnement Python
```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate        # Windows
python -m pip install -r requirements.txt
```

### Parcours conseillé
1. Générer des événements : `python -m src.generator`
2. Valider et transformer les événements.
3. Charger les données dans Cassandra.
4. Produire un rapport qualité et des indicateurs.
5. Lancer les tests : `pytest -q`

### Architecture
Source simulée → JSONL → validation/normalisation → Cassandra → indicateurs.
Ce dépôt est un environnement pédagogique. Le mode mono-nœud n'est pas une architecture de production.
