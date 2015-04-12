#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     starts a roulette game with the user
#
# Authors:     Stefan Fnord, Clemens Raffler, Daniel Zamojski  
#
# Created:     25.03.2015
# Copyright:   (c) Stefan Fnord, Clemens Raffler, Daniel Zamojski 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from roulettetable import RouletteTable
from player import Player

#start the roulette game by calling .starting_playing() method on RouletteTable object. 
RouletteTable().starting_playing()
