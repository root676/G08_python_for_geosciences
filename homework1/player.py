#-------------------------------------------------------------------------------
# Name:        Player
# Purpose:     saves the data like money, name of the player an his bets for
#              playing Roulette
#
# Author:      Dan
#
# Created:     25.03.2015
# Copyright:   (c) Dan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class Player:
    """ Player class - player can play on the roulette table and win or lose money"""

    def __init__(self,playername,money_set):
        self.name=playername
        self.money=money_set
        self.bet={}

    # save the bets for the specific user
    def bets(self,mainoption,option,money):
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
        return self.bet.keys()

    # gives the money for the betted option
    def getbettedmoney(self,mainoption,option):
        return self.bet[mainoption].get(option)

    # add money to players money
    def wins(self,money):
        print('You have won {} Euro',money)
        self.money += money

    #  take money from players money
    def loses(self,money):
        if money > self.money:
            return False
        self.money -= money
        return True

    # give back the money status
    def getmoneystatus(self):
        return self.money

    def cleanupbets(self):
        self.bet = {}

