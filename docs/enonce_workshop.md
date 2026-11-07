# Workshop final — chaîne de données de télémétrie

## Contexte
Un studio de jeu souhaite suivre l'activité des joueurs, la progression dans les niveaux et les erreurs techniques. Vous recevez un flux simulé d'événements JSONL, potentiellement incomplets ou dupliqués.

## Travail demandé
1. Générer ou charger un fichier d'événements.
2. Valider le contrat d'événement.
3. Séparer les événements acceptés des événements rejetés.
4. Modéliser Cassandra à partir de trois requêtes métier.
5. Ingestérer les événements dans Cassandra.
6. Produire au moins trois indicateurs :
   - nombre d'événements acceptés/rejetés ;
   - nombre de niveaux terminés ;
   - nombre d'erreurs par version ou par jour.
7. Documenter les hypothèses et limites.

## Livrables
- Code exécutable et README.
- Schéma CQL.
- Résumé qualité au format JSON ou texte.
- Démonstration de deux requêtes Cassandra.
- Présentation de 5 minutes : architecture, choix, limites.

