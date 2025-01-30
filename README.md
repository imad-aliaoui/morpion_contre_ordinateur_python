# Morpion (Tic-Tac-Toe) avec l'ordinateur

Implémentation du jeu de Morpion (Tic-Tac-Toe) en Python avec une interface graphique créée à l'aide de Tkinter. Le joueur affronte l'ordinateur, qui prend ses décisions en fonction du niveau de difficulté choisi.

## Fonctionnalités

  - Interface graphique : Utilisation de Tkinter pour une expérience utilisateur fluide.
  - Modes de difficulté :
    - Facile : L'ordinateur joue aléatoirement.
    - Moyen : L'ordinateur regarde 2 coups à l'avance pour prendre sa décision.
    - Difficile : L'ordinateur utilise l'algorithme Minimax sans limite et devient imbattable.
  - Rejouabilité : À la fin d'une partie, le joueur peut choisir une nouvelle difficulté et rejouer.
  - Redimensionnement dynamique : L'interface s'adapte à la taille de la fenêtre.
  - Utilisation de l'IA : L'algorithme Minimax a été développé en appliquant des principes d'intelligence artificielle pour permettre à l'ordinateur de prendre des décisions optimales.

## Règles du jeu
  - Le joueur commence toujours en jouant avec le symbole X.
  - L'ordinateur joue avec le symbole O.
  - Chaque joueur joue à tour de rôle en cliquant sur une case.
  - Le premier à aligner trois symboles identiques (horizontalement, verticalement ou en diagonale) remporte la partie.
  - Si toutes les cases sont remplies sans qu’un joueur n’ait aligné trois symboles, la partie se termine par un match nul.

## Structure du code
  - choisir_difficulte() : Affiche une fenêtre pour choisir le niveau de difficulté.
  - creer_plateau() : Initialise l’interface graphique du jeu.
  - clic_case(row, col) : Gère l’action du joueur lorsqu’il clique sur une case.
  - verifier_vainqueur(grille, joueur) : Vérifie si un joueur a gagné.
  - obtenir_cases_vides(grille) : Renvoie la liste des cases vides disponibles.
  - minimax(grille, profondeur, maximisant, limite_profondeur) : Algorithme de décision utilisé par l’ordinateur en mode difficile, basé sur des principes d'intelligence artificielle.
  - coup_ordinateur(grille) : Choisit le meilleur coup pour l’ordinateur en fonction de la difficulté.

# Imad ALIAOUI

