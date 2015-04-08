#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     starts a roulette game with the user
#
# Author:      Dan
#
# Created:     25.03.2015
# Copyright:   (c) Dan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#purpose of main.py:
#main.py imports the classes RouletteTable and Player and starts the roulette-game.

from roulettetable import RouletteTable
from player import Player

#start the roulette game by calling .starting_playing() method on RouletteTable object. 
RouletteTable().starting_playing()
