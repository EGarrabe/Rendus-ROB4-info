# DARDE Romain & CHAUVET Antonin

import math
import matplotlib.pyplot as plt

class Point():
    # constructreur
    def __init__(self, x: float, y: float, couleur: str):
        self.x = x
        self.y = y
        self.couleur = couleur

    # fonction d'affichage
    def affichage(self):
        print("[ " + str(self.x) + ", " + str(self.y) + " ]" + " Couleur : " + str(self.couleur))

    def __str__(self):
        return "[ " + str(self.x) + ", " + str(self.y) + " ]" + " Couleur : " + str(self.couleur)

    # affichage avec matplotlib
    def affichageGraphique(self):
        plt.scatter(self.x, self.y, color = self.couleur) # affichage du point
        plt.text(self.x, self.y, f"({round(self.x, 3)}, {round(self.y, 3)})", fontsize=10) # affichage des coordonnées du point

    # surchage de l'opérateur +
    def __add__(self, autreVecteur):
        return Vecteur(self.x + autreVecteur.x, self.y + autreVecteur.y, autreVecteur.couleur)

    # surchage de l'opérateur -
    def __sub__(self, autreVecteur):
        return Vecteur(self.x - autreVecteur.x, self.y - autreVecteur.y, autreVecteur.couleur)

    # surchage de l'opérateur *
    def __mul__(self, scalaire):
        return Vecteur(self.x * scalaire, self.y * scalaire, self.couleur)

    # surchage de l'opérateur /
    def __truediv__(self, scalaire):
        return Vecteur(self.x / scalaire, self.y / scalaire, self.couleur)


# Vecteur hérite du point (et donc des fonctions d'affichage de Point)
class Vecteur(Point):
    # constructeur
    def __init__(self, x: int, y: int, couleur: str):
        super().__init__(x, y, couleur)


class Triangle():
    # constructeur
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    # fonction tourner
    def tourner(self, angle: float):
        # conversion en radian de l'angle
        angle = math.radians(angle)

        # stockage temporaire des coordonnées des points pour effectuer les calculs
        x1_temp = self.point1.x
        y1_temp = self.point1.y
        self.point1.x = x1_temp * math.cos(angle) - y1_temp * math.sin(angle)
        self.point1.y = x1_temp * math.sin(angle) + y1_temp * math.cos(angle)

        x2_temp = self.point2.x
        y2_temp = self.point2.y
        self.point2.x = x2_temp * math.cos(angle) - y2_temp * math.sin(angle)
        self.point2.y = x2_temp * math.sin(angle) + y2_temp * math.cos(angle)

        x3_temp = self.point3.x
        y3_temp = self.point3.y
        self.point3.x = x3_temp * math.cos(angle) - y3_temp * math.sin(angle)
        self.point3.y = x3_temp * math.sin(angle) + y3_temp * math.cos(angle)

    # afficher coordonnées des points
    def affichage(self):
        print("Le triangle a pour points : ")
        print("Point 1 : ", self.point1)
        print("Point 2 : ", self.point3)
        print("Point 3 : ", self.point3)

    # translation du triangle
    def translation(self, vecteur: Vecteur):
        self.point1 = self.point1 + vecteur
        self.point2 = self.point2 + vecteur
        self.point3 = self.point3 + vecteur

    # fonction dessiner le triangle avec matplotlib
    def dessiner(self):
        self.point1.affichageGraphique()
        self.point2.affichageGraphique()
        self.point3.affichageGraphique()
        plt.plot([self.point1.x, self.point2.x], [self.point1.y, self.point2.y], color="black")
        plt.plot([self.point2.x, self.point3.x], [self.point2.y, self.point3.y], color="black")
        plt.plot([self.point3.x, self.point1.x], [self.point3.y, self.point1.y], color="black")
        plt.fill([self.point1.x, self.point2.x, self.point3.x], [self.point1.y, self.point2.y, self.point3.y], 0.5, color=self.point1.couleur) # 0.5 pour l'opacité du remplissage des triangles

    # changement de couleur du triangle
    def changementCouleur(self, nouvCouleur: str):
        self.point1.couleur = nouvCouleur
        self.point2.couleur = nouvCouleur
        self.point3.couleur = nouvCouleur


def main():
    # création et affichage d'un point
    p = Point(0, 0, "black")
    p.affichage()
    print(p)

    # création et affichage d'un vecteur
    v = Vecteur(1, 2, "red")
    v.affichage()
    print(v)

    # test des surchages
    print("\nTests Surcharges")
    v1 = Vecteur(2, 6, "red")
    v2 = Vecteur(3, 4, "blue")
    # addition
    print(v1, "+", v2)
    print("=", v1 + v2)
    # soustraction
    print(v1, "-", v2)
    print("=", v1 - v2)
    scalaire = 2
    # multiplication
    print(v1, "*", scalaire)
    print("=", v * scalaire)
    # sousrtaction
    print(v1, "/", scalaire)
    print("=", v1 - v2, "\n")

    # création des sommets du triangle
    p1 = Point(0, 0, "red")
    p2 = Point(6, 0, "red")
    p3 = Point(3, 3, "red")

    # création du triangle
    t = Triangle(p1, p2, p3)

    # affichage des coordonnées des sommets du triangle
    t.affichage()

    # duplication du triangle
    t2 = t

    # dessin du premier triangle
    t.dessiner()

    # rotation et dessin du triangle 2
    t2.tourner(90)
    t2.changementCouleur("green")
    t2.dessiner()

    # duplication du triangle tourné
    t3 = t2

    # translation et affichage du triangle tourné
    t3.translation(v)
    t3.changementCouleur("blue")
    t3.dessiner()

    # affichage de la grille et de la figure
    plt.grid(True)
    plt.show()

main()
