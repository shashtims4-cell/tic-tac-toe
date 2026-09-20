# Tic-Tac-Toe with Simple AI using Minimax
# Internship Task 2

# -------------------------------------------------
# Display the Tic-Tac-Toe board
# -------------------------------------------------
def display_board(board):
    print()
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")
    print()


# -------------------------------------------------
# Check whether a player has won
# -------------------------------------------------
def check_winner(board, player):

    winning_combinations = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Middle column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Diagonal
        (2, 4, 6)   # Diagonal
    ]

    for combination in winning_combinations:
        a, b, c = combination

        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


# -------------------------------------------------
# Check whether the board is full
# -------------------------------------------------
def is_board_full(board):

    for position in board:
        if position not in ["X", "O"]:
            return False

    return True


# -------------------------------------------------
# Minimax algorithm for the computer
# -------------------------------------------------
def minimax(board, maximizing):

    # If computer wins
    if check_winner(board, "O"):
        return 1

    # If user wins
    if check_winner(board, "X"):
        return -1

    # If game is a draw
    if is_board_full(board):
        return 0

    # Computer's turn
    if maximizing:

        best_score = -1000

        for i in range(9):

            if board[i] not in ["X", "O"]:

                original_value = board[i]

                board[i] = "O"

                score = minimax(board, False)

                board[i] = original_value

                best_score = max(best_score, score)

        return best_score

    # User's turn
    else:

        best_score = 1000

        for i in range(9):

            if board[i] not in ["X", "O"]:

                original_value = board[i]

                board[i] = "X"

                score = minimax(board, True)

                board[i] = original_value

                best_score = min(best_score, score)

        return best_score


# -------------------------------------------------
# Find the best move for the computer
# -------------------------------------------------
def computer_move(board):

    best_score = -1000
    best_move = None

    for i in range(9):

        if board[i] not in ["X", "O"]:

            original_value = board[i]

            # Computer makes a temporary move
            board[i] = "O"

            score = minimax(board, False)

            # Undo temporary move
            board[i] = original_value

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


# -------------------------------------------------
# Main game
# -------------------------------------------------
def play_game():

    # Numbers represent empty positions
    board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]

    print("\n==============================")
    print("      TIC-TAC-TOE AI")
    print("==============================")

    print("\nYou are X")
    print("Computer is O")

    print("\nBoard positions:")
    display_board(board)

    # Game continues until someone wins or draw
    while True:

        # -----------------------------------------
        # USER MOVE
        # -----------------------------------------
        while True:

            try:
                position = int(input("Enter your position (1-9): "))

                if position < 1 or position > 9:
                    print("Please enter a number between 1 and 9.")
                    continue

                index = position - 1

                if board[index] in ["X", "O"]:
                    print("That position is already occupied.")
                    continue

                break

            except ValueError:
                print("Invalid input. Please enter a number from 1 to 9.")

        # Place user's X
        board[index] = "X"

        print("\nYour move:")
        display_board(board)

        # Check whether user won
        if check_winner(board, "X"):
            print("Congratulations! You WIN! 🎉")
            break

        # Check whether game is draw
        if is_board_full(board):
            print("It's a DRAW! 🤝")
            break

        # -----------------------------------------
        # COMPUTER MOVE
        # -----------------------------------------
        print("Computer is thinking...")

        move = computer_move(board)

        board[move] = "O"

        print("\nComputer's move:")
        display_board(board)

        # Check whether computer won
        if check_winner(board, "O"):
            print("Computer WINS! 🤖")
            print("Better luck next time!")
            break

        # Check whether game is draw
        if is_board_full(board):
            print("It's a DRAW! 🤝")
            break


# -------------------------------------------------
# Start the game
# -------------------------------------------------
if __name__ == "__main__":
    play_game()