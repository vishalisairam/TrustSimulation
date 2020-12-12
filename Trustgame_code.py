#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 11:47:39 2020

@author: riamodh
"""
import random


def transpose(seqseq): #simple 2-dimensional transpose
    """Return transpose of `seqseq`."""
    return zip(*seqseq)


class SimpleGame:
    def __init__(self, player1,  player2, payoffmat):
        # initialize instance attributes
        self.players = [ player1, player2 ]
        self.payoffmat = payoffmat
        self.history = list()
    def run(self, game_iter=5):
        # unpack the two players
        player1, player2 = self.players
        # each iteration, get new moves and append these to history
        for iteration in range(game_iter):
            newmoves = player1.move(self), player2.move(self)
            self.history.append(newmoves)
        # prompt players to record the game played (i.e., 'self')
        player1.record(self)
    def payoff(self):
        # unpack the two players
        player1, player2 = self.players
        # generate a payoff pair for each game iteration
        payoffs = (self.payoffmat[m1][m2] for (m1,m2) in self.history)
        # transpose to get a payoff sequence for each player
        pay1, pay2 = transpose(payoffs)
        # return a mapping of each player to its mean payoff
        return { player1:sum(pay1), player2:sum(pay2) }


class SimplePlayer:
    def __init__(self, playertype):
        self.playertype = playertype
        self.reset()
    def reset(self):
        self.games_played = list()   #empty list
        self.players_played = list()  #empty list
    def move(self,game):
        # delegate move to playertype
        return self.playertype.move(self, game)
    def record(self, game):
        self.games_played.append(game)
        opponent = game.opponents[self]
        self.players_played.append(opponent)
   
class HumanPlayer(SimplePlayer):
    def __init__(self, playerhuman):
        self.playertype = playerhuman
        self.reset()
    def reset(self):
        self.games_played = list()
        self.players_played = list()
    def move(self,game):
        #delegate moveto CDI playertype
        return self.playertype.strat(self,game)
    


class CDIPlayerType:
    def __init__(self, p_cdi=(0.5,0.5,0.5)):
        self.p_cdi = p_cdi
    def move(self, player, game):
        # get opponent and learn her last move
        opponent = game.opponents[player]
        last_move = game.get_last_move(opponent)
        # respond to opponent's last move
        if last_move is None:
            p_defect = self.p_cdi[-1]
        else:
            p_defect = self.p_cdi[last_move]
        return random.uniform(0,1) < p_defect
    def strat(self, human, game):
        answer = input("What is your response?: ")
        if answer == 0:
            p_cdi = 0.0
        elif answer == 1:
            p_cdi = 1.0
        else:
            print(" Please enter a correct respose")
        return random.uniform(0,1)
 
    
class CDIGame(SimpleGame):
    def __init__(self, player1, player2, payoffmat):
        # begin initialization with `__init__` from `SimpleGame`
        SimpleGame.__init__(self, player1, player2, payoffmat)
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


## GAME: CDIGame with SimplePlayer
# create a payoff matrix and two players (with playertypes)
PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
ptype1 = CDIPlayerType((1.0,1.0,1.0))
ptype2 = CDIPlayerType((0.5, 0.0,0.5))
player1 = SimplePlayer(ptype1)
player2 = HumanPlayer(ptype2)
# create and run the game
game = CDIGame(player1, player2, PAYOFFMAT)
game.run()
# retrieve and print the payoffs
payoffs = game.payoff()
print ("Player1 payoff: ", payoffs[player1])
print ("Player2 payoff: ", payoffs[player2])