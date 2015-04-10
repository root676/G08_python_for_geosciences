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
import os
from player import Player

class RouletteTable:
    """ the table class - persons can bet and win/lose money"""
    def __init__(self):
        """
        constructor-function for the RouletteTable-object
        stores the roulette number resulting from a wheel turn, 
        the player-object that plays is on the table, money the player-object brought to the table
        
        returns
        -------
        RouletteTable: object
            returns the RouletteTable-object with initial attributes set
            according to constructor function
        """
        self.roulette_number = None
        self.playerOnTable = None
        self.moneyOnTable = 0

    def starting_playing(self):
        """
        method that starts the game and calls further methods
        """
        playername = raw_input("\n \n" \
            "                  Welcome to                    \n" \
            "    ______                    _             __  \n" \
            "   / _ __/__  _________ ___  (_)___  ____ _/ /  \n" \
            "    / / / _ \/ ___/ __ `__ \/ / __ \/ __ `/ /   \n" \
            "   / / /  __/ /  / / / / / / / / / / /_/ / /    \n" \
            "  /_/  \___/_/  /_/ /_/ /_/_/_/ /_/\__,_/_/     \n" \
            "      ____              __     __  __           \n" \
            "     / __ \____  __  __/ /__  / /_/ /____       \n" \
            "    / /_/ / __ \/ / / / / _ \/ __/ __/ _ \      \n" \
            "   / _, _/ /_/ / /_/ / /  __/ /_/ /_/ __/       \n" \
            "  /_/ |_|\____/\__,_/_/\___/\__/\__/\___/       \n" \
            "                                                \n" \
            "                                                \n" \
            "Terminal Roulette allows you to play French Roulette \n" \
            "from the comfort of your favorite terminal.\n \n" \
            "Please enter your name: ")
        # if name contains numbers, then the player will be asked if it's really his name - if not then the name can be changed
        while any(c.isdigit() for c in playername):
            answer = raw_input("Is "+playername+" really your name? (y/n)").lower()
            if answer in ['yes','y','ja']:
                break
            elif answer not in ['no','n','nein']:
                print('This is not a valid answer. Please enter your real name y/n.')
            else:
                playername = raw_input("So, what is your name?")


        # set up the description for the user
        introduction = ("\n\nWelcome to Terminal Roulette," + playername + "\n\n" \
        "How does French Roulette work?\n" \
        "At the beginning you decide how much money you want to bring to the \n" \
        "Roulette Table. The you can choose between 6 different types of bet, \n" \
        "and then select the amount of money you want to place. You can place as \n" \
        "many bets as you like, als long as you have the money. After you \n" \
        "finished betting, the virtual croupier will spin the roulette wheel to \n" \
        "determine the winning number and color.                              \n\n" \
        "                                                           Good Luck! \n\n")

        # asking the player how much money he wants to set and check if it's more then zero - if not ask again
        while True:
            playersmoney = raw_input(introduction+"How much money do want to bring to the table? ")
            try:
                playersmoney = int(playersmoney)
                if playersmoney > 0:
                    break
            except ValueError:
                print("Please enter a number greater than 0!")

        # save player object into the roulettetabel object
        self.playerOnTable = Player(playername,playersmoney)

        # starting the betting phase through method of the object
        self.betting_phase()
        self.rotate_roulette()
        self.payout_phase()

        # check if player has money left to bet
        if self.playerOnTable.getmoneystatus() == 0:
            print('Sorry - You have no money left to bet.')
            self.stop_playing()

        # asking player if he wants to play again + check if input is valid
        while True:
            answer = raw_input("Do you want to play another round? (y/n) ").lower()
            if answer in ['no','n','nein']:
                self.stop_playing()
            elif answer not in ['yes','y','ja']:
                print('Not valid answer. Please give y/yes or n/no ')
            else:
                self.nextround()
                self.betting_phase()

    def betting_phase(self):
        """
        method starting the betting-phase: the player can choose on which numbers/colors he wants
        to bet, and specifies the amount of money he wants to place on these bets
        """
        # the user can set up several bets (as much as he wants)
        while True:
            # choosing the option
            while True:
                mainoption = raw_input("\nChoose an option you want to bet on. (use the number between the parenthesis)\n" \
                "The numbers in [ ] represent the payout of each bet.\n"
                "   (1) 'Straight' or 'Single'        : bet on a single number [35 to 1]\n" \
                "   (2) 'Manque' or 'Passe'           : bet on the first 18 {1-18} or second 18 {19-36} numbers. [1 to 1]\n" \
                "   (3) 'Rouge ou Noir' (Red or Black): bet on which color the roulette wheel will show. [1 to 1]\n" \
                "   (4) 'Pair ou Impair' (Even or odd): bet on even or odd numbers (without 0). [1 to 1]\n" \
                "   (5) 'Dozen Bets'                  : bet on the first dozen {1-12}, second dozen {13-24} or third dozen {25-36} numbers. [2 to 1]\n" \
                "   (6) 'Column Bets'                 : bet on one of the three vertical lines e.g.: 1-4-7-10 . . . [2 to 1]\n\n" \
                "   (7) Stop playing\n")

                try:
                    mainoption = int(mainoption)
                    if mainoption < 1 or mainoption > 7:
                        raise ValueError
                except ValueError:
                    print("\nThis is not a valid number! Please try it again.")
                    continue

                while True:
                    # if the user gives a invalid input then he gets an message and can try it again
                    try:

                        # ask player on which number or group of numbers he wants to bet
                        if mainoption==1:
                            # ask for the number betwen 0 and 36
                            option = int(raw_input("You are betting on a single number.\n" \
                                    "Choose a number between 0 and 36: "))
                            if option < 0 or option >36:
                                raise ValueError
                        elif mainoption==2:
                            option = int(raw_input('Your are betting on the first 18 or second 18 numbers:' \
                                  'Please decide on which set you want to bet (use the number between the parenthesis):\n'\
                                  '   (1) Manque - first 18 {1-18}\n' \
                                  '   (2) Passe - second 18 {19-26}'))
                            if option < 0 or option >2:
                                raise ValueError
                        elif mainoption==3:
                            option = raw_input("Your are betting on 'red' or 'black'. \n" \
                                    "Please decide on which you want to bet (red/black): ").lower()
                            if not option in ['red','black']:
                                raise ValueError
                        elif mainoption==4:
                            option = raw_input("Your are betting on 'even' or 'odd'.  \n" \
                                    "Please decide on which you want to bet (even/odd): ").lower()
                            if not option in ['even','odd']:
                                raise ValueError
                        elif mainoption==5:
                            option = int(raw_input("You betting on dozens.  \n" \
                                    "Please decide on which set of 12 numbers you want to bet (use the number between the parenthesis):\n" \
                                    "   (1) first dozen {1-12}\n" \
                                    "   (2) second dozen {13-24}\n" \
                                    "   (3) third dozen {25-36}\n"))
                            if option <1 or option >3:
                                raise ValueError
                        elif mainoption==6:
                            option = int(raw_input("You are betting on columns. \n" \
                                    "Please decide on which column you want to bet (use the number between the parenthesis):\n" \
                                    "   (1) first column {1,4,7,10,13,16,19,22,25,28,31,34}\n" \
                                    "   (2) second column {2,5,8,11,14,17,20,23,26,29,32,35}\n" \
                                    "   (3) third column {3,6,9,12,15,18,21,24,27,30,33,36}\n"))
                            if option <1 or option >3:
                                raise ValueError
                        elif mainoption==7:
                            self.stop_playing()
                        break
                    except ValueError:
                        "This is not a valid input! Please try again."

                while True:
                    try:
                        money = float(raw_input("How much money do want to bet?: "))
                        if money <=0:
                            raise ValueError
                    except ValueError:
                        "This is not a valid number! Please enter a number greater than 0."
                        continue

                    # take money from player
                    status = self.playerOnTable.loses(money)
                    if status == True:
                        break
                    print('You have only {} Euro left. Please bet less money.'.format(self.playerOnTable.getmoneystatus()))

                # save the amount of money which is left on the table
                self.addmoney2table(money)

                # save/log the bets
                self.playerOnTable.bets(mainoption, option, money)

                # check if player has money left to bet
                if self.playerOnTable.getmoneystatus() == 0:
                    print('You have no money left to bet. Starting Roulette...')
                    return

                # ask if user wants to bet on another option + check if input valid
                while True:
                    answer = raw_input("To you want to bet on another option? (y/n): ").lower()
                    if answer in ['no','n','nein']:
                        print('Starting Roulette...')
                        return
                    elif answer in ['yes','y','ja']:
                        break
                    else:
                        print('This is not valid answer. You have to answer either y/yes or n/no')

    def rotate_roulette(self):
        """
        method that rotates the roulette and returns a number between 0 and 36
        
        returns
        -------
        roulette_number: int
            winning number for the roulette game
        """
        self.roulette_number = random.randint(0, 36)
        print("\nThe roulette stopped at number {} ({}) !".format(self.roulette_number,self.getcolor()))

    def getcolor(self):
        """
        method that determines whether the resulting number has red, black or no color (in case of 0)
        
        returns
        -------
        string
            string stating the color
        """
        if self.roulette_number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
            return 'red'
        elif self.roulette_number == 0:
            return 'No color [Zero]'
        else:
            return 'black'

    def checkeven(self):
        """
        method that checks if the resulting number is even or odd
        
        returns
        -------
        string
            string stating even / odd / ''
        """
        if self.roulette_number == 0:
            return ''
        elif self.roulette_number % 2 > 0:
            return 'odd'
        else:
            return 'even'

    def addmoney2table(self,money):
        """
        method that adds the money brought to the table by the player-object.
        
        Parameters
        ----------
        money: float
            money brought by player
            
        returns
        -------
        moneyOnTable: float
            money at table for betting
        """
        self.moneyOnTable += money

    def takemoneyfromtable(self,money):
        """
        method that subtracts money from the table
        
        Parameters
        ----------
        money: float
            money to be subtracted from the table
            
        returns
        -------
        moneyOnTable: float
            money currently available for bets on the table
        """
        self.moneyOnTable -= money

    # this phase goes through all wins and loses
    def payout_phase(self):
        """
        method that calculates the money paid out by the table through
        checking the players set betoptions against the drawn number. 
        """
        won_money = 0
        mainoptions = self.playerOnTable.getbetoptions()
        for mainoption in mainoptions:
            if mainoption == 1:
                option = self.roulette_number
            if mainoption == 2:
                option = 1 if self.roulette_number < 18 else 2
            if mainoption == 3:
                option = self.getcolor()
            if mainoption == 4:
                option = self.checkeven()
            if mainoption == 5:
                if self.roulette_number > 12:
                    if self.roulette_number > 24:
                        option = 3
                    else:
                        option = 2
                else:
                    option = 1
            if mainoption == 6:
                if self.roulette_number in [1,4,7,10,13,16,19,22,25,28,31,34]:
                    option = 1
                elif self.roulette_number in [2,5,8,11,14,17,20,23,26,29,32,35]:
                    option = 2
                elif self.roulette_number in [3,6,9,12,15,18,21,24,27,30,33,36]:
                    option = 3

            money = self.playerOnTable.getbettedmoney(mainoption, option)

            if money is not None:
                won_money += self.playerOnTable.wins(self.winning_quote(mainoption)*money)
                self.takemoneyfromtable(money)

        self.playerOnTable.loses(self.moneyOnTable)
        print("You won {} Euro and lost {} Euro!\nYou now have {} Euro in total.\n".format(won_money,self.moneyOnTable,self.playerOnTable.getmoneystatus()))



    def winning_quote(self, mainoption):
        """
        method that gives back the winning quote for a specific bet-option
        
        Parameters
        ----------
        mainoption: int
            primary bet specification
            
        returns
        -------
        int
            multiplicator for the input money that will paid out
        """
        return [36,2,2,2,2,3,3][mainoption-1]

    def nextround(self):
        """
        method that cleans the table and commandline for another round
        deletes saved number and color of the number stored in table-attributes
        """
        self.roulette_number = None
        self.moneyOnTable = 0
        os.system('cls' if os.name == 'nt' else 'clear')

    def stop_playing(self):
        """
        method that stops the program and gives the status of the players-object money.
        """
        print('You are leaving the Roulette table with {} Euro.'.format(self.playerOnTable.getmoneystatus()))
        exit()
