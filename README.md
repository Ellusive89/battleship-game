# Battleship Game!

This is a simple implementation of the classic game Battleship, written in Python. The game is played on an 8x8 board, with 6 ships of different sizes ranging from 1 to 6.

The user plays against the computer, taking turns to guess the location of the opponent's ships. The game ends when either the user or the computer sinks all of the opponent's ships.

![Responsive Mockup](https://github.com/Ellusive89/battleship-game/blob/main/media/am-i-responsive.png)

## Game Elements

### How to play

- __When you run the game, you will be prompted to enter your name. Once you have entered your name, the game will begin.__

- __You will then see two game boards: one for your ships and one for the computer's ships. Your ships will be placed randomly on your board at the start of the game.__

- __To make a guess, enter the row letter and column number of the position you want to guess, e.g., "A1". A hit will be marked with an "X" on the opponent's board, while a miss will be marked with an "*". The computer will then take its turn and guess a location on your board.__

- __The game ends when either you or the computer sinks all of the opponent's ships. At that point, the winner will be announced and you will be given the option to play again.__

- __Good luck and have fun playing Battleship Game!__

### Features

- __The game is played on an 8x8 board, with 6 ships of different sizes ranging from 1 to 6. Game provide instructions how to play.__

![Instructions](https://github.com/Ellusive89/battleship-game/blob/main/media/instructions.png)

- __The user is prompted to enter their name at the start of the game.__

- __The user and the computer each have their own game board, which shows the locations of their ships.__

![User and computer board](https://github.com/Ellusive89/battleship-game/blob/main/media/user-computer-board.png)

- __To make a guess, the user enters the row letter and column number of the position they want to guess, e.g., "A1". A hit will be marked with an "X" on the opponent's board, while a miss will be marked with an "*".__

![Hit and miss](https://github.com/Ellusive89/battleship-game/blob/main/media/hit-and-miss.png)

- __The game will ensure that the input data is valid.__

![Input](https://github.com/Ellusive89/battleship-game/blob/main/media/invali-guess.png)

- __The computer generates its guesses randomly, but will focus its guesses around hit locations to increase the chances of hitting a ship.__

- __The game will supply you with information on the length of a sunken ship.__

![Ship lenght](https://github.com/Ellusive89/battleship-game/blob/main/media/ship3-sunk.png)

![Ship lenght2](https://github.com/Ellusive89/battleship-game/blob/main/media/ship6-sunk.png)

- __The game ends when either the user or the computer sinks all of the opponent's ships.__

- __The winner is announced at the end of the game, and the user is given the option to play again.__

![You Won!](https://github.com/Ellusive89/battleship-game/blob/main/media/you-won.png)

![Play again?](https://github.com/Ellusive89/battleship-game/blob/main/media/play-again.png)

- __If the player decides to exit the game, a message expressing gratitude for playing will be shown. If the player chooses to play again, the game will restart.__

![Play again NO](https://github.com/Ellusive89/battleship-game/blob/main/media/play-again-no.png)

## Implemented Features

- __By importing Colorama, I've incorporated colors into the game, providing users with a more enjoyable and full experience.__

## Features to be Implemented

- __In the future, I intend to incorporate various board sizes and enable players to position their own ships on the board.__

## Bugs

- __Through testing there are no currently known bugs within the game.__

## Testing
I have extensively tested the game to ensure it is functional and responsive.
- __Test user name input to ensure it accepts only valid names (alphabetic characters) and rejects invalid ones.__
- __Ensure ships are placed randomly and do not overlap on the board.__
- __Ensure game only accepts valid guesses (correct format and not previously guessed) and rejects invalid ones.__
- __Ensure that game generates valid guesses based on hit locations.__
- __Ensure that program correctly detects when a ship is sunk and updates the ship count.__
- __Ensure player guesses are reflected correctly on the computer's board and computer guesses are reflected correctly on the player's board.__
- __Ensure ship sunk messages are displayed accurately.__
- __Play through an entire game to verify that the game loop functions correctly, updating the board and tracking hits, misses, and sunk ships as expected.__
- __Test various game scenarios, such as player or computer winning, to ensure the game ends appropriately and displays the correct winner message.__

## Validation

- __This game passes through the Code Institute PEP8 Validator with no errors.__

![Validation](https://github.com/Ellusive89/battleship-game/blob/main/media/python-validator-ci.png)

## Technologies

- __Producing the game required the use of Python, a versatile and powerful programming language.__
- __The 'random' module was used to generate random coordinates for the placement of the ships in the game.__
- __To enhance the visual aesthetics of the game, I have imported the 'colorama' module to add color to the terminal output.__
- __I stored the game's source code and related files in a repository on GitHub, a popular platform for version control and collaboration.__
- __For the coding enviroment I have used Gitpod.__
- __Heroku was used to deploy the game to the web.__

## Deployment

# To deploy the game, I used Heroku CLI. Here are the steps to follow:
- __Create a Heroku account and log in. From the dashboard, click "New" to create a new app.__
- __Choose a unique name for your app and select your region. Click "Create app" to create the app.__
- __Go to "Settings" and navigate to Config Vars. Add a new Config Var with the following key-value pair: KEY = PORT, VALUE = 8000 (this is the only variable needed for this app).__
- __Add buildpacks for Python and NodeJS, in that order.__
- __Click the Deploy tab.__
- __Scroll down to Deployment Method and select GitHub.__
- __Select the repository to be deployed and connect to Heroku.__
- __Scroll down to deploy. There are two options:__
    - __Option 1 is to select Automatic deploys. This will update the app with every "git push". This is the recommended option for this project.__
    - __Option 2 is to select Manual deploy. This requires manually redeploying the app after every change via the Heroku deploy tab.__
- __Here is deployed project: https://battleship-game-ellusive89.herokuapp.com/__

## Credits

- __ULTIMATE Battleships from Code Institute served as a guide and inspiration for this readme, as I utilized similar elements and structure to create a document that would effectively communicate the project's details and objectives.__
- __Code Institute's walkthrough project, love_sandwiches, provided a valuable source of inspiration and learning for the creation of this game.__
- __In developing the Python code, I drew upon the expertise and insights of a variety of resources, including python.org, w3schools, pypi.org and stackoverflow, to ensure optimal functionality and performance.__
- __Code Institiute provided the deployment terminal.__