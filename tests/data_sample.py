import requests


# TEST 1 - INSCRIPTION UTILISATEUR

# URL pour l'inscription des utilisateurs
url_register = "http://localhost:8000/api/users/register/"

# Données d'inscription
data = {
    'username': 'admin',
    'email': 'admin@example.com',
    'password': 'motdepasse',
    'role': 'admin'
}

# Faire la requête POST pour créer l'utilisateur
response = requests.post(url_register, data=data)

# Vérification si la requête a réussi
if response.status_code == 201:
    print("Utilisateur créé avec succès.")
else:
    print("L'utilisateur n'a pas été créé : ", response.json())


# TEST 2 - RECUPERATION TOKEN

# URL de l'endpoint pour obtenir le token
url_token = "http://localhost:8000/api/token/"

# Données de connexion
data = {
    'username': 'admin',
    'password': 'motdepasse' 
}

# Faire la requête POST pour obtenir le token
response = requests.post(url_token, data=data)

# Vérification si la requête a réussi
if response.status_code == 200:
    tokens = response.json()
    access_token = tokens.get('access')
    print("Token d'accès obtenu (à utiliser pour fichier tests_api.py): ", access_token)
else:
    print("Erreur lors de l'obtention du token : ", response.json())

print()

# URL de création des marques et des voitures
url_create_brand = "http://localhost:8000/api/brands/create/"
url_create_car = "http://localhost:8000/api/cars/create/"

# En-têtes avec le token d'accès
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Liste de marques à ajouter
brands_data = [
    {'name': 'Toyota', 'country': 'Japan'},
    {'name': 'Ford', 'country': 'USA'},
    {'name': 'BMW', 'country': 'Germany'},
    {'name': 'Hyundai', 'country': 'South Korea'},
    {'name': 'Audi', 'country': 'Germany'}
]

# Liste de voitures à ajouter
cars_data = [
    {'name': 'Toyota Corolla', 'year': 2021, 'price': 20000.00, 'brand_name': 'Toyota'},
    {'name': 'Ford Mustang', 'year': 2020, 'price': 35000.00, 'brand_name': 'Ford'},
    {'name': 'BMW X5', 'year': 2022, 'price': 60000.00, 'brand_name': 'BMW'},
    {'name': 'Hyundai Elantra', 'year': 2021, 'price': 18000.00, 'brand_name': 'Hyundai'},
    {'name': 'Audi A4', 'year': 2022, 'price': 45000.00, 'brand_name': 'Audi'}
]

# Step 1 - Créer les marques
brand_ids = {}

for brand in brands_data:
    # Faire la requête POST pour créer chaque marque
    response = requests.post(url_create_brand, json=brand, headers=headers)

    if response.status_code == 201:
        print(f"Marque {brand['name']} créée avec succès.")
        brand_ids[brand['name']] = response.json()["id"]
    else:
        print(f"Erreur lors de la création de la marque {brand['name']}: ", response.json())

print()

# Step 2 - Créer les voitures associées aux marques créées
for car in cars_data:
    # Obtenir l'ID de la marque
    brand_id = brand_ids.get(car['brand_name'])

    if brand_id:
        # Construire les données de la voiture avec l'ID de la marque
        car_data = {
            "name": car['name'],
            "brand": brand_id,
            "year": car['year'],
            "price": car['price']
        }

        # Faire la requête POST pour créer la voiture
        response = requests.post(url_create_car, json=car_data, headers=headers)

        if response.status_code == 201:
            print(f"Voiture {car['name']} créée avec succès.")
        else:
            print(f"Erreur lors de la création de la voiture {car['name']}: ", response.json())
    else:
        print(f"Erreur: Marque {car['brand_name']} non trouvée.")
