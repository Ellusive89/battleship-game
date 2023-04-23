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


def print_board(player_board, computer_board, player_name):
    """Prints the game board with the player's name."""
    print(f"\n== {player_name}'s Board ==")
    print("  A B C D E F G H")
    for i in range(BOARD_SIZE):
        row = [str(i+1)]
        for j in range(BOARD_SIZE):
            row.append(player_board[i][j])
        print(f"{'|'.join(row)}|")

    print("\nComputer's Board")
    print("  A B C D E F G H")
    for i in range(BOARD_SIZE):
        row = [str(i+1)]
        for j in range(BOARD_SIZE):
            if computer_board[i][j] == "X" or computer_board[i][j] == "O":
                row.append(computer_board[i][j])
            else:
                row.append(" ")
        print(f"{'|'.join(row)}|")


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


def get_guess():
    while True:
        guess = input("\nEnter your guess (e.g. A1): ").upper()
        if len(guess) != 2 or guess[0] not in LETT_TO_NUM or not guess[1].isdigit() or int(guess[1]) not in range(1, BOARD_SIZE + 1):
            print("Invalid guess. Please try again.")
        else:
            return LETT_TO_NUM[guess[0]], int(guess[1]) - 1


def computer_guess(player_board, hit_locations):
    if hit_locations:
        x, y = random.choice(hit_locations)
        hit_locations.remove((x, y))
    else:
        x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
        while player_board[y][x] in ["X", "O"]:
            x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
    return x, y


def check_ship_sunk(board, ship_symbol, ship_count):
    for row in board:
        if ship_symbol in row:
            return False, ship_count
    print(f"Ship {ship_symbol} has been sunk!")
    ship_count -= 1
    return True, ship_count


def play_game():
    player_board = create_empty_board()
    computer_board = create_empty_board()
    place_ships(player_board)
    place_ships(computer_board)
    player_name = get_player_name()
    num_hits = 0
    computer_hit_locations = []

    player_ship_count = len(SHIP_SIZE)
    computer_ship_count = len(SHIP_SIZE)

    while True:
        print_board(player_board, computer_board, player_name)
        x, y = get_guess()

        if computer_board[y][x] != " ":
            print("Hit!")
            ship_symbol = computer_board[y][x]
            computer_board[y][x] = "X"
            sunk, player_ship_count = check_ship_sunk(computer_board, ship_symbol, player_ship_count)

            if sunk and player_ship_count == 0:
                print_board(player_board, computer_board, player_name)
                print(f"Congratulations, {player_name}! You won in {num_hits} hits.")
                break
        else:
            print("Miss.")
            computer_board[y][x] = "O"

        print("Computer's turn...")
        x, y = computer_guess(player_board, computer_hit_locations)
        if player_board[y][x] != " ":
            print("Computer hit!")
            ship_symbol = player_board[y][x]
            player_board[y][x] = "X"
            sunk, computer_ship_count = check_ship_sunk(player_board, ship_symbol, computer_ship_count)

            if sunk and computer_ship_count == 0:
                print_board(player_board, computer_board, player_name)
                print(f"Sorry, {player_name}. The computer won!")
                break
        else:
            print("Computer miss.")
            player_board[y][x] = "O"

        num_hits += 1

        if all(cell == "X" or cell == " " for row in computer_board for cell in row):
            print_board(player_board, computer_board, player_name)
            print(f"Congratulations, {player_name}! You won in {num_hits} hits.")
            break
        elif computer_ship_count == 0:
            print_board(player_board, computer_board, player_name)
            print(f"Congratulations, {player_name}! You won in {num_hits} hits.")
            break
        elif player_ship_count == 0:
            print_board(player_board, computer_board, player_name)
            print(f"Sorry, {player_name}. The computer won!")
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
