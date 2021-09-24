# Vous trouverez ci dessous plusieurs informations concernant l'api Books:


## 1-Les differents endpoints:

### http://localhost:5000/api/post/book/		Ajoute un livre et si c'est le premier livre crée le fichier data.json pour le stocker (méthode POST, voir section 3 pour le body)
### http://localhost:5000/api/get/book/{id} 	Permet d'obtenir un livre par le biais de son id et de la méthode GET
### http://localhost:5000/api/get/books		    Permet d'obtenir tous les livres par le biais de la méthode GET
### http://localhost:5000/api/update/book/		Met à jour un livre existant dans data.json (méthode PUT, voir section 3 pour le body)
### http://localhost:5000/api/delete/book/{id}	Supprime un livre de la bibliothèque via l'id de celui ci (méthode DELETE) 
### http://localhost:5000/api/delete/books/		Supprime tous les livres (méthode DELETE)

## 2-Auteurs :

### Barnabé CUVILLIERS
### Tom CHAMBOREDON
### Joan SMITH

## 3-Exemple de format JSON attendu pour un livre :

```json
[
    {
        "authors": [
            "Sun Tzu"
        ],
        "genres": [
            "Military",
            "Classical litterature"
        ],
        "id": 1,
        "name": "The Art of War",
        "type": "Military Treatise",
        "year": -500
    }
]
```