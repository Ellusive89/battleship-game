import random

BOARD_SIZE = 8
SHIP_SIZE = [1, 2, 3, 4, 5, 6]
LETT_TO_NUM = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
SHIP_SYMBOLS = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}


def create_empty_board():
    return [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]


def get_player_name():
    while True:
        player_name = input("Enter your name: ").upper()
        if player_name.isalpha():
            return player_name
        else:
            print("Please enter a name containing only letters.")


def print_board(board, player_name):
    """Prints the game board with the player's name."""
    print(f"\n{player_name}'s Board")
    print("  A B C D E F G H")
    for i in range(BOARD_SIZE):
        row = [str(i + 1)]
        for j in range(BOARD_SIZE):
            row.append(board[i][j])
        print(" ".join(row))


def main():

    print("=== Welcome to Battleship Game! ===")
    create_empty_board()
    player_name = get_player_name()


main()
