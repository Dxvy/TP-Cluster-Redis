# TP-Cluster-Redis

### Partie 1: Installation et Configuration du Cluster Redis avec Docker

1. **Installation de Redis via Docker :**
    - J'ai préférer utiliser Docker pour réaliser ce projet.
    - Télécharger l'image Redis à travers le Docker Hub :
     ```
         docker pull redis
     ```

   2. **Configuration du Cluster Redis :**
       - Créer un réseau pour les conteneurs Redis :
         ```
         docker network create redis-cluster
         ```
       - Démarrer les conteneurs Redis en mode cluster ici avec 6 noeuds : 
      ```
         docker run --name redis1 --net redis-cluster -d redis redis-server --cluster-enabled yes
         docker run --name redis2 --net redis-cluster -d redis redis-server --cluster-enabled yes
         docker run --name redis3 --net redis-cluster -d redis redis-server --cluster-enabled yes
         docker run --name redis4 --net redis-cluster -d redis redis-server --cluster-enabled yes
         docker run --name redis5 --net redis-cluster -d redis redis-server --cluster-enabled yes
         docker run --name redis6 --net redis-cluster -d redis redis-server --cluster-enabled yes
      ```

### Partie 2: Premiers Pas avec le Cluster Redis

1. **Injection de Données** :
   - Insérer des données de différents types dans Redis :
     - Pour insérer une chaîne de caractères (String) :
       ```
       docker exec -it <nom_conteneur> redis-cli SET mykey "Hello"
       ```
     - Pour insérer une liste (List) :
       ```
       docker exec -it <nom_conteneur> redis-cli LPUSH mylist "element1"
       docker exec -it <nom_conteneur> redis-cli LPUSH mylist "element2"
       ```
     - Pour insérer un ensemble (Set) :
       ```
       docker exec -it <nom_conteneur> redis-cli SADD myset "member1"
       docker exec -it <nom_conteneur> redis-cli SADD myset "member2"
       ```
     - Pour insérer un hash :
       ```
       docker exec -it <nom_conteneur> redis-cli HSET myhash field1 "value1"
       docker exec -it <nom_conteneur> redis-cli HSET myhash field2 "value2"
       ```
     - Pour insérer un ensemble trié (Sorted Set) :
       ```
       docker exec -it <nom_conteneur> redis-cli ZADD myzset 1 "one"
       docker exec -it <nom_conteneur> redis-cli ZADD myzset 2 "two"
       ```

2. **Requêtage des Données** :
   - Effectuer des opérations de lecture sur les données stockées, en utilisant divers critères selon le type de données :
     - Pour lire une chaîne de caractères (String) :
       ```
       docker exec -it <nom_conteneur> redis-cli GET mykey
       ```
     - Pour lire une liste (List) :
       ```
       docker exec -it <nom_conteneur> redis-cli LRANGE mylist 0 -1
       ```
     - Pour lire un ensemble (Set) :
       ```
       docker exec -it <nom_conteneur> redis-cli SMEMBERS myset
       ```
     - Pour lire un hash :
       ```
       docker exec -it <nom_conteneur> redis-cli HGETALL myhash
       ```
     - Pour lire un ensemble trié (Sorted Set) :
       ```
       docker exec -it <nom_conteneur> redis-cli ZRANGE myzset 0 -1 WITHSCORES
       ```

Assurez-vous de remplacer `<nom_conteneur>` par le nom du conteneur Redis dans lequel vous souhaitez insérer et consulter les données.

### Partie 3: Intégration de Redis dans un Projet

**Restitution** :

- Projet Réalisé : Application d'annuaire avec Redis comme solution de stockage.
- Utilisation de Redis : Stockage des données et mise en cache pour améliorer les performances.
  - Bénéfices Observés :
  - Amélioration des temps de réponse grâce au cache Redis.
  - Gestion efficace des données avec Redis en tant qu'entrepôt de données.
  - Simplification du développement grâce à l'utilisation de Redis pour le stockage et le cache.
  - Cette intégration de Redis dans le projet a permis d'améliorer les performances, la gestion des données et la facilité de développement, offrant ainsi une solution efficace pour l'application.

### Partie 4: Introspection sur l'Intégration de Redis

**Restitution** :

- Analyse des Avantages de l'Intégration de Redis :
- Performance Améliorée : Utilisation de Redis comme cache pour réduire les temps de réponse.
- Scalabilité Renforcée : Possibilité d'étendre facilement la capacité de stockage et de traitement.
- Gestion des Sessions : Stockage des sessions utilisateurs pour une expérience utilisateur fluide.
- Traitement de Données en Temps Réel : Utilisation de Redis pour des opérations nécessitant des données en temps réel.
- Réduction de la Charge sur la Base de Données Principale : En déchargeant les requêtes fréquentes vers Redis.
- 
- En résumé, l'intégration de Redis dans le projet a permis d'améliorer les performances, la scalabilité, la gestion des sessions et le traitement des données en temps réel, tout en réduisant la charge sur la base de données principale. L'intégration dans différents types de projets offre des perspectives intéressantes pour améliorer les performances et l'évolutivité des systèmes.
