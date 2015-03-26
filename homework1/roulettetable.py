#-------------------------------------------------------------------------------
# Name:        RouletteTable
# Purpose:     This class allows a player (from class Player) to play Roulette
#
# Author:      Dan
#
# Created:     25.03.2015
# Copyright:   (c) Dan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import random
from player import Player

class RouletteTable:
    """ the table class - persons can bet and win/lose money"""
    def __init__(self):
        roulette_number = None
        playerOnTable = None

    def starting_playing(self):
        playername = raw_input("Welcome Sir/Madame to French Roulette!\nWhat's your name?")
        # if name contains numbers, then the player will be asked if it's really his name - if not then the name can be changed
        while any(c.isdigit() for c in playername):
            if raw_input("Is that correct that your name is "+playername+"?").lower() in ['yes','y','ja']:
                break
            else:
                playername = raw_input("So what's your name Sir/Madame?")

        # asking the player how much money he wants to set and check if it's more then zero - if not ask again
        playersmoney=0
        while playersmoney<=0:
            playersmoney = raw_input("How much money do want to use for the play?")
            try:
                playersmoney = int(playersmoney)
                if playersmoney>0:
                    break
            except ValueError:
                print("Please give a number over 0!")

        # save player object into the roulettetabel object
        self.playerOnTable = Player(playername,playersmoney)

        print('DESCRIPTION/RULES FOR ROULETTE')

        # starting the betting phase through method of the object
        self.betting_phase()

    def betting_phase(self):
        while True:
            raw_input("Choose a ") # ON WORK -daniel
            raw_input("Place your bets!")


    def rotate_roulette(self):
        self.roulette_number=random.randint(0,36)

