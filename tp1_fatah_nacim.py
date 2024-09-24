"""
Ce module contient des classes et des fonctions pour manipuler des points,
des vecteurs et des triangles dans un plan 2D. Il utilise matplotlib pour
afficher graphiquement ces objets geometriques.

Classes :
    - Point : Represente un point dans un plan 2D.
    - Vecteur : Represente un vecteur 2D avec des operations vectorielles de base.
    - Triangle : Represente un triangle forme de trois vecteurs.

"""
######## Auteurs : Fatah MSAID et Nacim TALAOUBRID => ROB4, GRP1
######## Resultat Pylint : 10/10

import cmath as mt
import matplotlib.pyplot as plt

# Importation des bibs necessaires, exemple "plt. avant utilisation


class Point: # On a enlever le (object) sous demande de pylint
    """ Classe representant un point dans un espace 2D avec une couleur."""

    # pylint: disable=too-few-public-methods
    # cette ligne au dessus enleve l'avertissement pylint



    def __init__(self, x, y, couleur_p):
        """ Initialisation d'un point avec ses coordonnees x(float) et 
        y(float) et sa couleur (str)"""
        self.x = x
        self.y = y
        self.couleur_p = couleur_p



class Vecteur: # On a enlever le (object) sous demande de pylint
    """Classe representant un vecteur dans un espace 2D avec une couleur associee."""

    def __init__(self, x, y, couleur_v):
        """Initialisation d'un vecteur avec ses composantes x, y et sa couleur."""
        self.x = x
        self.y = y
        self.couleur_v = couleur_v


### Attention : Les 5 fonctions suivantes permettent de surcharger
# les operateurs, mais ne pas les confondre avec la surcharge du cours avec @Dispatch

    def __str__(self): ### Attention : la syntaxe __str__ doit etre respectee
        """Permet d'afficher les attributs du vecteur sur le Terminal."""
        return f"x={self.x} y={self.y} couleur={self.couleur_v}"

    def __add__(self, vect_2): ### Attention : la syntaxe __add__ doit etre respectee
        """ Additionne deux vecteurs suivant leurs x et y respectifs 
        et renvoie un nouveau vecteur."""
        return Vecteur((self.x + vect_2.x), (self.y + vect_2.y), self.couleur_v)
        #Couleur chosie arbitrairement

    def __sub__(self, vect_2): ### Attention : la syntaxe __add__ doit etre respectee
        """  Soustrait deux vecteurs suivant leurs x et y 
        respectifs et renvoie un nouveau vecteur."""
        return Vecteur((self.x - vect_2.x), (self.y - vect_2.y), self.couleur_v)

    def __mul__(self, vect_2):
        """Multiplie deux vecteurs suivant leurs x et y respectifs et renvoie un nouveau vecteur"""
        return Vecteur((self.x * vect_2.x), (self.y * vect_2.y), self.couleur_v)

    def __truediv__(self, vect_2):
        """Divise deux vecteurs suivant leurs x et y respectifs et renvoie un nouveau vecteur"""
        return Vecteur((self.x / vect_2.x), (self.y / vect_2.y), self.couleur_v)



    def plot_(self): # Ne pas oublier d'importer matplotlib
        """Affiche le vecteur sur un graphique en utilisant Matplotlib."""
        plt.plot(self.x, self.y, color=self.couleur_v, marker='o', markersize=5)
        #marker signifie la forme du point



class Triangle: # On a enlever le (object) sous demande de pylint
    """  Classe representant un triangle dans un espace 2D avec une couleur associe.
    Attributs :
    - i, j, k : vecteurs qui sont les sommets du triangle
    - couleur_tri : couleur du triangle 
    """

    def __init__(self, i, j, k, couleur_tri):
        """ Initialisation d'un triangle avec ses sommets i,j,k et sa couleur. """
        self.i = i
        self.j = j
        self.k = k
        self.couleur_tri = couleur_tri

    def turn(self, alpha):
        """Fait tourner le triangle autour de l'origine du repere d'un angle alpha (en radians). """
        # Rotation du sommet i
        self.i.x = self.i.x * mt.cos(alpha) - self.i.y * mt.sin(alpha)
        self.i.y = self.i.x * mt.sin(alpha) + self.i.y * mt.cos(alpha)
        # Rotation du sommet j
        self.j.x = self.j.x * mt.cos(alpha) - self.j.y * mt.sin(alpha)
        self.j.y = self.j.x * mt.sin(alpha) + self.j.y * mt.cos(alpha)
        # Rotation du sommet k
        self.k.x = self.k.x * mt.cos(alpha) - self.k.y * mt.sin(alpha)
        self.k.y = self.k.x * mt.sin(alpha) + self.k.y * mt.cos(alpha)

    def __str__(self): #Faire attention à la syntaxe __str__
        """ Permet d'afficher les attributs (coordonées des sommets i,j,k et la couleur) 
        du vecteur sur le Terminal"""
        return (f"Abcisse de i={self.i.x} Ordonnee de i={self.i.y} / "
                f"Abcisse de j={self.j.x} Ordonnee de j={self.j.y} / "
                f"Abcisse de k={self.k.x} Ordonnee de k={self.k.y} / "
                f"couleur={self.couleur_tri}")

    def move(self, vect_tri):
        """ Deplace le triangle en ajoutant un vecteur de translation a chaque sommet. """
        # Translation des sommets i, j et k
        self.i.x += vect_tri.x
        self.i.y += vect_tri.y
        self.j.x += vect_tri.x
        self.j.y += vect_tri.y
        self.k.x += vect_tri.x
        self.k.y += vect_tri.y

    def draw(self): #importer prelablement Matplotlib
        """Affiche le triangle sur un graphique en utilisant Matplotlib."""
        # Affichage des sommets
        plt.plot(self.i.x, self.i.y, color=self.couleur_tri, marker='o', markersize=5)
        plt.plot(self.j.x, self.j.y, color=self.couleur_tri, marker='o', markersize=5)
        plt.plot(self.k.x, self.k.y, color=self.couleur_tri, marker='o', markersize=5)
        # Remplissage du triangle
        plt.fill([self.i.x, self.j.x, self.k.x, self.i.x],
                 [self.i.y, self.j.y, self.k.y, self.i.y], color=self.couleur_tri)



####### Partie tests #######
# Initialisation d'un point
X = 0.0
Y = 0.0
COULEUR_P = "black"
p = Point(X, Y, COULEUR_P)

# Initialisation de deux vecteurs
v1 = Vecteur(1, 2, 'green') # Attetion :  mettre les noms des couleurs en anglais
v2 = Vecteur(2, 3, 'black')



# Initialisation des sommets du triangle
I = Vecteur(5, 0, 'red') # Attetion :  mettre les noms des couleurs en anglais
J = Vecteur(12, 3, 'red')
K = Vecteur(9, 9, 'red')

# Creation et affichage d'un triangle vert
TRI = Triangle(I, J, K, 'green')
TRI.draw()

# Rotation du triangle et changement de couleur
TRI = Triangle(I, J, K, 'yellow')
TRI.turn(3.14 / 10)
TRI.draw()

# Translation du triangle rouge
TRI = Triangle(I, J, K, 'red')
TRI.move(Vecteur(4, 4, 'black'))
TRI.draw()

# Affichage final du graphique avec tous les triangles de couleur differentes
plt.show()
