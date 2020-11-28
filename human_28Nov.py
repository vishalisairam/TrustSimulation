#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:45:07 2020

@author: riamodh
"""
import random

def transpose(seqseq): #simple 2-dimensional transpose
    """Return transpose of `seqseq`."""
    return zip(*seqseq)


class RandomMover:
    def move(self):
        return random.uniform(0,1) < 0.5

## GAME: RandomMover
# create a payoff matrix and two players
PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
player1 = RandomMover()
player2 = RandomMover()
# get a move from each player
move1 = player1.move()
move2 = player2.move()
# retrieve and print the payoffs
pay1, pay2 = PAYOFFMAT[move1][move2]

print("Player1 payoff: ", pay1)
print("Player2 payoff: ", pay2)

class humanmover:
    def strat(self):
        move = input("Select a move: 1 or 0")
        if move == 1:
            print("You chose to cooperate")
        elif move == 0:
            print("You chose to defelect")



class SimpleGame:
    def __init__(self, player1,  human, payoffmat):
        # initialize instance attributes
        self.players = [ player1, human ]
        self.payoffmat = payoffmat
        self.history = list()
    def run(self, game_iter=5):
        # unpack the two players
        player1, human = self.players
        # each iteration, get new moves and append these to history
        for iteration in range(game_iter):
            newmoves = player1.move(self), human.strat(self)
            self.history.append(newmoves)
        # prompt players to record the game played (i.e., 'self')
        player1.record(self); human.record(self)
    def payoff(self):
        # unpack the two players
        player1, player2 = self.players
        # generate a payoff pair for each game iteration
        payoffs = (self.payoffmat[m1][m2] for (m1,m2) in self.history)
        # transpose to get a payoff sequence for each player
        pay1, pay2 = transpose(payoffs)
        # return a mapping of each player to its mean payoff
        return { player1:sum(pay1), player2:sum(pay2) }
    
## GAME: RandomMover
# create a payoff matrix and two players
PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
player1 = RandomMover()
human = humanmover()
# get a move from each player
move1 = player1.move()
move2 = human.strat()
# retrieve and print the payoffs
pay1, pay2 = PAYOFFMAT[move1][move2]