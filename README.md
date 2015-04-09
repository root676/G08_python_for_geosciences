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
real roulette table.


# Requirements

The following is required when handing in the exercise:
* A short (1-3) pages report explaining what the program is doing, its structure and how the functions
and/or modules work together. Somebody reading this document should find it easy to start reading
the source code. No source code in this document. This can also be a simple README text

* Documented python source code.
  After I had a chance to look at the source code I will make appointments with each group to have a short
  (10-15 min) talk about the exercise. Hand in of the exercise will be handled in TUWEL.

# Note:

* Wenn ich den Benutzer meine schreib ich "user", wenn ich "Player" schreibe
    mein ich damit die Klasse Player

## French Terminal Roulette

The French Terminal Roulette programm is implemented through object-orientated 
python-programming and consists of two classes:

### `Player` 
Manages player-specific data. An object of the `Player` class
stores the `Player`'s name, his available money, and the bets that the user
placed. A player can lose `money` (by betting it) and gain `money` (by winning).

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

`betting_phase()` - The betting phase: The user is first asked what type of bet he
wants to place, and then can select the amount of money he wants to bet. He can
repeat this process as often as he likes or until he runs out of money. When
either of this happens the `rotate_roulette()` method selects a random integer
between 0 and 36, and stores this number in the `roulette_number` variable
of the `RouletteTable` class. Next the `payout_phase()` method is called. It
checks the bets saved in `playerOnTable` against the `roulete_number`. Should
the user have betted on a winning option, the `winning_quote()` method calclulates
how much he won, and the corresponding amount is added to `money` of `playerOnTable`.
Finally the `RouletteTable` reset by `nextround()` and the user can choose whether
to play another round, or whether to take his winnings (if any) and leave the game.
