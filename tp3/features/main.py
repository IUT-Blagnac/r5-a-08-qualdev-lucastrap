# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Définition d'une classe pour la Courbe elliptique avec des méthodes nécessaires
class CourbeElliptique:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def a_point(self, x, y):
        # Vérifie si un point (x, y) appartient à la courbe elliptique
        return (y ** 2) % self.p == (x ** 3 + self.a * x + self.b) % self.p

    def points_courbe(self):
        # Génère des points sur la courbe elliptique
        x_vals = []
        y_vals = []

        for x in range(self.p):
            for y in range(self.p):
                if self.a_point(x, y):
                    x_vals.append(x)
                    y_vals.append(y)

        return x_vals, y_vals

    def __str__(self):
        # Représentation sous forme de chaîne de la courbe elliptique
        return 'y^2 = x^3 + {}x + {}'.format(self.a, self.b)

# Définition d'une classe pour l'application principale
class ApplicationTraceCourbe:
    def __init__(self, root):
        # Initialisation de l'application
        self.root = root
        self.root.title("Traceur de Courbe Elliptique")

        # Création d'une courbe fictive avec des valeurs par défaut
        self.courbe = CourbeElliptique(a=0, b=7, p=17)
        self.montrer_points = True  # Indicateur pour montrer les points ou la courbe

        # Création d'un cadre pour contenir les widgets d'entrée des paramètres en bas
        cadre_param = tk.Frame(root)
        cadre_param.pack(side=tk.BOTTOM, pady=10)

        # Ajout des étiquettes et des widgets d'entrée pour a, b, et p
        tk.Label(cadre_param, text="a:").pack(side=tk.LEFT)
        self.a_entree = tk.Entry(cadre_param)
        self.a_entree.pack(side=tk.LEFT)
        self.a_entree.insert(0, "0")  # Valeur par défaut pour a

        tk.Label(cadre_param, text="b:").pack(side=tk.LEFT)
        self.b_entree = tk.Entry(cadre_param)
        self.b_entree.pack(side=tk.LEFT)
        self.b_entree.insert(0, "7")  # Valeur par défaut pour b

        tk.Label(cadre_param, text="p:").pack(side=tk.LEFT)
        self.p_entree = tk.Entry(cadre_param)
        self.p_entree.pack(side=tk.LEFT)
        self.p_entree.insert(0, "17")  # Valeur par défaut pour p

        # Création d'un canevas matplotlib dans la fenêtre tkinter
        self.canevas = FigureCanvasTkAgg(plt.figure(), master=root)
        self.canevas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Mise à jour du tracé
        self.maj_tracé()

        # Ajout des boutons "Mettre à jour la courbe" et "Basculer Points/Courbe"
        bouton_maj = tk.Button(root, text="Mettre à jour la courbe", command=self.maj_courbe)
        bouton_maj.pack(side=tk.BOTTOM, pady=5)

        bouton_basculer = tk.Button(root, text="Basculer Points/Courbe", command=self.basculer_points_courbe)
        bouton_basculer.pack(side=tk.BOTTOM, pady=5)

    def maj_courbe(self):
        # Met à jour la courbe avec de nouvelles valeurs des widgets d'entrée
        try:
            a = int(self.a_entree.get())
            b = int(self.b_entree.get())
            p = int(self.p_entree.get())
        except ValueError:
            # Gère le cas où les entrées ne sont pas des entiers valides
            return

        self.courbe = CourbeElliptique(a=a, b=b, p=p)
        self.maj_tracé()

    def basculer_points_courbe(self):
        # Bascule entre l'affichage des points et l'affichage de la courbe
        self.montrer_points = not self.montrer_points
        self.maj_tracé()

    def maj_tracé(self):
        # Efface le tracé actuel et le met à jour avec la courbe ou les points actuels
        plt.clf()

        # Vérifie si les widgets d'entrée ont des valeurs non vides
        if not all(entry.get() for entry in [self.a_entree, self.b_entree, self.p_entree]):
            # Affiche un message ou gère le cas où les entrées sont vides
            return

        plt.axis('equal')  # Définit un rapport d'aspect égal

        if self.montrer_points:
            # Affiche les points sur la courbe sans étiquette
            x_vals, y_vals = self.courbe.points_courbe()
            plt.scatter(x_vals, y_vals, color='blue', s=10)

        else:
            # Affiche la courbe en utilisant la formule
            a = int(self.a_entree.get())
            b = int(self.b_entree.get())
            p = int(self.p_entree.get())
            y, x = np.ogrid[-10:10:100j, -10:10:100j]
            plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - a * x - b, [0], colors='blue', linewidths=2,
                        linestyles='solid')

        plt.grid()
        plt.title('Courbe Elliptique: {}'.format(self.courbe))
        plt.xlabel('x')
        plt.ylabel('y')

        # Ajoute une légende uniquement si la courbe est affichée
        if not self.montrer_points:
            plt.legend()

        # Redessine le canevas
        self.canevas.draw()

# Point d'entrée pour l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationTraceCourbe(root)
    root.mainloop()
