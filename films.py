import csv

def afficher_films():
  with open('films.csv', 'r') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    entetes = next(lecteur_csv)  # Lire la première ligne contenant les entêtes

    for ligne in lecteur_csv:
      titre = ligne[0]
      annee = ligne[1]
      realisateur = ligne[2]
      genre = ligne[3]

      print(f"Titre: {titre}")
      print(f"Année: {annee}")
      print(f"Réalisateur: {realisateur}")
      print(f"Genre: {genre}")
      print("")


def rechercher_film(titre_recherche):
  with open('films.csv', 'r') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    entetes = next(lecteur_csv)  # Lire la première ligne contenant les entêtes
    films_trouves = []

    for ligne in lecteur_csv:
      titre = ligne[0]

      if titre.lower().startswith(titre_recherche.lower()):
        films_trouves.append(ligne)

    return films_trouves


def interface_utilisateur():
  while True:
    print("--- Interface de la base de données de films ---")
    print("1. Afficher tous les films")
    print("2. Rechercher un film")
    print("3. Quitter")
    choix = input("Choisissez une option : ")

    if choix == "1":
      print("--- Liste de tous les films ---")
      afficher_films()
    elif choix == "2":
      titre_recherche = input("Entrez le titre du film à rechercher : ")
      films_trouves = rechercher_film(titre_recherche)

      if films_trouves:
        print(f"--- Résultats de la recherche pour '{titre_recherche}' ---")
        for film in films_trouves:
          titre = film[0]
          annee = film[1]
          realisateur = film[2]
          genre = film[3]

          print(f"Titre: {titre}")
          print(f"Année: {annee}")
          print(f"Réalisateur: {realisateur}")
          print(f"Genre: {genre}")
          print("")
      else:
        print(f"Aucun film trouvé pour '{titre_recherche}'.")
    elif choix == "3":
      print("Au revoir !")
      break
    else:
      print("Option invalide. Veuillez sélectionner une option valide.")
