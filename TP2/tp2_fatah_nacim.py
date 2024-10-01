"""
Jeu de Cartes à Effets - Deux Joueurs

Ce programme simule un jeu de cartes où deux joueurs tirent des cartes d'un deck
pendant 5 tours. Chaque carte a un effet spécifique qui modifie le score
des joueurs, et le but est d'obtenir le score le plus élevé.

Classes principales :
- Carte (abstraite) et ses héritiers : Normale, Bonus, Malus, Chance.
- Joueur et son héritier Tricheur
"""

######## Auteurs : Fatah MSAID et Nacim TALAOUBRID => ROB4, GRP1
######## Resultat Pylint : 10/10

# Importation des bibs necessaires
from abc import ABC, abstractmethod
import random as rd
from colorama import Fore, Back, init
# Un peu de couleur ne fais pas de mal
init(autoreset=True) # réinisialisation des couleurs a chaque ligne



# Classe Carte abstraite (attetion aux import)
class Carte(ABC):
    """ Classe abstraite représentant une carte de jeu.
    Chaque carte doit intégrer en elle la méthode jouer, qui modifie le score du joueur."""
    # pylint: disable=too-few-public-methods
    # pylint: disable=unnecessary-pass
    @abstractmethod
    def jouer(self, joueur):
        """Applique l'effet de la carte sur le joueur spécifié."""
        pass


class Normale(Carte):
    """Classe représentant une carte Normale.
    elle ajoute un nombre de points aléatoire (entre 1 et 10) au score du joueur."""
    def jouer(self, joueur):
        points = rd.randint(1, 10)
        joueur.score += points
        print(f"Effet : ajoute {points} points")
        print(f"Score actuel de Joueur {joueur.nom} : {joueur.score}\n")

    def __str__(self):
        return "Normale"


class Bonus(Carte):
    """Classe représentant une carte Bonus.
    elle double le score du joueur."""

    def jouer(self, joueur):
        joueur.score *= 2
        print("Effet : double le score du joueur")
        print(f"Score actuel de Joueur {joueur.nom} : {joueur.score}\n")

    def __str__(self):
        return "Bonus"


class Malus(Carte):
    """Classe représentant le une carte Malus, elle fait perdre 5 points score du joueur. """
    def jouer(self, joueur):
        joueur.score -= 5
        print("Effet : Perd 5 points")
        print(f"Score actuel de Joueur {joueur.nom} : {joueur.score}\n")

    def __str__(self):
        return "Malus"


class Chance(Carte):
    """ Classe représentant une carte Chance.
    Lorsque la carte est jouée, elle ajoute ou retire un nombre de 
    points aléatoire (entre -5 et 15) du score du joueur. """
    def jouer(self, joueur):
        points = rd.randint(-5, 15)
        joueur.score += points
        if points >= 0:
            print(f"Effet : Ajoute {points} points")
        else:
            print(f"Effet : Perd {points} points")
        print(f"Score actuel de Joueur {joueur.nom} : {joueur.score}\n")

    def __str__(self):
        return "Chance"


class Joueur:
    # pylint: disable=too-few-public-methods
    """Classe représentant un joueur de jeu de cartes.
    Un joueur a un nom et un score initialisé à 0. """
    def __init__(self, nom):
        self.score = 0
        self.nom = nom

    def jouer_carte(self, carte):
        """Méthode pour jouer une carte et appliquer son effet au score du joueur."""
        print(f"Joueur {self.nom} : tire une carte {carte}")
        carte.jouer(self)


class Tricheur(Joueur):
    # pylint: disable=too-few-public-methods
    """Classe représentant un joueur qui triche.
    Le joueur Tricheur ignore les effets des cartes Malus."""
    def jouer_carte(self, carte):
        # Si la carte est une carte Malus, l'effet est ignoré
        if isinstance(carte, Malus):
            print(f"Joueur {self.nom} : tire une carte {carte}")
            print(Fore.LIGHTMAGENTA_EX + "Je triche sans vergogne donc je ne perds aucun point")
            print(f"Score actuel de Joueur {self.nom} : {self.score}\n")
        else: # Pour toutes les autres cartes, on appelle la méthode de la classe parente
            super().jouer_carte(carte)





# Initialisation des joueurs + mode tricheur
char = input("Joueur 1, voulez-vous tricher oui ou non ? ")
if char == "oui":
    J1 = Tricheur(input("Quel est votre nom joueur 1 ? "))
else:
    J1 = Joueur(input("Quel est votre nom joueur 1 ? "))

char = input("Joueur 2, voulez-vous tricher oui ou non ? ")
if char == "oui":
    J2 = Tricheur(input("Quel est votre nom joueur 2 ? "))
else:
    J2 = Joueur(input("Quel est votre nom joueur 2 ? "))

# Création du deck de cartes
deck = []

# Ajout des cartes Normales, Bonus, Malus et Chance au deck
for i in range(1, 30):
    deck.append(Normale())
for i in range(31, 36):
    deck.append(Bonus())
for i in range(37, 41):
    deck.append(Malus())
for i in range(41, 56):
    deck.append(Chance())

rd.shuffle(deck) ## Sert à mélanger le deck

# Processus du jeu
for i in range(1, 6):
    print(Back.YELLOW + f"\n    Tour {i} :")
    # Joueur 1 tire une carte
    choix_carte = deck.pop()
    J1.jouer_carte(choix_carte)
    # Joueur 2 tire une carte
    choix_carte = deck.pop()
    J2.jouer_carte(choix_carte)




# Affichage du score final
print(Fore.BLUE + "\n++++ Les scores sont ++++")
print(f"Score {J1.nom} : {J1.score} points")
print(f"Score {J2.nom} : {J2.score} points")

# Détermination du gagnant
if J1.score > J2.score:
    print(Fore.GREEN + f"\n{J1.nom}, Félicitations, vous avez gagné!\n")
    print(Fore.RED + f"{J2.nom}, essayez une prochaine fois, peut-être que la roue tournera.\n")
else:
    print(Fore.GREEN + f"\n{J2.nom}, Félicitations, vous avez gagné!\n")
    print(Fore.RED + f"{J1.nom}, essayez une prochaine fois, peut-être que la roue tournera.\n")
