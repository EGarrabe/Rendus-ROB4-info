# TP2 Ayoub Hadjab --- Mathys Claudel


import random
from abc import ABC, abstractmethod

# Classe abstraite Carte, représentant une carte de jeu
class Carte(ABC):
    def __init__(self, nom):
        # Chaque carte a un nom
        self.nom = nom

    # Méthode abstraite que chaque sous-classe de Carte doit implémenter
    @abstractmethod
    def appliquer_effet(self, joueur):
        pass

# CarteNormale ajoute un nombre aléatoire de points (1 à 10) au score du joueur
class CarteNormale(Carte):
    def __init__(self):
        super().__init__("Carte Normale")

    # Appliquer l'effet de la carte normale
    def appliquer_effet(self, joueur):
        points = random.randint(1, 10)  # Génère un nombre de points entre 1 et 10
        joueur.modifier_score(points)
        print(f"Effet : Ajoute {points} points.")

# CarteBonus double le score du joueur
class CarteBonus(Carte):
    def __init__(self):
        super().__init__("Carte Bonus")

    # Appliquer l'effet de la carte bonus
    def appliquer_effet(self, joueur):
        joueur.score *= 2  # Multiplie le score actuel par 2
        print(f"Effet : Double le score actuel.")

# CarteMalus fait perdre 5 points au joueur
class CarteMalus(Carte):
    def __init__(self):
        super().__init__("Carte Malus")

    # Appliquer l'effet de la carte malus
    def appliquer_effet(self, joueur):
        joueur.modifier_score(-5)  # Retire 5 points
        print(f"Effet : Perd 5 points.")

# CarteChance ajoute ou retire un nombre aléatoire de points (entre -5 et 10)
class CarteChance(Carte):
    def __init__(self):
        super().__init__("Carte Chance")

    # Appliquer l'effet de la carte chance
    def appliquer_effet(self, joueur):
        points = random.randint(-5, 10)  # Génère un nombre de points entre -5 et 10
        joueur.modifier_score(points)
        if points >= 0:
            print(f"Effet : Ajoute {points} points.")
        else:
            print(f"Effet : Perd {abs(points)} points.")  # Affiche la perte en valeur absolue

# Classe représentant un joueur
class Joueur:
    def __init__(self, nom):
        self.nom = nom  # Le nom du joueur
        self.score = 0  # Initialisation du score à 0

    # Méthode pour modifier le score du joueur
    def modifier_score(self, points):
        self.score += points  # Ajoute les points au score

    # Le joueur joue une carte et l'effet est appliqué
    def jouerCarte(self, carte, tour):
        print(f"Tour {tour} : {self.nom} tire une {carte.nom}.")
        carte.appliquer_effet(self)  # Applique l'effet de la carte
        print(f"Score actuel de {self.nom} : {self.score}\n")

    # Afficher le score final du joueur
    def afficher_score_final(self):
        print(f"Score final de {self.nom} : {self.score}")

# Classe Tricheur, une sous-classe de Joueur, qui peut éviter l'effet des cartes malus
class Tricheur(Joueur):
    def __init__(self, nom):
        super().__init__(nom)

    # Le tricheur peut ignorer les effets de certaines cartes
    def jouerCarte(self, carte, tour):
        print(f"Tour {tour} : {self.nom} tire une {carte.nom}.")
        if isinstance(carte, CarteMalus):  # Si c'est une carte malus, le tricheur évite l'effet
            print(f"{self.nom} a triché et a évité l'effet de la carte {carte.nom} !")
        else:
            carte.appliquer_effet(self)  # Sinon, applique l'effet normalement
        print(f"Score actuel de {self.nom} : {self.score}\n")

# Création du deck de cartes
deck = []
for i in range(30):
    deck.append(CarteNormale())  # Ajoute 30 cartes normales
for i in range(6):
    deck.append(CarteBonus())  # Ajoute 6 cartes bonus
for i in range(5):
    deck.append(CarteMalus())  # Ajoute 5 cartes malus
for i in range(15):
    deck.append(CarteChance())  # Ajoute 15 cartes chance

# Initialisation des joueurs
# Décommentez l'un des deux joueurs pour choisir le type de joueur

#joueur1 = Joueur("Joueur 1")
joueur1 = Tricheur("Joueur 1")  # Joueur tricheur
joueur2 = Joueur("Joueur 2")  # Joueur normal
#joueur2 = Tricheur("Joueur 2")

# Nombre de tours à jouer
nombre_tours = 5

# Début du jeu
for tour in range(1, nombre_tours + 1):
    # Le joueur 1 tire une carte
    carte_tiree = random.choice(deck)
    deck.remove(carte_tiree)  # Retire la carte du deck après avoir été jouée
    joueur1.jouerCarte(carte_tiree, tour)  # Le joueur 1 joue la carte

    # Le joueur 2 tire une carte
    carte_tiree = random.choice(deck)
    deck.remove(carte_tiree)
    joueur2.jouerCarte(carte_tiree, tour)  # Le joueur 2 joue la carte

# Fin du jeu - Affichage des scores finaux
print("--- Résultats ---")
joueur1.afficher_score_final()
joueur2.afficher_score_final()
