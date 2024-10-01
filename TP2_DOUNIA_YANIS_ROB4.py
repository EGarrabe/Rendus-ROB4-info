import random
import time
from abc import ABC, abstractmethod
from colorama import init, Fore, Style

# Initialiser Colorama pour les couleurs dans le terminal
init(autoreset=True)

class Carte(ABC):
    """
    Classe abstraite représentant une carte du jeu.
    Chaque carte doit implémenter la méthode effet qui définit l'impact de la carte sur le joueur.
    """

    @abstractmethod
    def effet(self, joueur):
        """
        Applique l'effet de la carte sur le joueur.
        Args:
            joueur (Joueur): Le joueur sur lequel appliquer l'effet de la carte.
        """
        pass

class CartePoint(Carte):
    """
    Carte qui affecte directement les points du joueur.
    Hérite de la classe Carte et applique des gains ou des pertes de points.
    """

    def __init__(self, points):
        """
        Initialise une carte de points avec un certain nombre de points.
        Args:
            points (int): Le nombre de points à ajouter ou à retirer au score du joueur.
        """
        self.points = points

    def effet(self, joueur):
        """
        Applique l'effet de la carte, modifiant les points du joueur.
        Si la valeur des points est positive, le joueur gagne des points.
        Si la valeur est négative, le joueur perd des points.
        Args:
            joueur (Joueur): Le joueur sur lequel appliquer l'effet.
        """
        joueur.score += self.points
        action = "gagne" if self.points >= 0 else "perd"
        print(f"{joueur.nom} {action} {abs(self.points)} points.")

class CarteMultiplicateur(Carte):
    """
    Carte qui multiplie le score du joueur.
    Applique un effet multiplicateur sur le score du joueur.
    """

    def __init__(self, facteur):
        """
        Initialise une carte multiplicatrice avec un certain facteur.
        Args:
            facteur (int): Le facteur par lequel multiplier le score du joueur.
        """
        self.facteur = facteur

    def effet(self, joueur):
        """
        Multiplie le score actuel du joueur par le facteur défini.
        Args:
            joueur (Joueur): Le joueur sur lequel appliquer l'effet multiplicateur.
        """
        joueur.score *= self.facteur
        print(f"{joueur.nom} voit son score multiplié par {self.facteur}.")

class CarteNormale(CartePoint):
    """
    Carte normale qui ajoute un nombre de points aléatoire entre 1 et 10.
    Hérite de CartePoint.
    """

    def __init__(self):
        """Initialise une Carte Normale avec des points aléatoires entre 1 et 10."""
        points = random.randint(1, 10)
        super().__init__(points)

    def effet(self, joueur):
        """Affiche que la Carte Normale est tirée, puis applique l'effet."""
        print(f"{joueur.nom} tire une Carte Normale.")
        super().effet(joueur)

class CarteBonus(CarteMultiplicateur):
    """
    Carte bonus qui double le score du joueur.
    Hérite de CarteMultiplicateur et applique un multiplicateur de 2.
    """

    def __init__(self):
        """Initialise une Carte Bonus avec un facteur de multiplication de 2."""
        super().__init__(2)

    def effet(self, joueur):
        """Affiche que la Carte Bonus est tirée, puis applique l'effet."""
        print(f"{joueur.nom} tire une Carte Bonus.")
        super().effet(joueur)

class CarteMalus(CartePoint):
    """
    Carte qui réduit le score du joueur de 5 points.
    Hérite de CartePoint et retire 5 points au joueur.
    """

    def __init__(self):
        """Initialise une Carte Malus avec une réduction de 5 points."""
        super().__init__(-5)

    def effet(self, joueur):
        """Affiche que la Carte Malus est tirée, puis applique l'effet."""
        print(f"{joueur.nom} tire une Carte Malus.")
        super().effet(joueur)

class CarteChance(CartePoint):
    """
    Carte qui ajoute ou retire un nombre de points aléatoire entre -5 et 15.
    Hérite de CartePoint.
    """

    def __init__(self):
        """Initialise une Carte Chance avec des points aléatoires entre -5 et 15."""
        points = random.randint(-5, 15)
        super().__init__(points)

    def effet(self, joueur):
        """Affiche que la Carte Chance est tirée, puis applique l'effet."""
        print(f"{joueur.nom} tire une Carte Chance.")
        super().effet(joueur)

