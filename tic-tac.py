def print_tic_tac_toe_board(board):
    """
    Prints a 3x3 Tic-Tac-Toe board.

    Args:
        board: A list of 9 elements representing the board. 
               Each element can be a number (1-9) for empty spaces,
               or 'X'/'O' for player symbols.
    """
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")

if __name__ == "__main__":
    # Example 1: Board with numbers (initial state)
    initial_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Initial Tic-Tac-Toe Board:")
    print_tic_tac_toe_board(initial_board)

    # Example 2: Board with player symbols
    game_board = ['X', 2, 'O', 4, 'X', 6, 'O', 8, 'X']
    print("\nTic-Tac-Toe Board with Player Symbols:")
    print_tic_tac_toe_board(game_board)

    # Example 3: Another board with player symbols
    another_board = ['X', 'O', 'X', 'O', 'X', 'O', 7, 8, 9]
    print("\nAnother Tic-Tac-Toe Board:")
    print_tic_tac_toe_board(another_board)