import matplotlib.pyplot as plt

class Vecteur:
    def __init__(self, x, y, color):
        # Initialisation des coordonnées x, y et de la couleur
        self.x = x
        self.y = y
        self.color = color

    def display_info(self):
        # Affichage des informations du vecteur
        print(f"Coordonnées : ({self.x}, {self.y})")
        print(f"Couleur : {self.color}")
    
    # Méthode pour dessiner le point aux bonnes coordonnées et avec la bonne couleur
    def dessiner(self):
        plt.scatter(self.x, self.y, color=self.color)  # Dessiner le point
        plt.text(self.x, self.y, f"({self.x}, {self.y})", fontsize=12, ha='right')  # Ajouter une légende
        plt.xlim(-10, 10)  # Limites des axes
        plt.ylim(-10, 10)
        plt.grid(True)  # Afficher la grille
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f"Point ({self.x}, {self.y}) en {self.color}")
    
    # Surcharge de l'opérateur +
    def __add__(self, other):
        return Vecteur(self.x + other.x, self.y + other.y, self.color)
    
    # Surcharge de l'opérateur -
    def __sub__(self, other):
        return Vecteur(self.x - other.x, self.y - other.y, self.color)
    
    # Surcharge de l'opérateur *
    # Multiplication par un scalaire
    def __mul__(self, scalar):
        return Vecteur(self.x * scalar, self.y * scalar, self.color)
    
    # Surcharge de l'opérateur /
    # Division par un scalaire
    def __truediv__(self, scalar):
        return Vecteur(self.x / scalar, self.y / scalar, self.color)

# Exemple d'utilisation

# Création de deux vecteurs
vecteur1 = Vecteur(1, 2, "red")
vecteur2 = Vecteur(3, 4, "blue")

# Affichage des vecteurs
print("Vecteur 1 :")
vecteur1.display_info()

print("\nVecteur 2 :")
vecteur2.display_info()

# Addition des vecteurs
vecteur_add = vecteur1 + vecteur2
print("\nRésultat de l'addition :")
vecteur_add.display_info()

# Multiplication par un scalaire
vecteur_mul = vecteur1 * 2
print("\nMultiplication par un scalaire :")
vecteur_mul.display_info()

# Dessiner les vecteurs
plt.figure(figsize=(5, 5))  # Ajuster la taille de la figure
vecteur1.dessiner()
vecteur2.dessiner()

# Afficher le graphique
plt.show()