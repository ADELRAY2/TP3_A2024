# TODO: À compléter
import tkinter as tk
from tkinter import messagebox
class ValeurHorsLimites(Exception):
    """Exception levée lorsque les valeurs de l'angle ou de la puissance sont hors limites."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message
    def affichage_de_lerreur (self):
        messagebox.showerror("Erreur", self.message)
        '''
        Voici une sollution sans message box que j'avais uttiliser avant de voir qu'il existait deja une facon d'afficher l'erreur:
        f= tk.Toplevel()
        f.title("Erreur")
        f.geometry("400x300")
        label = tk.Label(f, text={self.message},font=("Arial",15),wraplength=280,)
        label.pack()
        bouton_ok = tk.Button(
            f,text="OK",command=f.destroy,  # Ferme la fenêtre en cliquant sur OK
            bg="#3396ff",fg="white",width=20,)
        bouton_ok.pack(pady=10)
        f.mainloop()'''