import tkinter as tk


class Classement:
    """Classe pour gérer la fonctionnalité de classement.

    Attributs:
        nom_fichier (str): Le nom du fichier où les scores sont sauvegardés.
        scores (list): Une liste de tuples contenant les noms et scores.
        fenetre_classement (tk.Toplevel): La fenêtre de classement.
    """

    def __init__(self, nom_fichier="classement.txt"):
        """Initialise un objet Classement avec un nom de fichier donné.

        Args:
            nom_fichier (str): Le nom du fichier où les scores sont sauvegardés. Par défaut "classement.txt".
        """
        self.nom_fichier = "classement.txt"
        self.scores = self.charger_scores()
        self.fenetre_classement = None

    def charger_scores(self):
        """Charge les scores à partir du fichier de classement.

        Cette méthode lit le fichier de classement spécifié par l'attribut
        `nom_fichier`, et extrait les scores sous forme de tuples (nom, score).
        Les scores sont triés par ordre décroissant et seules les dix meilleures
        entrées sont conservées.

        Returns:
            list: Une liste triée de tuples contenant les noms et scores. Si le
            fichier de classement n'existe pas, une liste vide est retournée.

        Exemple de contenu du fichier de classement:
            Le fichier `classement.txt` doit avoir le format suivant, avec chaque ligne
            contenant un nom et un score séparés par une virgule:

            John,100
            Alice,30
            Bob,50
            Eve,0
            Charlie,10

        Exemple de sortie:
            Si le fichier `classement.txt` contient les lignes ci-dessus, la méthode
            retournera:

            [('John', 100), ('Bob', 50), ('Alice', 30), ('Charlie', 10), ('Eve', 0)]
        """
        # TODO: À compléter <<Isaac's Done ;)>>
        creation=open(self.nom_fichier, 'a')
        creation.close()
        premiereliste=[]
        if not self.nom_fichier:
            return premiereliste

        with open(self.nom_fichier, "r") as fichier:
            # Vérifier si le fichier n'est pas vide avant de sauter la ligne d'en-tête
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne:  # Ignorer les lignes vides
                    nom, score=ligne.split(",")
                    realscore=int(score)
                    premiereliste.append((nom, realscore))
        listefinal=sorted(premiereliste, key=lambda x: x[1], reverse=True)
        return listefinal

    def enregistrer_score(self, nom, score):
        """Enregistre un nouveau score dans le classement.

        Args:
            nom (str): Le nom du joueur.
            score (int): Le score du joueur.
        """
        self.scores.append((nom, score))
        # Tri des scores par ordre décroissant et on conserve que les 10 meilleurs scores
        self.scores = sorted(self.scores, key=lambda x: x[1], reverse=True)[:10]
        with open(self.nom_fichier, "a") as f:
            f.write(f"{nom},{score}\n")

    def afficher(self):
        """Affiche la fenêtre du classement avec les 10 meilleurs scores."""
        # Vérifie si la fenêtre de classement existe et est ouverte
        if (
            self.fenetre_classement is not None
            and self.fenetre_classement.winfo_exists()
        ):
            self.fenetre_classement.lift()  # Ramener la fenêtre au premier plan
            return

        self.fenetre_classement = tk.Toplevel()  # Création d'une nouvelle fenêtre
        self.fenetre_classement.geometry("300x300")
        self.fenetre_classement.title("Classement")
        tk.Label(
            self.fenetre_classement,
            text="Les 10 meilleurs scores",
            font=("Helvetica", 16),
        ).pack(anchor=tk.W, padx=10, pady=10)
        # TODO: À compléter <<Isaac's Done ;)>>
        # Aide:
        # Vérifier s'il y a des scores à afficher
        #  - Si oui, afficher les numéros de classement (1., 2., 3., etc.), les noms et les scores
        #  - Si aucun score n'est enregistré, afficher un message par défaut
        #    (Ex: -- Aucun score enregistré pour l'instant --)
        if self.scores:
            self.scores = sorted(self.scores, key=lambda x: x[1], reverse=True)[:10]
            for paire in self.scores:
                tk.Label(self.fenetre_classement,
                text=f"{self.scores.index(paire)+1}. {paire[0]}:{paire[1]}",
                font=("Helvetica", 13)).pack(anchor=tk.W, padx=10, pady=10)

             #tk.Label(self.fenetre_classement,
                #text=f"1. {self.scores[0][0]}:{self.scores[0][1]}\n2. {self.scores[1][0]=None}:{self.scores[1][1]=None}\n3. {self.scores[2][0]=None}:{self.scores[2][1]=None}\n4. {self.scores[3][0]}:{self.scores[3][1]}\n5. {self.scores[4][0]}:{self.scores[4][1]}\n6. {self.scores[5][0]}:{self.scores[5][1]}\n7. {self.scores[6][0]}:{self.scores[6][1]}\n8. {self.scores[7][0]}:{self.scores[7][1]}\n9. {self.scores[8][0]}:{self.scores[8][1]}\n10. {self.scores[9][0]}:{self.scores[9][1]}",
            #font=("Helvetica", 13)).pack(anchor=tk.W, padx=10, pady=10)
        else:
            tk.Label(self.fenetre_classement,
                text="-- Aucun score enregistré pour l'instant --",
            font=("Helvetica", 13)).pack(anchor=tk.W, padx=10, pady=10)