class Joueur:
    """
    Classe représentant un joueur dans le jeu.
    Un joueur possède un nom et un score qui est modifié au fur et à mesure que les cartes sont jouées.
    """

    def __init__(self, nom):
        """
        Initialise un joueur avec un nom et un score de départ à 0.
        Args:
            nom (str): Le nom du joueur.
        """
        self.nom = nom
        self.score = 0

    def jouerCarte(self, carte: Carte):
        """
        Joue une carte et applique son effet sur le score du joueur.
        Args:
            carte (Carte): La carte tirée par le joueur.
        """
        carte.effet(self)

class Tricheur(Joueur):
    """
    Classe représentant un joueur tricheur.
    Ce joueur ignore les pertes de points associées aux cartes malus.
    Hérite de la classe Joueur.
    """

    def jouerCarte(self, carte: Carte):
        """
        Surcharge de la méthode jouerCarte pour ignorer les pertes de points
        liées aux cartes malus.
        Args:
            carte (Carte): La carte tirée par le joueur.
        """
        if isinstance(carte, CarteMalus):
            print(f"{self.nom} tire une Carte Malus mais ignore la perte de points grâce à sa triche.")
        else:
            carte.effet(self)

def creer_deck():
    """
    Crée un deck de 56 cartes mélangées pour le jeu.
    Le deck est composé de :
    - 30 cartes normales
    - 6 cartes bonus
    - 5 cartes malus
    - 15 cartes chance
    Returns:
        list: Une liste de cartes mélangées.
    """
    deck = []
    deck.extend([CarteNormale() for _ in range(30)])
    deck.extend([CarteBonus() for _ in range(6)])
    deck.extend([CarteMalus() for _ in range(5)])
    deck.extend([CarteChance() for _ in range(15)])
    random.shuffle(deck)
    return deck

def afficher_banderole():
    """
    Affiche la banderole du jeu dans le terminal.
    Utilise des couleurs pour un affichage visuel agréable grâce à Colorama.
    """
    print(Fore.CYAN + Style.BRIGHT + "\n====================================")
    print(Fore.GREEN + "       Jeu de carte by Yanis et Dounia")
    print(Fore.CYAN + Style.BRIGHT + "====================================\n")

def barre_de_chargement():
    """
    Simule une barre de chargement dans le terminal.
    Affiche progressivement une série de caractères pour simuler le chargement du jeu.
    """
    print("Chargement du jeu, veuillez patienter...")
    for i in range(1, 31):
        print(Fore.YELLOW + Style.BRIGHT + "=" * i + ">", end="\r")
        time.sleep(0.1)
    print("\n")

def main():
    """
    Fonction principale qui lance le jeu.
    - Affiche la banderole du jeu.
    - Demande les noms des joueurs.
    - Crée un deck de cartes mélangées.
    - Gère les tours des joueurs, qui tirent chacun leur tour des cartes.
    - Affiche le score final et détermine le gagnant à la fin du jeu.
    """
    # Affichage de la banderole
    afficher_banderole()

    # Barre de chargement
    barre_de_chargement()

    # Demander les noms des joueurs
    nom_joueur1 = input("Entrez le nom du Joueur 1 : ")
    nom_joueur2 = input("Entrez le nom du Joueur 2 : ")

    # Créer les joueurs (On peut remplacer Joueur par Tricheur pour tester le tricheur)
    joueur1 = Joueur(nom_joueur1)
    joueur2 = Tricheur(nom_joueur2)  # Le joueur 2 sera un tricheur

    # Créer le deck
    deck = creer_deck()

    nombre_tours = 5  # Chaque joueur tire une carte à chaque tour, donc un total de 10 tours (5 par joueur)

    for tour in range(1, nombre_tours + 1):
        print(f"\n--- {joueur1.nom} Tour {tour} ---")

        # Tour de joueur 1
        if deck:
            carte = deck.pop()
            joueur1.jouerCarte(carte)
            print(f"{joueur1.nom} Score actuel : {joueur1.score}")
        else:
            print("Le deck est vide.")
            break

        print(f"\n--- {joueur2.nom} Tour {tour} ---")

        # Tour de joueur 2
        if deck:
            carte = deck.pop()
            joueur2.jouerCarte(carte)
            print(f"{joueur2.nom} Score actuel : {joueur2.score}")
        else:
            print("Le deck est vide.")
            break

    # Affichage du score final
    print(f"\nScore final de {joueur1.nom} : {joueur1.score}")
    print(f"Score final de {joueur2.nom} : {joueur2.score}")

    # Déterminer le gagnant
    if joueur1.score > joueur2.score:
        print(f"{joueur1.nom} remporte la partie !")
    elif joueur1.score < joueur2.score:
        print(f"{joueur2.nom} remporte la partie !")
    else:
        print("Match nul !")

if __name__ == "__main__":
    main()
