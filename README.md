# Documentation API pour la gestion des voitures et marques

Cette API permet de gérer les voitures et les marques. Elle fournit des fonctionnalités telles que l'authentification, la pagination, la création, la mise à jour et la suppression.

---

### Installation
- Prérequis: python 3.7 à python 3.13

Installation des libraries python (dans la racine du projet):

```pip install -r "requierements.txt"```

```python manage.py makemigrations users``` \
```python manage.py makemigrations brands``` \
```python manage.py makemigrations cars``` \
```python manage.py migrate```

Lancer django: \
```python manage.py runserver```

Docuementation swager généré automatiquement: http://127.0.0.1:8000/swagger/

---


### Tests

Dans un nouveau terminal, en ayant toujours le serveur qui est run:

Ajouts des données d'exemple: \
```python tests/data_sample.py```

Test avec admin: \
```python tests/test_admin.py``` \
```python tests/tests_api.py```

Test avec user (n'a pas les permissions pour la création de marque): \
```python tests/test_user.py```

---

### Authentification
- L'API utilise des tokens JWT pour authentifier les utilisateurs. Les tokens doivent être inclus dans les en-têtes HTTP :
  ```http
  Authorization: Bearer <access_token>
  ```

---

### Pagination
- La pagination est activée par défaut avec les paramètres `page` et `limit`.
- Exemple : 
  ```
  http://localhost:8000/api/brands/?page=1&limit=3
  ```

---

## *Endpoints de l'API

### 1. Gestion des utilisateurs

#### 1.1 Inscription d'un utilisateur
- URL : `/api/users/register/`
- Méthode : `POST`
- Description : Permet de créer un nouvel utilisateur (avec le rôle `user` ou `admin`).
- Paramètres (dans le corps de la requête) :
  - `username` (string) : Nom d'utilisateur.
  - `email` (string) : Adresse email de l'utilisateur.
  - `password` (string) : Mot de passe.
  - `role` (string) : Rôle de l'utilisateur (`user` ou `admin`).

- Requête :
  ```json
  {
      "username": "Jean",
      "email": "jean@example.com",
      "password": "motdepasse123",
      "role": "user"
  }
  ```
- Réponse :
  ```json
  {
      "message": "Utilisateur créé avec succès.",
      "id": 1,
      "username": "Jean",
      "email": "jean@example.com",
      "role": "user"
  }
  ```

---

#### 1.2 Obtenir un token JWT
- URL : `/api/token/`
- Méthode : `POST`
- Description : Permet à un utilisateur existant de se connecter et d'obtenir un token JWT pour l'authentification.
- Paramètres (dans le corps de la requête) :
  - `username` (string) : Nom d'utilisateur.
  - `password` (string) : Mot de passe.

- Requête :
  ```json
  {
      "username": "Jean",
      "password": "motdepasse123"
  }
  ```
- Réponse :
  ```json
  {
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

---

### 2. Gestion des marques

#### 2.1 Créer une marque
- URL : `/api/brands/create/`
- Méthode : `POST`
- Description : Permet de créer une nouvelle marque. 
  - Accessible uniquement aux utilisateurs avec le rôle `admin`.
- Paramètres (dans le corps de la requête) :
  - `name` (string) : Nom de la marque.
  - `country` (string) : Pays d'origine de la marque.

- Requête :
  ```json
  {
      "name": "Toyota",
      "country": "Japan"
  }
  ```
- Réponse :
  ```json
  {
      "id": 1,
      "name": "Toyota",
      "country": "Japan"
  }
  ```

---

#### 2.2 Lister les marques
- URL : `/api/brands/`
- Méthode : `GET`
- Description : Retourne une liste paginée de toutes les marques.
- Paramètres (query) :
  - `page` (int, facultatif) : Numéro de la page (par défaut : 1).
  - `limit` (int, facultatif) : Nombre de résultats par page (par défaut : 10).

- Réponse :
  ```json
  {
      "count": 1,
      "next": null,
      "previous": null,
      "results": [
          {
              "id": 1,
              "name": "Toyota",
              "country": "Japan"
          }
      ]
  }
  ```

---

#### 2.3 Mettre à jour une marque
- URL : `/api/brands/update/<int:brand_id>/`
- Méthode : `PUT`
- Description : Met à jour les informations d'une marque spécifique.
- Paramètres :
  - `name` (string) : Nom de la marque.
  - `country` (string) : Pays d'origine.

- Requête :
  ```json
  {
      "name": "Toyota Updated",
      "country": "Japan Updated"
  }
  ```
- Réponse :
  ```json
  {
      "id": 1,
      "name": "Toyota Updated",
      "country": "Japan Updated"
  }
  ```

---

#### 2.4 Supprimer une marque
- URL : `/api/brands/delete/<int:brand_id>/`
- Méthode : `DELETE`
- Description : Supprime une marque spécifique.
- Réponse (code HTTP 204) :
  ```
  Marque supprimée avec succès.
  ```

---

### 3. Gestion des voitures

#### 3.1 Créer une voiture
- URL : `/api/cars/create/`
- Méthode : `POST`
- Description : Permet de créer une nouvelle voiture. 
  - Accessible uniquement aux utilisateurs avec le rôle `admin`.
- Paramètres (dans le corps de la requête) :
  - `name` (string) : Nom de la voiture.
  - `brand` (int) : ID de la marque associée.
  - `year` (int) : Année de fabrication.
  - `price` (decimal) : Prix de la voiture.

- Requête :
  ```json
  {
      "name": "Toyota Corolla",
      "brand": 1,
      "year": 2021,
      "price": 20000.00
  }
  ```
- Réponse :
  ```json
  {
      "id": 1,
      "name": "Toyota Corolla",
      "brand": 1,
      "year": 2021,
      "price": "20000.00"
  }
  ```

---

#### 3.2 Lister les voitures
- URL : `/api/cars/`
- Méthode : `GET`
- Description : Retourne une liste paginée de toutes les voitures.
- Paramètres (query) :
  - `page` (int, facultatif) : Numéro de la page (par défaut : 1).
  - `limit` (int, facultatif) : Nombre de résultats par page (par défaut : 10).

- Réponse :
  ```json
  {
      "count": 1,
      "next": null,
      "previous": null,
      "results": [
          {
              "id": 1,
              "name": "Toyota Corolla",
              "brand": 1,
              "year": 2021,
              "price": "20000.00"
          }
      ]
  }
  ```

---

#### 3.3 Mettre à jour une voiture
- URL : `/api/cars/update/<int:car_id>/`
- Méthode : `PUT`
- Description : Met à jour les informations d'une voiture spécifique.
- Paramètres :
  - `name` (string) : Nom de la voiture.
  - `brand` (int) : ID de la marque associée.
  - `year` (int) : Année de fabrication.
  - `price` (decimal) : Prix.

- Requête :
  ```json
  {
      "name": "Toyota Corolla Updated",
      "brand": 1,
      "year": 2022,
      "price": 21000.00
  }
  ```
- Réponse :
  ```json
  {
      "id": 1,
      "name": "Toyota Corolla Updated",
      "brand": 1,
      "year": 2022,
      "price": "21000.00"
  }
  ```

---

#### 3.4 Supprimer une voiture
- URL : `/api/cars/delete/<int:car_id>/`
- Méthode : `DELETE`
- Description : Supprime une voiture spécifique.
- Réponse (code HTTP 204) :
  ```
  Voiture supprimée avec succès.
  ```


