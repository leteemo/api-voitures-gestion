import requests


# TEST 1 - INSCRIPTION UTILISATEUR

# URL pour l'inscription des utilisateurs
url_register = "http://localhost:8000/api/users/register/"

# Données d'inscription
data = {
    'username': 'Antoine',
    'email': 'Antoine@example.com',
    'password': 'motdepasse',
    'role': 'user'
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
    'username': 'Antoine',
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


