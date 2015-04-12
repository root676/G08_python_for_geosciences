# G08_python_for_geosciences
This repository contains all sourcecode produced during the class 120.050 'Python for geosciences' (ViennaUniversity of Technology)


Folder Structure:
homework1: This folder contains all Scripts for the Commandline Roulette
      main.py
      palyer.py
      roulettetable.py


# Whats the task of the first assignment?

The aim is to test our knowledge in python by programming
a terminal roulette. These means that the user should be asked
by the programm on what the user wants to bet and wich amount of 
money he wants to set. The betting options are the same like at a
real roulette table, but with fewer input-options to lower the 
level of complexity.


# Requirements

The following is required when handing in the exercise:
* A short (1-3) pages report explaining what the program is doing, its structure and how the functions
and/or modules work together. Somebody reading this document should find it easy to start reading
the source code. No source code in this document. This can also be a simple README text

* Documented python source code.
  After I had a chance to look at the source code I will make appointments with each group to have a short
  (10-15 min) talk about the exercise. Hand in of the exercise will be handled in TUWEL.

## French Terminal Roulette

The French Terminal Roulette programm can be started with the `main.py` file. 
The program is implemented through object-orientated 
python-programming, which makes the code easier to unterstand
and allows a fast error detection considering the small code-length of methods.
The whole program ensures stability through a lot of checks to catch all the 
input errors made by the user. The program should shut down if the user types in 
something wrong, so there is always the possibility to give the specific input again.
This should improve the usability. The game consists of two basic classes:

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
