from abc import ABC, abstractmethod
import random

""" TP2 ELOTREUCH Ilyes et COUQUE Bastien """

# Classe abstraite Carte
class Carte(ABC):
    @abstractmethod
    def effet(self, joueur):
        """Applique l'effet de la carte sur le joueur."""
        pass

# Carte Normale qui ajoute entre 1 et 10 points
class CarteNormale(Carte):
    def effet(self, joueur):
        """Ajoute entre 1 et 10 points au score du joueur."""
        points = random.randint(1, 10)
        joueur.score += points
        print(f"Effet: ajoute {points} points. Score actuel de {joueur.nom}: {joueur.score}")

# Carte Bonus qui double le score du joueur
class CarteBonus(Carte):
    def effet(self, joueur):
        """Double le score du joueur."""
        joueur.score *= 2
        print(f"Effet: double le score. Score actuel de {joueur.nom}: {joueur.score}")

# Carte Malus qui retire 5 points au joueur
class CarteMalus(Carte):
    def effet(self, joueur):
        """Retire 5 points au score du joueur."""
        joueur.score -= 5
        print(f"Effet: perd 5 points. Score actuel de {joueur.nom}: {joueur.score}")

# Carte Chance qui ajoute entre -5 et 15 points
class CarteChance(Carte):
    def effet(self, joueur):
        """Ajoute un nombre de points aléatoire entre -5 et 15 au score du joueur."""
        points = random.randint(-5, 15)
        joueur.score += points
        print(f"Effet: ajoute {points} points. Score actuel de {joueur.nom}: {joueur.score}")

# Classe Joueur avec un nom et un score
class Joueur:
    def __init__(self, nom):
        """Initialise un joueur avec un nom et un score de 0."""
        self.nom = nom
        self.score = 0

    def jouerCarte(self, carte):
        """Applique l'effet de la carte sur le joueur."""
        carte.effet(self)

# Classe Tricheur qui hérite de Joueur et surcharge la méthode jouerCarte
class Tricheur(Joueur):
    def jouerCarte(self, carte):
        """Le tricheur ne perd pas de points quand il tire une Carte Malus."""
        if isinstance(carte, CarteMalus):
            print(f"{self.nom} tire une Carte Malus mais triche et ne perd pas de points!")
        else:
            carte.effet(self)

# Fonction pour créer un deck de cartes avec 56 cartes (30 Normales, 6 Bonus, 5 Malus, 15 Chances)
def creer_deck():
    """Crée un deck de 56 cartes mélangées."""
    deck = []
    deck += [CarteNormale() for i in range(30)]
    deck += [CarteBonus() for j in range(6)]
    deck += [CarteMalus() for k in range(5)]
    deck += [CarteChance() for l in range(15)]
    random.shuffle(deck)  # Mélange aléatoirement les cartes dans le deck
    return deck

# Fonction principale pour gérer le jeu avec deux joueurs
def jouer_jeu(tours, joueur1, joueur2, deck):
    """Gère le déroulement du jeu tour par tour pour deux joueurs."""
    for tour in range(1, tours + 1):
        print(f"----- Tour {tour} -----")
        
        # Joueur 1 tire une carte et applique son effet
        carte1 = deck.pop()
        print(f"{joueur1.nom} tire une {carte1.__class__.__name__}")
        joueur1.jouerCarte(carte1)

        # Joueur 2 tire une carte et applique son effet
        carte2 = deck.pop()
        print(f"{joueur2.nom} tire une {carte2.__class__.__name__}")
        joueur2.jouerCarte(carte2)
    
    # Affiche les scores finaux des deux joueurs
    print(f"------------------------ Fin ------------------------")
    print(f"-------- Score final de {joueur1.nom}: {joueur1.score}")
    print(f"-------- Score final de {joueur2.nom}: {joueur2.score}")

# Point d'entrée du programme
if __name__ == "__main__":
    # Création de deux joueurs, dont un tricheur
    joueur1 = Joueur("Joueur 1")
    joueur2 = Tricheur("Joueur 2")  # Joueur 2 est un tricheur
    deck = creer_deck()  # Création et mélange du deck
    jouer_jeu(5, joueur1, joueur2, deck)  # Lancement du jeu avec 5 tours
