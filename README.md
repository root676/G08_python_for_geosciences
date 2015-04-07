# G08_python_for_geosciences
This repository contains all sourcecode produced during the class 120.050 'Python for geosciences' (ViennaUniversity of Technology)


Folder Structure:

homework1: This folder contains all Scripts for the Commandline Roulette

# Aufgabe

The following is required when handing in the exercise:
 A short (1-3) pages report explaining what the program is doing, its structure and how the functions
and/or modules work together. Somebody reading this document should nd it easy to start reading
the source code. No source code in this document. This can also be a simple README text le.
 Documented python source code.
After I had a chance to look at the source code I will make appointments with each group to have a short
(10-15 min) talk about the exercise. Hand in of the exercise will be handled in TUWEL.

# Report

**Grad noch in sehr gebrochenem englisch, ich formuliers bald gescheit aus**

The programm consists of two classes: RouletteTable for the Roulette Table and Player for a roulette player.

The Player class saves the player name, the money he or she owns and the bets that he placed. A player can win or lose money. 

The RouletteTable class implements the game logic of French roulette. When it is initally called the roulette table asks the user for his name and how much money he wants to bring to the table. It the creates an object of the Player class (*playerOnTable*) with those values. 

After the player is set up, the acutal game begins. It is organiced in two phases:

The betting phase: The player is asked what type of bet he wants to place and then can select the amount of money he wants to bet on that option. He can repeat this process as often as he likes and place as many bets each round as he can afford. 

After he finished betting the roulette is turned (a random integer between 0 and 36 is set). The turning of the roulette marks the transition from the betting phase to the payout phase. 

In the payout phase the players bets are compared against the number of the roulette, and based on this information the player wins and losses are calculated. The money is added to the playerOnTable object.

Finaly the roultte table is reset: The number is set to none again, the money on the table is set to zero and the screen is cleared.

The player can then choose whether to play another round, or if he rather left the game




