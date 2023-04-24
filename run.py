import random
from colorama import Fore, init

BOARD_SIZE = 8
SHIP_SIZE = [1, 2, 3, 4, 5, 6]
LETT_TO_NUM = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
SHIP_SYMBOLS = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}


def create_empty_board():
    """Create an empty board of the specified size."""
    return [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]


def get_player_name():
    """Prompt the user for their name and validate the input."""
    while True:
        player_name = input(Fore.CYAN + "Your name?: " + Fore.RESET).upper()
        if player_name.isalpha():
            return player_name
        else:
            print(Fore.RED + "Please enter only letters." + Fore.RESET)


def print_board(player_board, computer_board, player_name):
    """Display the player and computer game boards."""
    print(f"\n== {player_name}'s Board ==")
    print("  A B C D E F G H")
    for i in range(BOARD_SIZE):
        row = [str(i+1)]
        for j in range(BOARD_SIZE):
            if player_board[i][j] == "X":
                row.append(Fore.RED + player_board[i][j] + Fore.RESET)
            elif player_board[i][j] == "*":
                row.append(Fore.BLUE + player_board[i][j] + Fore.RESET)
            else:
                row.append(player_board[i][j])
        print(f"{'|'.join(row)}|")

    print("\nComputer's Board")
    print("  A B C D E F G H")
    for i in range(BOARD_SIZE):
        row = [str(i+1)]
        for j in range(BOARD_SIZE):
            if computer_board[i][j] == "X":
                row.append(Fore.RED + computer_board[i][j] + Fore.RESET)
            elif computer_board[i][j] == "*":
                row.append(Fore.BLUE + computer_board[i][j] + Fore.RESET)
            else:
                row.append(" ")
        print(f"{'|'.join(row)}|")


def place_ships(board):
    """Place ships randomly on the given board."""
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


def get_guess(previous_guesses):
    """Prompt the user for a guess and validate the input."""
    while True:
        guess = input(Fore.CYAN + "\nGuess (e.g. A1): " + Fore.RESET).upper()
        if (len(guess) != 2 or guess[0] not in LETT_TO_NUM
                or not guess[1].isdigit()
                or int(guess[1]) not in range(1, BOARD_SIZE + 1)):
            print(Fore.YELLOW + "Invalid guess.")
            print("Please try again." + Fore.RESET)
        else:
            x, y = LETT_TO_NUM[guess[0]], int(guess[1]) - 1
            if (x, y) in previous_guesses:
                print(Fore.MAGENTA + "You have already guessed that spot.")
                print(Fore.MAGENTA + "Please try again." + Fore.RESET)
            else:
                previous_guesses.add((x, y))
                return x, y


def computer_guess(player_board, hit_locations):
    """Generate a computer guess based on hit locations."""
    if hit_locations:
        coord = random.choice(hit_locations)
        hit_locations.remove(coord)
        x, y = coord
    else:
        x, y = random_coords()
        while player_board[y][x] in ["X", "*"]:
            x, y = random_coords()
    return x, y


def random_coords():
    """Return a tuple of random row and column indices."""
    return random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)


def check_ship_sunk(board, ship_symbol, ship_count):
    """Check if a ship with the given symbol is sunk on the board."""
    for row in board:
        if ship_symbol in row:
            return False, ship_count
    print(Fore.RED + f"Ship {ship_symbol} has been sunk!" + Fore.RESET)
    ship_count -= 1
    return True, ship_count


def play_game():
    """Run the main game loop."""
    player_board = create_empty_board()
    computer_board = create_empty_board()
    place_ships(player_board)
    place_ships(computer_board)
    player_name = get_player_name()
    num_hits = 0
    computer_hit_locations = []

    previous_guesses = set()

    player_ship_count = len(SHIP_SIZE)
    computer_ship_count = len(SHIP_SIZE)

    while True:
        print_board(player_board, computer_board, player_name)
        x, y = get_guess(previous_guesses)

        if computer_board[y][x] != " ":
            print(Fore.RED + "Hit!" + Fore.RESET)
            ship_symbol = computer_board[y][x]
            computer_board[y][x] = "X"
            sunk, player_ship_count = check_ship_sunk(
                computer_board, ship_symbol, player_ship_count)

            if sunk and player_ship_count == 0:
                print_board(player_board, computer_board, player_name)
                print(Fore.GREEN + f"\nCongratulations, {player_name}!")
                print(Fore.GREEN + f"You won in {num_hits} hits." + Fore.RESET)
                break
        else:
            print(Fore.YELLOW + "Miss." + Fore.RESET)
            computer_board[y][x] = "*"

        print(Fore.CYAN + "Computer's turn..." + Fore.RESET)
        x, y = computer_guess(player_board, computer_hit_locations)
        if player_board[y][x] != " ":
            print(Fore.RED + "Computer hit!" + Fore.RESET)
            ship_symbol = player_board[y][x]
            player_board[y][x] = "X"
            sunk, computer_ship_count = check_ship_sunk(
                player_board, ship_symbol, computer_ship_count)

            if sunk and computer_ship_count == 0:
                print_board(player_board, computer_board, player_name)
                print(Fore.RED + f"\nSorry, {player_name}.")
                print(Fore.RED + "The computer won!" + Fore.RESET)
                break
        else:
            print(Fore.YELLOW + "Computer miss." + Fore.RESET)
            player_board[y][x] = "*"

        num_hits += 1

        if all(cell == "X" or cell == " " for row in computer_board
                for cell in row):
            print_board(player_board, computer_board, player_name)
            print(Fore.GREEN + f"Congratulations, {player_name}!")
            print(Fore.GREEN + f"\nYou won in {num_hits} hits." + Fore.RESET)
            break
        if computer_ship_count == 0:
            print_board(player_board, computer_board, player_name)
            print(Fore.GREEN + f"Congratulations, {player_name}!")
            print(Fore.GREEN + f"\nYou won in {num_hits} hits." + Fore.RESET)
            break
        if player_ship_count == 0:
            print_board(player_board, computer_board, player_name)
            print(Fore.RED + f"Sorry, {player_name}.")
            print(Fore.RED + "The computer won!" + Fore.RESET)
            break


def main():
    """Initialize and run the game."""
    init(autoreset=True)

    print(Fore.CYAN + "=== Welcome to Battleship Game! ===" + Fore.RESET)
    print(Fore.GREEN + "\nInstructions:" + Fore.RESET)
    print("1. The board size is 8x8.")
    print("2. There are 6 ships with sizes ranging from 1 to 6.")
    print("3. To make a guess, enter the row letter and column number.")
    print("   == e.g., A1 ==")
    print("4. A hit will be marked with an 'X' and a miss with an '*'.")
    print("5. The game ends when either you or the computer")
    print("   sinks all the ships.")
    print(Fore.GREEN + "6. Have fun!\n" + Fore.RESET)
    while True:
        play_game()
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "N":
            break
    print(Fore.GREEN + "Thank you for playing Battleship Game!" + Fore.RESET)


main()
