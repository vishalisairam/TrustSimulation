#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:52:04 2020

@author: riamodh
"""

import random
import numpy as np
import matplotlib.pyplot as plt



def transpose(seqseq): 
    """Return transpose of `seqseq`."""
    return zip(*seqseq)

# Simple Game

class Game:
    class SimpleGame:  
        def __init__(self, player1, player2, payoffmat):
            # initialize instance attributes
            self.players = [ player1, player2 ]
            self.payoffmat = payoffmat
            self.history = list()
        def run(self, game_iter=1):
            # unpack the two players
            player1, player2 = self.players
            # each iteration, get new moves and append these to history
            # here we choose each iteration to be 1
            game_iter  = 1
            for iteration in range(game_iter):
                newmoves = player1.move(self), player2.move(self)
                self.history.append(newmoves)
            # prompt players to record the game played (i.e., 'self')
            player1.record(self); player2.record(self)
        def payoff(self):
            # unpack the two players
            player1, player2 = self.players
            # generate a payoff pair for each game iteration
            payoffs = (self.payoffmat[m1][m2] for (m1,m2) in self.history)
            pay1, pay2 = transpose(payoffs)
            return { player1:sum(pay1), player2:sum(pay2) }
        
    class CDIGame(SimpleGame):
        def __init__(self, player1, player2, payoffmat):
            # begin initialization with `__init__` from `SimpleGame`
            Game.SimpleGame.__init__(self, player1, player2, payoffmat)
            # initialize the new data attribute
            self.opponents = {player1:player2, player2:player1}
        def get_last_move(self, player):
            # if history not empty, return prior move of `player`
            if self.history:
                player_idx = self.players.index(player)
                last_move = self.history[-1][player_idx]
            else:
                last_move = None
            return last_move