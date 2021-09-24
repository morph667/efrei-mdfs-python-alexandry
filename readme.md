Vous trouverez ci dessous plusieurs informations concernant l'api Books:


1-Les different endpoint:

http://localhost:5000/api/post/book/		Ajoute un livre et si c'est le premier livre crée le fichier data.json pour le stocker (methode POST)
http://localhost:5000/api/get/book/{id} 	permet d'obtenir un livre par le biais de son id et de la methode POST
http://localhost:5000/api/get/books		permet d'obtenir tous les livres par le biais de la methode POST
http://localhost:5000/api/update/book/		met à jour un livre exitant dans data.jon (methode PUT)
http://localhost:5000/api/delete/book/{id}	suprimme un livre de la bibliotheque via l'id de celui ci (methode DELETE) 
http://localhost:5000/api/delete/books/		suprimme tous les livres (methode DELETE)