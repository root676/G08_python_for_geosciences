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

    def stop_playing(self):
        if self.money==0:
            print("Excuse me, you have no money left to bet.")
        else:
            print('You are leaving the Roulette table with {} ?.',self.money)
        exit()
