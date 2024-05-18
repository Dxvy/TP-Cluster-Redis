import requests
import redis
import time

# Connexion à Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# URL de la page web à mesurer
url = "https://www.example.com"

# Fonction pour mesurer la taille de la page web
def measure_page_size(url):
    response = requests.get(url)
    page_size = len(response.text)
    return page_size

# Fonction pour stocker la taille de la page web dans Redis avec une durée de vie
def store_page_size_in_cache(url, page_size, expiration_time):
    r.setex(url, expiration_time, page_size)

# Durée de vie du cache en secondes (par exemple 1 heure = 3600 secondes)
expiration_time = 3600

# Vérifier si la taille de la page web est déjà en cache
cached_page_size = r.get(url)

if cached_page_size:
    print("Taille de la page web (en cache) : ", cached_page_size)
else:
    # Mesurer la taille de la page web et la stocker dans Redis
    page_size = measure_page_size(url)
    store_page_size_in_cache(url, page_size, expiration_time)
    print("Taille de la page web (nouvelle mesure) : ", page_size)
