#Darde Romain et Hauzay Joshua

from abc import ABC
import random

class Carte(ABC):
    ''' Création de la classe abstraite Carte '''
    def __init__(self):
        self.point = 0


class Carte_Normale(Carte):
    ''' Création de la carte normale avec un point entre 1 et 10'''
    def __init__(self):
        super().__init__()
        self.max = 10
        self.min = 1
        self.point = random.randint(self.min, self.max)
        self.nom = "Carte Normale"
        #On définit le nom qui vont être utilisé lors de l'affichage 


class Carte_Bonus(Carte):
    ''' Création de la carte bonus qui double le score du joueur'''
    def __init__(self):
        super().__init__()
        self.nom = "Carte Bonus"

    def multi(self, x):  # Fonction pour multiplier par deux le score
        self.point = x


class Carte_Malus(Carte):
    ''' Création de la carte malus qui fait perdre 5 points au score du joueur'''
    def __init__(self):
        super().__init__()
        self.point = -5
        self.nom = "Carte Malus"


class Carte_Chance(Carte):
    ''' Création de la carte chance qui ajoute entre -5 et 15 points au score du joueur'''
    def __init__(self):
        super().__init__()
        self.max = 15  #On redéfinit le max et le min pour avoir une valeur aléatoire entre -5 et 15
        self.min = -5
        self.nom = "Carte Chance"
        self.point = random.randint(self.min, self.max)


class Joueur():
    ''' Création de la classe joueur avec un nom et un score'''
    def __init__(self, nom: str, score: int):
        self.nom = nom
        self.score = score

    def jouerCarte(self, carte: Carte): # fonction jouer carte
        self.score = self.score + carte.point  #On ajoute au score du joueur le score de la carte
        
class Tricheur(Joueur):
    ''' Création de la classe tricheur'''
    def jouerCarte(self, carte: Carte): # modifie le comportement de jouer carte pour le tricheur
        if isinstance(carte,Carte_Malus):
            print ("Le joueur triche !") # ne rien faire lorsque le tricheur tire une carte malus
        else:
            self.score = self.score + carte.point # comportement classique pour les autres cartes

def remplir_deck(deck: list):
    ''' Fonction pour remplir le paquet de 56 cartes'''
    for i in range(0, 30): # On ajoute succésivement les différentes cartes dans le deck
        deck.append(Carte_Normale())
        i = i + 1
    for i in range(0, 6):
        deck.append(Carte_Bonus())
        i = i + 1
    for i in range(0, 5):
        deck.append(Carte_Malus())
        i = i + 1
    for i in range(0, 15):
        deck.append(Carte_Chance())
        i = i + 1


def Jouer(deck: list, joueur1: Joueur, joueur2: Joueur):
    ''' Déroulement de la partie avec alternance des joueurs '''
    a = 0  # permet l'alternance des joueurs
    for i in range(8):
        if a % 2 == 0: # alterne les joueurs
            joueur = joueur1
        else:
            joueur = joueur2

        carte = random.choice(deck) # tirage aléatoire d'une carte dans le paquet
        print("Tour ", i + 1, " : ", joueur.nom, " tire une carte", carte.nom)

        if isinstance(carte, Carte_Bonus):  #On regarde si la carte est une carte bonus pour multiplier le score par 2
            carte.multi(joueur.score)
            joueur.jouerCarte(carte)
            print("Effet : Le score est doublé !")
            a += 1
        else:  # Les autres sont simplement une somme
            print("Effet :  ajoute ", carte.point, " points.")
            joueur.jouerCarte(carte)
            a += 1

        print("Score actuel de ", joueur.nom, " : ", joueur.score, "\n")
        deck.remove(carte)
    print("Score final de ", joueur1.nom, " : ", joueur1.score)
    print("Score final de ", joueur2.nom, " : ", joueur2.score, "\n")
    if joueur1.score > joueur2.score :
        print("Le gagnant est : ", joueur1.nom, " ! ")
    else :
        print("Le gagnant est : ", joueur2.nom, " ! ")


def main():
    ''' Main pour définir les joueurs et lancer la partie '''
    print("Bienvenue dans le jeu de cartes")
    Deck = [] # création d'un paquet de carte vide
    Pierre = Joueur("Pierre", 0) # création du joueur 1 avec un score de base nul
    Paul = Tricheur("Paul", 0) # création du joueur 2 (ici tricheur) avec un score de base nul 

    remplir_deck(Deck) # remplissage du paquet de carte
    Jouer(Deck, Pierre, Paul) # lancer la partie

main()
