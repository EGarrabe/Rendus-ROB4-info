#VEUILLEZ DECOMMENTER LES DERNIÈRE LIGNES POUR TESTER LES DIFFÉRENTES FONCTIONS
#AYOUB HADJAB - MATHYS CLAUDEL - CLARENCE PFISTER


import math
import matplotlib.pyplot as plt

# Classe Point
class Point:
    def __init__(self, x, y, color="noir"):
        self.x = x
        self.y = y
        self.color = color

    def afficher_info(self):
        print(f"Coordonnées : ({self.x}, {self.y})")
        print(f"Couleur : {self.color}")

    def dessiner(self):
        plt.scatter(self.x, self.y, color=self.color)
        plt.text(self.x, self.y, f"({self.x}, {self.y})", fontsize=12, ha='right')

    def tourner_autour_origine(self, angle):
        radians = math.radians(angle)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        self.x = new_x
        self.y = new_y

    def deplacer(self, dx, dy):
        self.x += dx
        self.y += dy


class Vecteur:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def afficher_info(self):
        print(f"Coordonnées : ({self.x}, {self.y})")
        print(f"Couleur : {self.color}")

    def dessiner(self):
        plt.scatter(self.x, self.y, color=self.color)
        plt.text(self.x, self.y, f"({self.x}, {self.y})", fontsize=12, ha='right')
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.grid(True)
        plt.xlabel('X')
        plt.ylabel('Y')

    def __add__(self, other):
        return Vecteur(self.x + other.x, self.y + other.y, self.color)

    def __sub__(self, other):
        return Vecteur(self.x - other.x, self.y - other.y, self.color)

    def __mul__(self, scalar):
        return Vecteur(self.x * scalar, self.y * scalar, self.color)

    def __truediv__(self, scalar):
        return Vecteur(self.x / scalar, self.y / scalar, self.color)


class Triangle:
    def __init__(self, p1, p2, p3, color="noir"):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color

    def afficher_info(self):
        print("Triangle :")
        self.p1.afficher_info()
        self.p2.afficher_info()
        self.p3.afficher_info()
        print(f"Couleur : {self.color}")

    def dessiner(self):
        plt.fill([self.p1.x, self.p2.x, self.p3.x], [self.p1.y, self.p2.y, self.p3.y], self.color, alpha=0.5)
        self.p1.dessiner()
        self.p2.dessiner()
        self.p3.dessiner()

    def tourner(self, angle):
        self.p1.tourner_autour_origine(angle)
        self.p2.tourner_autour_origine(angle)
        self.p3.tourner_autour_origine(angle)

    def afficher(self):
        print(f"Vecteur 1 : Point 1 -> Point 2, Coordonnées : ({self.p1.x}, {self.p1.y}) -> ({self.p2.x}, {self.p2.y})")
        print(f"Vecteur 2 : Point 2 -> Point 3, Coordonnées : ({self.p2.x}, {self.p2.y}) -> ({self.p3.x}, {self.p3.y})")
        print(f"Vecteur 3 : Point 3 -> Point 1, Coordonnées : ({self.p3.x}, {self.p3.y}) -> ({self.p1.x}, {self.p1.y})")

    def deplacer(self, dx, dy):
        self.p1.deplacer(dx, dy)
        self.p2.deplacer(dx, dy)
        self.p3.deplacer(dx, dy)


def partie_vecteur():
    print("=== Partie Vecteur ===")
    vecteur1 = Vecteur(1, 2, "red")
    vecteur2 = Vecteur(3, 4, "blue")

    print("Vecteur 1 :")
    vecteur1.afficher_info()

    print("\nVecteur 2 :")
    vecteur2.afficher_info()

    vecteur_add = vecteur1 + vecteur2
    print("\nRésultat de l'addition :")
    vecteur_add.afficher_info()

    vecteur_mul = vecteur1 * 2
    print("\nMultiplication par un scalaire :")
    vecteur_mul.afficher_info()

    vecteur_div = vecteur2 / 2
    print("\nDivision du vecteur 2 par un scalaire :")
    vecteur_div.afficher_info()

    plt.figure(figsize=(5, 5))
    vecteur1.dessiner()
    vecteur2.dessiner()
    plt.show()


def partie_triangle_rotation():
    print("=== Partie Triangle et Rotation ===")
    point1 = Point(5, 5, "red")
    point2 = Point(4, 0, "green")
    point3 = Point(2, 3, "blue")

    triangle = Triangle(point1, point2, point3, "cyan")

    triangle.afficher_info()

    plt.figure(figsize=(5, 5))
    triangle.dessiner()

    triangle.tourner(180)

    triangle.color = "red"
    triangle.dessiner()
    plt.show()


def partie_triangle_translation():
    print("=== Partie Triangle et Translation ===")
    point1 = Point(0, 0, "red")
    point2 = Point(4, 0, "green")
    point3 = Point(2, 3, "blue")

    triangle = Triangle(point1, point2, point3, "cyan")

    triangle.afficher()

    plt.figure(figsize=(5, 5))
    triangle.dessiner()

    triangle.deplacer(-4, -6)

    triangle.color = "red"
    print("\nAprès déplacement :")
    triangle.afficher()

    triangle.dessiner()
    plt.show()


def main(partie):
    if partie == 1:
        partie_vecteur()
    elif partie == 2:
        partie_triangle_rotation()
    elif partie == 3:
        partie_triangle_translation()
    else:
        print("Partie non reconnue. Veuillez entrer 1, 2 ou 3.")


# Exemple d'utilisation
# Appeler main(1) pour tester la partie Vecteur
# Appeler main(2) pour tester la partie Triangle et Rotation
# Appeler main(3) pour tester la partie Triangle et Translation

#main(1)  # Décommentez pour tester la première partie
#main(2)  # Décommentez pour tester la deuxième partie
#main(3)  # Décommentez pour tester la troisième partie
