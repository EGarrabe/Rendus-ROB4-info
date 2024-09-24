# Bastien Couque/ Joshua Hauzay
from multipledispatch import dispatch
import matplotlib.pyplot as plt
import colorsys
import math

class Point():  # On définit la classe Point
    def _init_(self, x: int, y: int, color: str):  # Attributs de la classe
        self.x = x
        self.y = y
        self.color = color

    def affiche(self):  # On affiche les coordonnées du vecteur
        print(f"Point: ({self.x}, {self.y}), Couleur: {self.color}")

    def dessiner(self):  # Fonction pour dessiner un point dans un repère
        plt.scatter(self.x, self.y, c=self.color)
        plt.title("Point Origine")
        plt.xlabel("Axe X")
        plt.ylabel("Axe Y")
        plt.grid(True)
        plt.show()

class Vecteur():
    def _init_(self, x1: int, y1: int, colorv: str):  # Attributs du vecteur
        self.x1 = x1
        self.y1 = y1
        self.colorv = colorv

    @dispatch(int, int)
    def addi(self, x2, y2):  # Addition de vecteurs
        self.x1 += x2
        self.y1 += y2

    @dispatch(int, int)
    def soust(self, x2, y2):  # Soustraction de vecteurs
        self.x1 -= x2
        self.y1 -= y2

    @dispatch(int)
    def multi(self, s):  # Multiplication scalaire
        self.x1 *= s
        self.y1 *= s

    @dispatch(int)
    def divi(self, s):  # Division scalaire
        self.x1 /= s
        self.y1 /= s

    def affichevect(self):  # On affiche les coordonnées du vecteur
        print("[", self.x1, ",", self.y1, "]")

class Triangle():
    def _init_(self, point1: Point, point2: Point, point3: Point):  # On définit le triangle par trois points
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def tourner(self, alpha):  
        # On effectue la rotation pour chaque point x'=x*cos(a)-y*sin(b) et y'=x*sin(a)+y*cos(a)
        x1_temp = self.point1.x  # on utilise x1_temp pour pouvoir effectuer la rotation 
        y1_temp = self.point1.y
        x2_temp = self.point2.x
        y2_temp = self.point2.y
        x3_temp = self.point3.x
        y3_temp = self.point3.y
        self.point1.x = x1_temp * math.cos(alpha) - y1_temp * math.sin(alpha)
        self.point1.y = x1_temp * math.sin(alpha) + y1_temp * math.cos(alpha)
        self.point2.x = x2_temp * math.cos(alpha) - y2_temp * math.sin(alpha)
        self.point2.y = x2_temp * math.sin(alpha) + y2_temp * math.cos(alpha)
        self.point3.x = x3_temp * math.cos(alpha) - y3_temp * math.sin(alpha)
        self.point3.y = x3_temp * math.sin(alpha) + y3_temp * math.cos(alpha)

    def afficher(self):  # On affiche les vecteurs constituant le triangle
        print("[", self.point2.x - self.point1.x, ",", self.point2.y - self.point1.y, "]")
        print("[", self.point3.x - self.point2.x, ",", self.point3.y - self.point2.y, "]")
        print("[", self.point3.x - self.point1.x, ",", self.point3.y - self.point1.y, "]")

    def translation(self, x1, y1, color):  
        # On introduit dans la fonction les composantes d'un vecteur pour le construire dans la fonction et effectuer la translation
        vecteur = Vecteur(x1, y1, color)
        self.point3.x += vecteur.x1
        self.point3.y += vecteur.y1
        self.point2.x += vecteur.x1
        self.point2.y += vecteur.y1
        self.point1.x += vecteur.x1
        self.point1.y += vecteur.y1

    def dessiner(self):  
        # Liste des coordonnées des x et y pour utiliser plot
        liste_x = [self.point1.x, self.point2.x, self.point3.x, self.point1.x]
        liste_y = [self.point1.y, self.point2.y, self.point3.y, self.point1.y]
        plt.fill(liste_x, liste_y, c=self.point1.color)  # Triangle rempli de couleur noire
        plt.plot(liste_x, liste_y, c=self.point1.color)

def main():

    # Étape 1 : On crée un point origine qu'on affiche
    origine = Point(0, 0, 'black')
    origine.affiche()
    origine.dessiner()

    # Étape 2 : Opérations de base et affichage sur des vecteurs
    vecteur = Vecteur(3, 4, 'w')
    vecteur.affichevect()
    vecteur.soust(1, 2)
    vecteur.affichevect()

    # Étape 3 : On crée un triangle, on lui fait subir une rotation de pi/2, puis on le translate d'un vecteur de [1 1]
    point1 = Point(0, 0, 'black')
    point2 = Point(1, 0, 'black')
    point3 = Point(1, 1, 'black')
    triangle = Triangle(point1, point2, point3)  # Création de l'objet triangle
    triangle.dessiner()  # Premier affichage
    triangle.tourner(90 * math.pi / 180)  # Rotation du triangle
    triangle.dessiner()  # Réaffichage pour vérification
    triangle.translation(1, 1, 'black')  # Translation du triangle après rotation
    triangle.dessiner()  # Affichage pour vérification
    plt.title("Transformation du triangle final")
    plt.xlabel("Axe X")
    plt.ylabel("Axe Y")
    plt.grid(True)
    plt.show()

main()