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
        roulette_number_color = None
        playerOnTable = None

    def starting_playing(self):
        playername = raw_input("Welcome Sir/Madame to the French Terminal Roulette!\n" \
        "What's your name?\n")
        # if name contains numbers, then the player will be asked if it's really his name - if not then the name can be changed
        while any(c.isdigit() for c in playername):
            if raw_input("Is that correct that your name is "+playername+"?").lower() in ['yes','y','ja']:
                break
            else:
                playername = raw_input("So what's your name Sir/Madame?")


        # set up the description for the user
        introduction =  "How works French Terminal Roulette?\n" \
        "At the beginning you can set the amount of money which you want to take to the Roulette Table.\n" \
        "In the betting phase you can choose different options on which you can bet with a specific amount\n" \
        "of money you have to define. But you can bet on several options.Afer the betting phase the Roulette\n" \
        "will be rotated and the determined number decides if you win or lose money.\n\n"

        # asking the player how much money he wants to set and check if it's more then zero - if not ask again
        playersmoney=0
        while playersmoney<=0:
            playersmoney = raw_input(introduction+"How much money do want to use for the play?")
            try:
                playersmoney = int(playersmoney)
                if playersmoney>0:
                    break
            except ValueError:
                print("Please give a number over 0!")

        # save player object into the roulettetabel object
        self.playerOnTable = Player(playername,playersmoney)

        # starting the betting phase through method of the object
        self.betting_phase()



    # starting the betting phase: the player can choose the option and bet a specific amount of money
    def betting_phase(self):

        # the user can set up several bets (as much as he wants)
        while True:
            # choosing the option
            while True:
                betting_option = raw_input("Choose a option you want to bet on. (use the number between the parenthesis)\n" \
                "   (1) 'Straight' or 'Single' a bet on a single number [35 to 1]\n" \
                "   (2) 1 to 18 or 'Manque' a bet on one of thefirst 18 numbers. [1 to 1]\n" \
                "   (3) 19 to 36 or 'Passe' a bet on the high 18 numbers. [1 to 1]\n" \
                "   (4) Red or Black or 'Rouge ou Noir' a bet on which color the roulette wheel will show. [1 to 1]\n" \
                "   (5) Even or odd 'Pair ou Impair' a bet on even or odd nonzero number. [1 to 1]\n" \
                "   (6) Dozen Bets a bet on the first 12 {1-12}, second 12 {13-24} or third 12 {25-36} numbers. [2 to 1]\n" \
                "   (7) Column Bets a bet on one of the three vertical lines e.g.: 1-4-7-10 . . . [2 to 1]\n" \
                "The numbers in [ ] represent the payout of each bet.")

                try:
                    betting_option = int(betting_option)
                    break
                except ValueError:
                    print("\nThis not a valid number! Please try it again.")

                while True:
                    # if the user gives a invalid input then he gets an message and can try it again
                    try:

                        # ask player on which number or group of numbers he wants to bet
                        if betting_option==1:
                            # ask for the number betwen 0 and 36
                            value = int(raw_input("You are betting on a single number.\n" \
                                    "Give a number between 0 and 36 you want to bet on: "))
                            if value < 0 or value >36:
                                raise ValueError
                        elif betting_option==2:
                            print('Your are betting on the first 18 numbers: 1 to 18')
                        elif betting_option==3:
                            print('Your are betting on the second 18 numbers: 19 to 36')
                        elif betting_option==4:
                            value = raw_input("Your are betting on 'red' or 'black'" \
                                    "Please decide on which you want to bet (red/black): ").lower()
                            if not any(value in ['red','black']):
                                raise ValueError
                        elif betting_option==5:
                            value = raw_input("Your are betting on 'even' or 'odd'" \
                                    "Please decide on which you want to bet (even/odd): ").lower()
                            if not any(value in ['even','odd']):
                                raise ValueError



                        break
                    except ValueError:
                        "This is not a valid input! Please try it again."








            # save/log the bets
            self.playerOnTable.bets({option_id,money})



            raw_input("Place your bets!")
            if raw_input("Do you want to bet on another option?").lower() in ['no','n','nein']:
                break






    def rotate_roulette(self):
        self.roulette_number=random.randint(0,36)
        self.getcolor(self.roulette_number)

    # get color of the Roulette number
    def getcolor(self):
        if any(self.roulette_number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]):
            self.roulette_number_color = 'red'
        elif self.roulette_number == 0:
            self.roulette_number_color = 'None'
        else:
            self.roulette_number_color = 'black'

    # delete saved number and color of the number  (not really necessary but 'cleaner'/more similar to Roulette)
    def nextround(self):
        self.roulette_number_color = None
        self.roulette_number = None

"""
    def stop_playing(self):
        if self.money==0:
            print("Excuse me, you have no money left to bet.")
        else:
            print('You are leaving the Roulette table with {} ?.',self.money)
        exit()

"""
