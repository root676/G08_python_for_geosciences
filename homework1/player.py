#-------------------------------------------------------------------------------
# Name:        Player
# Purpose:     saves the data like money, name of the player an his bets for
#              playing Roulette
#
# Author:      Stefan Fnord, Clemens Raffler, Daniel Zamojski
#
# Created:     25.03.2015
# Copyright:   (c) Stefan Fnord, Clemens Raffler, Daniel Zamojski 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# purpose of player.py
# player.py contains code for the construction of a player-class
# a player can play on the roulette table and win or lose money

class Player:

    # definition of player properties (name, money he brings, bets he sets on the table)
    def __init__(self,playername,money_set):
        """
        constructor-function of the player-object
        stores username, money brought to table and betted options to player-object

        Paramters
        ---------
        playername: string
            input username
        money_set: int
            input amount of money

        Returns
        -------
        Player: object
            player-object which stores username,
            money brought to table and betted options
        """
        self.name=playername
        self.money=money_set
        self.bet={}

    # save the bets for the specific user
    def bets(self,mainoption,option,money):
        """
        method for storing information about bets, made at
        the RouletteTable-object to the bet-attribute of the player-object

        Paramters
        ---------
        mainoption: int
            primary bet specification
        option: int
            secondary bet specification
        money: float
            money betted on specified options

        returns
        -------
        self.bet: dict
            nested dict containing all specified bet-options
            and betted amount of money following this
            dict-pattern {mainoption:{option:money}}
        """
        bet_mainoptions = self.bet.get(mainoption)
        # if main-option does not exists, create it otherwise...
        if bet_mainoptions == None:
            self.bet[mainoption] = {option:money}
        else:
            # check if options (for specific main options) exists - if yes update otherwise create
            currentmoney = bet_mainoptions.get(option)
            if currentmoney == None:
                bet_mainoptions[option] = money
                self.bet[mainoption] = bet_mainoptions
            else:
                self.bet[mainoption] = {option:currentmoney+money}

    # give back all main bet options which are set
    def getbetoptions(self):
        """
        method that lists the dicts with infomration about
        made bets, stored in the player-object

        returns
        -------
        list
            list containing the betted options
        """
        return self.bet.keys()

    def getbettedmoney(self,mainoption,option):
        """
        method that returns the amount of money, bettet on a specific option.

        Parameters
        ----------
        mainoption: int
            primary bet specification
        option: int
            secondary bet specification

        returns
        -------
        float
            money betted by the on options
        """
        return self.bet[mainoption].get(option)

    def wins(self,money):
        """
        adds the money that was won through bets from the players budget

        Parameters
        ----------
        money: float
            won money paid out by the RouletteTable

        returns
        -------
        money: float
            return total amount of money owned by player
        """
        #print('You have won {} Euro'.format(money))
        self.money += money
        return money

    #  take money from players money
    def loses(self,money):
        """
        subtracts the money that was lost through bets from the players budget

        Parameters
        ----------
        money: float
            money lost through bets on the RouletteTable

        returns
        -------
        False if money lost through bet is greater than the players
        budget, else returns True
        money: float 
            returns the total amount of money owned by player
        """
        if money > self.money:
            return False
        self.money -= money
        return True

    # give back the money status
    def getmoneystatus(self):
        """
        returns the current budget of the player
        
        returns:
        --------
        money: float
            current budget of the player-object
        """
        return self.money

    # erase all bets for a new game
    def cleanupbets(self):
        """
        erases all information about bets stored in the bet dict
        """
        self.bet = {}

