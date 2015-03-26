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
    def bets(self,playersbet):  #TODO: noch ?berlegungsfehler drinnen (zweimal auf dieselbe Zahl wetten/setzen?)
        self.bet.append(playersbet)

    # add money to players money
    def wins(self,money):
        print('You have won {} ?',money)
        self.money += money

    #  take money from players money
    def loses(self,money):
        print('You have lost {} ?',money)
        self.money -= money


