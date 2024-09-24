class Point:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur

    def afficher_point(self):
        print(f"Point({self.x}, {self.y}), Couleur: {self.couleur}")

# Créer un point par défaut (0, 0, noir)
point_defaut = Point(0,0,"Noir")

# Afficher les informations du point
point_defaut.afficher_point()
