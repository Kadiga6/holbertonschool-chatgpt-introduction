def print_board(board):
    """Affiche le tableau de Tic-Tac-Toe."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Vérifie si un joueur a gagné."""
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    """Jeu principal de Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]  # Initialiser la grille
    player = "X"

    while True:
        print_board(board)

        # Demander au joueur où il veut jouer
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter values between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Effectuer le mouvement
        board[row][col] = player

        # Vérifier si quelqu'un a gagné
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Vérifier si le jeu est plein (match nul)
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a draw!")
            break

        # Changer de joueur
        player = "O" if player == "X" else "X"

# Démarrer le jeu
tic_tac_toe()

