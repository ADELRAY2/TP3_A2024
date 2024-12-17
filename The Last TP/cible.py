import random


class Cible:
    """Classe permettant de représenter une cible.

    Attributs:
        canvas (tk.Canvas): La toile où la cible est dessinée.
        x (int): La position x de la cible.
        y (int): La position y de la cible.
        identifiant (int): L'identifiant de la cible dans la toile.
    """

    def __init__(self, canvas):
        """Initialise un objet Cible avec une toile donnée.

        Args:
            canvas (tk.Canvas): La toile où la cible sera dessinée.
        """
        # TODO: À compléter
        self.canvas = canvas
        self.creer_nouvelle_cible()

    def creer_nouvelle_cible(self):
        """Crée une nouvelle cible à une position aléatoire sur la toile."""
        # TODO: À compléter
        # Aide:
        # - x (une valeur entière aléatoire entre 400 et 750)
        # - y (une valeur entière aléatoire entre 50 et 550)
        # - Se documenter sur la méthode `create_oval` disponible pour les objets Canvas
        self.x = random.randint(400, 750)
        self.y = random.randint(50, 550)
        self.identifiant = self.canvas.create_oval(
            self.x, self.y, self.x + 20, self.y + 20, fill="#FF0000", outline=""
        )
    def est_touchee(self, projectile):
        """Vérifie si la cible est touchée par un projectile aux coordonnées données.

        Cette méthode détermine si le projectile, aux coordonnées spécifiées,
        se trouve dans une zone de 10 unités autour de la cible.

        Args:
            projectile (Projectile): L'objet Projectile dont les coordonnées
            doivent être vérifiées.

        Returns:
            bool: True si le projectile touche la cible, False sinon.
        """
        # TODO: À compléter
        distance_x = abs(self.x - projectile.x)
        distance_y = abs(self.y - projectile.y)
        return distance_x <= 10 and distance_y <= 10