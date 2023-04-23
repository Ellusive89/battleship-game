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


def place_ships(board):
    for size in SHIP_SIZE:
        while True:
            orientation = random.choice(["horizontal", "vertical"])
            if orientation == "horizontal":
                x = random.randint(0, BOARD_SIZE - size)
                y = random.randint(0, BOARD_SIZE - 1)
                if all(board[y][x + i] == " " for i in range(size)):
                    for i in range(size):
                        board[y][x + i] = SHIP_SYMBOLS[size]
                    break
            else:
                x = random.randint(0, BOARD_SIZE - 1)
                y = random.randint(0, BOARD_SIZE - size)
                if all(board[y + i][x] == " " for i in range(size)):
                    for i in range(size):
                        board[y + i][x] = SHIP_SYMBOLS[size]
                    break


def play_game():
    board = create_empty_board()
    place_ships(board)
    player_name = get_player_name()
    while True:
        print_board(board, player_name)
        break


def main():

    print("=== Welcome to Battleship Game! ===")
    while True:
        play_game()
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "N":
            break
    print("Thank you for playing Battleship Game!")


main()
