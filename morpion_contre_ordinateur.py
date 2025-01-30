import tkinter as tk
from tkinter import messagebox
import math
import random

# Fonction permettant à l'utilisateur de choisir la difficulté puis ferme la page et lance le jeu
def choisir_difficulte():
    global niveau_difficulte
    
    def set_difficulte(niveau):
        global niveau_difficulte
        niveau_difficulte = niveau  # Définit le niveau de difficulté choisi
        fenetre_choix.destroy()  # Ferme la fenêtre de sélection
        creer_plateau()  # Lance le jeu
    
    fenetre_choix = tk.Tk()
    fenetre_choix.title("Choisir la difficulté")
    fenetre_choix.geometry("300x200")  # Définit une taille initiale
    fenetre_choix.resizable(True, True)  # Permet de redimensionner la fenêtre
    label = tk.Label(fenetre_choix, text="Sélectionnez le niveau de difficulté :", font=("Aptos", 14))
    label.pack(expand=True, fill="both")
    
    # Boutons pour la difficulté
    bouton_facile = tk.Button(fenetre_choix, text="Facile", font=("Aptos", 12), command=lambda: set_difficulte("Facile"))
    bouton_facile.pack(expand=True, fill="both")
    
    bouton_moyen = tk.Button(fenetre_choix, text="Moyen", font=("Aptos", 12), command=lambda: set_difficulte("Moyen"))
    bouton_moyen.pack(expand=True, fill="both")
    
    bouton_difficile = tk.Button(fenetre_choix, text="Difficile", font=("Aptos", 12), command=lambda: set_difficulte("Difficile"))
    bouton_difficile.pack(expand=True, fill="both")
    
    fenetre_choix.mainloop()  # Lance l'interface Tkinter

# Fonction qui vérifie si un joueur a gagné, retourne True si un joueur a trois symboles alignés
def verifier_vainqueur(grille, joueur):
    for ligne in grille:
        if all(cell == joueur for cell in ligne):
            return True
    
    for colonne in range(3):
        if all(grille[ligne][colonne] == joueur for ligne in range(3)):
            return True
    
    if all(grille[i][i] == joueur for i in range(3)) or all(grille[i][2 - i] == joueur for i in range(3)):
        return True
    
    return False

# Retourne la liste des cases vides disponibles sur la grille
def obtenir_cases_vides(grille):
    return [(r, c) for r in range(3) for c in range(3) if grille[r][c] == " "]

# Algorithme Minimax utilisé par l'ordinateur pour choisir le meilleur coup
def minimax(grille, profondeur, maximisant, limite_profondeur):
    if verifier_vainqueur(grille, "O"):
        return 1  # L'ordinateur gagne
    if verifier_vainqueur(grille, "X"):
        return -1  # Le joueur gagne
    if not obtenir_cases_vides(grille) or profondeur == limite_profondeur:
        return 0  # Match nul ou limite atteinte
    
    if maximisant:
        meilleur_score = -math.inf
        for (r, c) in obtenir_cases_vides(grille):
            grille[r][c] = "O"
            score = minimax(grille, profondeur + 1, False, limite_profondeur)
            grille[r][c] = " "
            meilleur_score = max(score, meilleur_score)
        return meilleur_score
    else:
        pire_score = math.inf
        for (r, c) in obtenir_cases_vides(grille):
            grille[r][c] = "X"
            score = minimax(grille, profondeur + 1, True, limite_profondeur)
            grille[r][c] = " "
            pire_score = min(score, pire_score)
        return pire_score

# Fonction permettant à l'ordinateur de choisir un coup en fonction de la difficulté
def coup_ordinateur(grille):
    if niveau_difficulte == "Facile":
        return random.choice(obtenir_cases_vides(grille))  # Choix aléatoire
    elif niveau_difficulte == "Moyen":
        limite_profondeur = 2  # L'ordinateur regarde 2 coups à l'avance
    else:
        limite_profondeur = 3  # L'ordinateur regare 3 coups à l'avance
    
    meilleur_score = -math.inf
    meilleur_coup = None
    for (r, c) in obtenir_cases_vides(grille):
        grille[r][c] = "O"
        score = minimax(grille, 0, False, limite_profondeur)
        grille[r][c] = " "
        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = (r, c)
    return meilleur_coup


# Gère le clic du joueur
def clic_case(ligne, colonne):
    global tour, grille, root
    if grille[ligne][colonne] != " " or verifier_vainqueur(grille, "X") or verifier_vainqueur(grille, "O"):
        return
    
    grille[ligne][colonne] = tour
    boutons[ligne][colonne].config(text=tour)
    
    if verifier_vainqueur(grille, tour):
        messagebox.showinfo("Fin de partie", f"{tour} a gagné !")
        root.destroy()
        choisir_difficulte()
    elif not obtenir_cases_vides(grille):
        messagebox.showinfo("Fin de partie", "Match nul !")
        root.destroy()
        choisir_difficulte()
    else:
        tour = "O" if tour == "X" else "X"
        if tour == "O":
            ia_ligne, ia_colonne = coup_ordinateur(grille)
            clic_case(ia_ligne, ia_colonne)

# Crée et affiche l'interface graphique
def creer_plateau():
    global root, boutons, grille, tour
    root = tk.Tk()
    root.title("Morpion")
    root.geometry("400x400")  
    root.resizable(True, True) 
    
    grille = [[" " for _ in range(3)] for _ in range(3)]
    boutons = [[None for _ in range(3)] for _ in range(3)]
    
    for r in range(3):
        for c in range(3):
            boutons[r][c] = tk.Button(root, text=" ", font=("Aptos", 24), width=5, height=2, command=lambda r=r, c=c: clic_case(r, c))
            boutons[r][c].grid(row=r, column=c, sticky="nsew")
    
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)
    
    tour = "X"
    root.mainloop()

# Lance le choix de difficulté
if __name__ == "__main__":
    choisir_difficulte()