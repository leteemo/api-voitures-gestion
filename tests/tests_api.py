import requests

# Tests d'ajouts, de get, d'update puis de supressions des données des voitures et des marques


id_brand = None
id_car = None
access_token = input("Acces token (test_admin.py ou test_user.py): ")

print()


# TEST 1 - CREATE BRAND

# URL de l'endpoint pour créer une marque
url_create_brand = "http://localhost:8000/api/brands/create/"



# Données de la marque à créer
data = {
    'name': 'Toyota',
    'country': 'Japan'
}

# En-têtes avec le token d'accès
headers = {
    'Authorization': f'Bearer {access_token}'  # Inclure le token dans l'en-tête
}

# Faire la requête POST pour créer la marque
response = requests.post(url_create_brand, json=data, headers=headers)

# Vérification si la requête a réussi
if response.status_code == 201:
    print("Marque créée avec succès : ", response.json())
    id_brand = response.json()["id"]

else:
    print("Erreur lors de la création de la marque : ", response.json())


print()

# TEST 2 - CREATE CAR

url_create_car = "http://localhost:8000/api/cars/create/"


if id_brand != None:
    # Données de la voiture à créer
    car_data = {
        "name": "Toyota Corolla",
        "brand": id_brand,
        "year": 2021,
        "price": 20000.00
    }

    # En-têtes avec le token d'accès
    headers = {
        'Authorization': f'Bearer {access_token}',  # Inclure le token dans l'en-tête
        'Content-Type': 'application/json'  # Type de contenu JSON
    }

    # Faire la requête POST pour créer la voiture
    response = requests.post(url_create_car, json=car_data, headers=headers)

    # Vérification si la requête a réussi
    if response.status_code == 201:
        print("Voiture créée : ", response.json())
        id_car = response.json()["id"]
    else:
        print("Erreur : ", response.json())


print()


# TEST 3 - GET TOUTES LES VOITURES

# URL de l'endpoint pour récupérer toutes les voitures
url_cars = "http://localhost:8000/api/cars/"

# En-têtes avec le token d'accès
headers = {
    'Authorization': f'Bearer {access_token}',  # Inclure le token dans l'en-tête
    'Content-Type': 'application/json'  # Type de contenu JSON
}

# Faire la requête GET pour récupérer toutes les voitures
response = requests.get(url_cars, headers=headers)

# Vérification si la requête a réussi
if response.status_code == 200:
    print("Voitures récupérées : ", response.json())
else:
    print("Erreur : ", response.json())




print()


# TEST 4 - GET TOUTES LES MARQUES

# URL de l'endpoint pour récupérer toutes les marques
url_brands = "http://localhost:8000/api/brands/"

# En-têtes avec le token d'accès
headers = {
    'Authorization': f'Bearer {access_token}',  # Inclure le token dans l'en-tête
    'Content-Type': 'application/json'  # Type de contenu JSON
}

# Faire la requête GET pour récupérer toutes les marques
response = requests.get(url_brands, headers=headers)

# Vérification si la requête a réussi
if response.status_code == 200:
    print("Marques récupérées : ", response.json())
else:
    print("Erreur : ", response.json())


print()


# TEST 5 - GET LES VOITURES AVEC PAGINATION

# URL de l'endpoint pour récupérer toutes les voitures
url_cars = "http://localhost:8000/api/cars/?page=1&limit=3"

# En-têtes avec le token d'accès
headers = {
    'Authorization': f'Bearer {access_token}',  # Inclure le token dans l'en-tête
    'Content-Type': 'application/json'  # Type de contenu JSON
}

# Faire la requête GET pour récupérer toutes les voitures
response = requests.get(url_cars, headers=headers)

# Vérification si la requête a réussi
if response.status_code == 200:
    print("Voitures récupérées avec pagination: ", response.json())
else:
    print("Erreur : ", response.json())


print()

# TEST 6 - GET LES MARQUES AVEC PAGINATION

# URL de l'endpoint pour récupérer toutes les marques
url_brands = "http://localhost:8000/api/brands/?page=1&limit=3"

# En-têtes avec le token d'accès
headers = {
    'Authorization': f'Bearer {access_token}',  # Inclure le token dans l'en-tête
    'Content-Type': 'application/json'  # Type de contenu JSON
}


# Faire la requête GET pour récupérer toutes les marques
response = requests.get(url_brands, headers=headers)

# Vérification si la requête a réussi
if response.status_code == 200:
    print("Marques récupérées avec pagination: ", response.json())
else:
    print("Erreur : ", response.json())


print()


# TEST 7 - UPDATE VOITURE PRIX

if id_brand != None:
    url_update_car = f"http://localhost:8000/api/cars/update/{id_car}/"

    # Données mises à jour pour la voiture
    car_data = {
        "name": "Toyota Corolla Updated",
        "brand": id_brand,
        "year": 2022,
        "price": 21000.00
    }

    # En-têtes avec le token d'accès
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Faire la requête PUT pour modifier la voiture
    response = requests.put(url_update_car, json=car_data, headers=headers)

    if response.status_code == 200:
        print("Voiture mise à jour avec succès : ", response.json())
    else:
        print("Erreur lors de la mise à jour de la voiture :", response.json())



print()


# TEST 8 - UPDATE MARQUE UPDATED

if id_brand != None:
    url_update_brand = f"http://localhost:8000/api/brands/update/{id_brand}/"

    # Données mises à jour pour la marque
    brand_data = {
        "name": "Toyota Updated",
        "country": "Japan Updated"
    }

    # En-têtes avec le token d'accès
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Faire la requête PUT pour modifier la marque
    response = requests.put(url_update_brand, json=brand_data, headers=headers)

    if response.status_code == 200:
        print("Marque mise à jour avec succès : ", response.json())
    else:
        print("Erreur lors de la mise à jour de la marque :", response.json())



print()


# TEST 9 - SUPRESSION VOITURE

if id_car != None:
    # URL pour la suppression de la voiture
    url_delete_car = f"http://localhost:8000/api/cars/delete/{id_car}/"

    # En-têtes avec le token JWT pour l'authentification
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.delete(url_delete_car, headers=headers)

    # Vérification de la réponse
    if response.status_code == 204:  # 204 No Content signifie que la suppression a réussi
        print("Voiture supprimée avec succès.")
    else:
        print("Erreur lors de la suppression de la voiture :", response.json())



print()


# TEST 10 - SUPRESSION MARQUE

if id_brand != None:
    # URL pour la suppression de la marque
    url_delete_brand = f"http://localhost:8000/api/brands/delete/{id_brand}/"

    # En-têtes avec le token JWT pour l'authentification
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.delete(url_delete_brand, headers=headers)

    # Vérification de la réponse
    if response.status_code == 204:  # 204 No Content signifie que la suppression a réussi
        print("Marque supprimée avec succès.")
    else:
        print("Erreur lors de la suppression de la marque :", response.json())




