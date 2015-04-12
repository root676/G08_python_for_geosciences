# G08_python_for_geosciences
This repository contains all sourcecode produced during the class 120.050 'Python for geosciences' (Vienna University of Technology)


Folder Structure:
homework1: This folder contains all Scripts for the Commandline Roulette
      main.py
      palyer.py
      roulettetable.py


# Whats the task of the first assignment?

The aim is to test our knowledge in python by implementing
French Roulette as a terminal application. The user can bet an arbitrary
amount of money on different betting options, and win or loose money depending
on the outcome of the roulette. As this is a only an exercise, 
not all betting options of real-life French Roulette are implemented.


## French Terminal Roulette

The French Terminal Roulette programm can be started with the `main.py` file. 
The program is implemented through object-orientated 
python-programming, which makes the code more readable and easier
to debug by splitting the code base into short, easy to understand methods.
The program ensures stability through frequent checks to catch input errors made by the user. 
Should an input error be detected, the program does not shut down, but gives the user
the opportunity to correct his input. This improves the usability. 
The game consists of two basic classes:

### `Player` 
Manages player-specific data. An object of the `Player` class
stores the `Player`'s name, his available money he brought to the table, and the bets
that the user placed in the current round. A player can lose `money` (by betting it) 
and gain `money` (by winning).

### `RouletteTable`
Implements the user interface as well as the business
logic of the roulette game. It can store the `roulette_number` (the number selected
after the roulette wheel is turned), the betted money that
is on the table (`moneyOnTable`) at any current phase of the game, and the `Player`.
When `RouletteTable` is called it asks the
user for the Player name and how much money he wants to bring to the table.
It then saves those values to a newly created object of the `Player` class
called `playerOnTable`.

After this inital introduction phase the actual roulette game begins,
represented by four methods:

`betting_phase()` - The betting phase: The user can choose between 6 main betting 
options which will split into detailed betting options when one of them is selected.
Too many options on the first page would be overwhelming for the player. 
He is allowed to set several bets with different amount of money until he has
no money left to bet. If it's the case the user will be informes as well as he tries to
bet more money than he has. He can repeat this betting process as often as he likes 
or until he runs out of money. When either of this happens the `rotate_roulette()` method
selects a random integer between 0 and 36, and stores this number in the 
`roulette_number` variable of the `RouletteTable` class. Next the `payout_phase()` method 
is called. It checks the bets saved in `playerOnTable` against the `roulete_number`. 
Should the user have betted on a winning option, the `winning_quote()` method gives back the 
winning quote for the further calclulation of how much he won. The corresponding amount can be added 
to `money` of `playerOnTable`. Finally the `RouletteTable` resets by `nextround()` which means it
deletes saved roulette number of the current round, the betted money on the table and clears the
terminal window. In addition the program offers the user the choice whether
to play another round, or whether to take his winnings (if any) and leave the game.
If the player has no money for playing another round then he will be informed and game ends.
