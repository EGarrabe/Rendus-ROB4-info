# CLARENCE PFISTER & ANTONIN CHAUVET

from abc import ABC, abstractmethod
import random


class Joueur:
    def __init__(self, nom: str, score: int):
        """ Constructeur de la classe Joueur """
        self.nom = nom
        self.score = score

    def jouer_carte(self, carte):
        """ Fonction qui permet au joueur de jouer la carte passé en paramètre """
        carte.effet(self)

    def __str__(self):
        """ Fonction qui permet d'afficher le nom et le score du joueur """
        return f"Score actuel de {self.nom} : {self.score}"


class Tricheur(Joueur):
    def __init__(self, nom: str, score: int):
        """ Constructeur de la classe Tricheur """
        super().__init__(nom, score)
        self.nom = nom

    def jouer_carte(self, carte):
        """ Fonction qui permet au joueur de jouer la carte passé en paramètre 
            et vérifie si la carte est une triche """
        if isinstance(carte, CarteMalus):
            print("Le tricheur a évité une carte malus")
        else:
            return super().jouer_carte(carte)


# Classe abstraite Carte
class Carte(ABC):
    def __init__(self):
        """ Constructeur de la classe Carte """
        self.nom = "carte"

    @abstractmethod
    def effet(self, joueur):
        """ Fonction qui permet d'appliquer l'effet de la carte sur le joueur passé en paramètre """

    def __str__(self):
        """ Fonction qui permet d'afficher le nom de la carte """
        return self.nom


class CarteNormale(Carte):
    def __init__(self):
        """ Constructeur de la classe CarteNormale """
        super().__init__()
        self.nom = "Carte Normale"

    def effet(self, joueur: Joueur):
        """ Fonction qui permet d'ajouter un nombre de points 
            aléatoire entre 1 et 10 au joueur passé en paramètre """
        points = random.randint(1, 10)
        joueur.score += points
        print(f"Effet : Ajoute {points} points")


class CarteBonus(Carte):
    def __init__(self):
        """ Constructeur de la classe CarteBonus """
        super().__init__()
        self.nom = "Carte Bonus"

    def effet(self, joueur: Joueur):
        """ Fonction qui permet de doubler le nombre de points du joueur passé en paramètre """
        joueur.score *= 2
        print("Effet : Double le score")


class CarteMalus(Carte):
    def __init__(self):
        """ Constructeur de la classe CarteMalus """
        super().__init__()
        self.nom = "Carte Malus"

    def effet(self, joueur: Joueur):
        """ Fonction qui permet d'enlever 5 points au joueur passé en paramètre """
        joueur.score -= 5
        print("Effet : Enlève 5 points")


class CarteChance(Carte):
    def __init__(self):
        """ Constructeur de la classe CarteChance"""
        super().__init__()
        self.nom = "Carte Chance"

    def effet(self, joueur: Joueur):
        """ Fonction qui permet d'ajouter 15 ou enlevé 5 points au joueur passé en paramètre """
        points = random.choice([-5, 15])
        joueur.score += points
        if points > 0:
            print(f"Effet : Ajoute {points} points")
        else:
            print(f"Effet : Enlève {points} points")


# Création du deck avec différentes cartes
def creer_deck():
    """ Fonction qui permet de créer un deck de cartes et de le mélanger """
    deck = []
    deck += [CarteNormale() for _ in range(30)] # ajout des cartes normales dans le deck
    deck += [CarteBonus() for _ in range(6)] # ajout des cartes bonus dans le deck
    deck += [CarteMalus() for _ in range(5)] # ajout des cartes malus dans le deck
    deck += [CarteChance() for _ in range(15)] # ajout des cartes chance dans le deck
    random.shuffle(deck)  # on mélange le deck
    return deck


def jeu(nb_tour: int):
    """ Fonction qui permet de jouer le jeu """
    # creation des joueurs
    joueur1 = Joueur("Joueur 1", 0)
    joueur2 = Tricheur("Joueur 2", 0)

    deck = creer_deck() # création du deck
    for i in range(0, nb_tour):
        print(f"Tour {i+1}")

        # joueur1 joue
        carte1 = deck.pop() # tire une carte du deck
        print(f"{joueur1.nom} joue : {carte1}")
        joueur1.jouer_carte(carte1) # le joueur joue la carte
        print(joueur1)

        # joueur2 joue
        carte2 = deck.pop() # tire une carte du deck
        print(f"{joueur2.nom} joue : {carte2}")
        joueur2.jouer_carte(carte2) # le joueur joue la carte
        print(joueur2)
        print()


    # fin du jeu affichage du gagnant
    if joueur1.score > joueur2.score:
        print(f"Le joueur {joueur1.nom} a gagné avec un score de {joueur1.score} points !")
    elif joueur1.score < joueur2.score:
        print(f"Le joueur {joueur2.nom} a gagné avec un score de {joueur2.score} points !")
    else:
        print("Match nul !")


if __name__ == "__main__":
    jeu(5)
