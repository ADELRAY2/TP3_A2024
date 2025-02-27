import math


class Canon:
    """Classe permettant de représenter un canon.

    Attributs:
        canvas (tk.Canvas): La toile où le canon est dessiné.
        angle (float): L'angle du canon.
        baril_du_canon (int): L'identifiant du baril du canon dans la toile.
        base_du_canon (int): L'identifiant de la base du canon dans la toile.
    """

    def __init__(self, canvas, angle):
        """Initialise un objet Canon avec une toile et un angle donné.

        Args:
            canvas (tk.Canvas): La toile où le canon sera dessiné.
            angle (float): L'angle initial du canon.
        """
        self.canvas = canvas
        self.angle = angle
        self.baril_du_canon = None
        self.base_du_canon = None
        self.creer()  # Création du canon

    def creer(self):
        """Crée la base et le baril du canon sur la toile."""
        self.base_du_canon = self.canvas.create_rectangle(
            50, 550, 100, 600, fill="#6366F1", outline=""
        )
        self.baril_du_canon = self.canvas.create_line(
            75,
            575,
            75 + 50 * math.cos(math.radians(self.angle)),
            575 - 50 * math.sin(math.radians(self.angle)),
            width=8,
            fill="#E0E7FF",
            dash=(4, 2),
        )

    def mettre_a_jour(self, angle):
        """Met à jour l'angle du canon et redessine le baril sur la toile afin de refléter le nouvel angle.

        Args:
            angle (float): Le nouvel angle du canon.
        """
        # TODO: À compléter
        # Aide:
        # - Voir comment le baril du canon est créé au niveau de la méthode `creer` définie plus haut.
        self.angle = angle  # Met à jour l'angle du canon

        # Supprime l'ancien baril du canon
        self.canvas.delete(self.baril_du_canon)

        # Calcule les nouvelles coordonnées du baril
        x1, y1 = 75, 575  # Origine du baril
        x2 = x1 + 50 * math.cos(math.radians(self.angle))
        y2 = y1 - 50 * math.sin(math.radians(self.angle))

        # Redessine le baril du canon
        self.baril_du_canon = self.canvas.create_line(
            x1, y1, x2, y2, width=8, fill="#E0E7FF", dash=(4, 2)
        )