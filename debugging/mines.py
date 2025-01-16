#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))  # Positions des mines
        self.field = [[' ' for _ in range(width)] for _ in range(height)]  # Champ de jeu
        self.revealed_cells = [[False for _ in range(width)] for _ in range(height)]  # Cases révélées

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2}", end=' ')  # Affichage des indices de ligne
            for x in range(self.width):
                if reveal or self.revealed_cells[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        """Compte les mines autour de la case (x, y)."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal_cell(self, x, y):
        """Révèle une cellule. Retourne False si une mine est touchée."""
        if (y * self.width + x) in self.mines:
            return False  # Perte de la partie si une mine est touchée
        if self.revealed_cells[y][x]:
            return True  # Ne rien faire si la cellule est déjà révélée

        self.revealed_cells[y][x] = True
        if self.count_mines_nearby(x, y) == 0:  # Si aucune mine alentour, révéler les voisins
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed_cells[ny][nx]:
                        self.reveal_cell(nx, ny)
        return True

    def all_safe_cells_revealed(self):
        """Vérifie si toutes les cases sûres ont été révélées."""
        total_cells = self.width * self.height
        safe_cells = total_cells - len(self.mines)
        revealed_safe_cells = sum(
                1 for y in range(self.height) for x in range(self.width)
                if self.revealed_cells[y][x] and (y * self.width + x) not in self.mines
                )
        return revealed_safe_cells == safe_cells

    def play(self):
        """Boucle principale du jeu."""
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                # Vérification des coordonnées valides
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Invalid coordinates. Please try again.")
                    continue

                # Révéler la cellule et gérer les résultats
                if not self.reveal_cell(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # Vérifier la condition de victoire
                if self.all_safe_cells_revealed():
                    self.print_board(reveal=True)
                    print("Congratulations! You cleared the minefield!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

