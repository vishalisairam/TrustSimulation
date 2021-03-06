#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:30:00 2020

@author: riamodh
"""

import random
import numpy as np
import matplotlib as mp

# inputs for later

#coop_perc = int(input("Please enter a number: "))
#defec_perc = int(input("Please enter a number: "))
#antigrud_perc = int(input("Please enter a number: "))
#grud_perc = int(input("Please enter a number: "))
#titfortat_perc = int(input("Please enter a number: "))

numberturns = int(input("Please enter a number of turns "))

# initial variables

def transpose(seqseq): #simple 2-dimensional transpose
    """Return transpose of `seqseq`."""
    return zip(*seqseq)


# Games

# Simple Game

class SimpleGame:
    def __init__(self, player1, player2, payoffmat):
        """
        

        Parameters
        ----------
        player1 : TYPE
            DESCRIPTION.
        player2 : TYPE
            DESCRIPTION.
        payoffmat : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        # initialize instance attributes
        self.players = [ player1, player2 ]
        self.payoffmat = payoffmat
        self.history = list()
    def run(self, game_iter=5):
        """
        

        Parameters
        ----------
        game_iter : TYPE, optional
            DESCRIPTION. The default is 5.

        Returns
        -------
        None.

        """
        # unpack the two players
        player1, player2 = self.players
        # each iteration, get new moves and append these to history
        game_iter  = numberturns
        for iteration in range(game_iter):
            newmoves = player1.move(self), player2.move(self)
            self.history.append(newmoves)
        # prompt players to record the game played (i.e., 'self')
        player1.record(self); player2.record(self)
    def payoff(self):
        """
        

        Returns
        -------
        dict
            DESCRIPTION.

        """
        # unpack the two players
        player1, player2 = self.players
        # generate a payoff pair for each game iteration
        payoffs = (self.payoffmat[m1][m2] for (m1,m2) in self.history)
        pay1, pay2 = transpose(payoffs)
        return { player1:sum(pay1), player2:sum(pay2) }
        # transpose to get a payoff sequence for each player
       
        # return a mapping of each player to its mean payoff
        
        
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

# Now we define the payoff mat



# Random Player

# class RandomPlayer:
#     def __init__(self, p=0.5):
#         self.p_defect = p
#     def move(self, game):
#         return random.uniform(0,1) < self.p_defect
#     def record(self, game):
#         pass


class SimplePlayer:
    def __init__(self, playertype):
        self.playertype = playertype
        self.reset()
    def reset(self):
        """
        This is actually for the normal player

        Returns
        -------
        it resets the entire thing - their moves and everything

        """
        self.games_played = list()   #empty list
        self.players_played = list()  #empty list
    def move(self,game):
        # delegate move to playertype
        return self.playertype.move(self, game)
    def record(self, game):
        """
        

        Parameters
        ----------
        game : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.games_played.append(game)
        opponent = game.opponents[self]
        self.players_played.append(opponent)
        
        
class CDIPlayerType:
    def __init__(self, p_cdi=(0.5,0.5,0.5)):
        """
        So a CDI Player is actually a type of simple player

        Parameters
        ----------
        p_cdi : TYPE, optional
            DESCRIPTION. The default is (0.5,0.5,0.5).

        Returns
        -------
        None.

        """
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
    
# class HumanPlayer(SimplePlayer):
    
    
    
    
# Now let us instantiate this

PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]


playercoop = CDIPlayerType((0.0,0.0,0,))
playerdefect = CDIPlayerType((1.0,1.0,1.0))
playergrud = CDIPlayerType((0.2,1.0,0.0))
playerantigrud = CDIPlayerType((0.2,1,0.0,1.0))
playertft = CDIPlayerType((0.0,1.0,0.5))
playerrandom = CDIPlayerType((0.5,0.5,0.5))
playerhuman = CDIPlayerType()


sp_playercoop = SimplePlayer(playercoop)
sp_playerdefect = SimplePlayer(playerdefect)
sp_playergrud = SimplePlayer(playergrud)
sp_playerantigrud = SimplePlayer(playerantigrud)
sp_playertft = SimplePlayer(playertft)
sp_playerrandom = SimplePlayer(playerrandom)


# now we create the players

perc_coop = int(input("Enter the percentage of cooperators in this society:  "))
perc_defect = int(input("Enter the percentage of defectors in this society:  "))
perc_grud = int(input("Enter the percentage of gruds in this society:  "))
perc_antigrud = int(input("Enter the percentage of anti gruds in this society:  "))
perc_tft = int(input("Enter the percentage of tit for tats in this society:  "))
perc_random = int(input("Enter the percentage of random player in this society:  "))



list_coop = list(range(1,perc_coop*10))
list_defect = list(range(1,perc_defect*10))
list_grud = list(range(1,perc_grud*10))
list_antigrud = list(range(1,perc_antigrud*10))
list_tft = list(range(1,perc_tft*10))
list_random = list(range(1,perc_random*10))




player_list = []

for  i in list_coop:
    sp_playercoop_i = SimplePlayer(playercoop)
    player_list.append(sp_playercoop_i)
for  i in list_defect:
    sp_playerdefect_i = SimplePlayer(playerdefect)
    player_list.append(sp_playerdefect_i)
for  i in list_grud:
    sp_playergrud_i = SimplePlayer(playergrud)
    player_list.append(sp_playergrud_i)
for  i in list_antigrud:
    sp_playerantigrud_i = SimplePlayer(playerantigrud)
    player_list.append(sp_playerantigrud_i)
for  i in list_tft:
    sp_playertft_i = SimplePlayer(playertft)
    player_list.append(sp_playertft_i)    
for  i in list_random:
    sp_playerrandom_i = SimplePlayer(playerrandom)
    player_list.append(sp_playerrandom_i)

# choose random players from the list

def random_pairs_of(players):
    """Return all of players as random pairs."""
    # copy player list
    players = player_list
    # shuffle the new player list in place
    random.shuffle(players)
    # yield the shuffled players, 2 at a time
    player_iter = iter(players)
    return zip(player_iter, player_iter)



PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
game = CDIGame((random_pairs_of(player_list)), PAYOFFMAT)
# game.run()


class SoupRound:
    def __init__(self, players, payoffmat):
        self.players = player_list
        self.payoffmat = PAYOFFMAT
    def run(self):
        payoff_matrix = self.payoffmat
        soup_player_list = []
        for player1, player2 in random_pairs_of(self.players):
            game = CDIGame(player1, player2, payoff_matrix)
            game.run()
            soup_player_list.append(player1, player2)

                
                
            





























class SoupPlayer(SimplePlayer):
    def evolve(self):
        self.playertype = self.next_playertype
    def get_payoff(self):
        return sum( game.payoff()[self] for game in self.games_played )
    def choose_next_type(self):
        # find the playertype(s) producing the highest score(s)
        best_playertypes = topscore_playertypes(self)
        # choose randomly from these best playertypes
        self.next_playertype = random.choice(best_playertypes)






# assuming you are just choosing from one of the playert







# now we have all the people in the society

def topscore_playertypes(player):
    """Return list of best (maximum payoff) player types."""
    best_types = [player.playertype]
    best_payoff = player.get_payoff()
    for opponent in player.players_played:
        payoff = opponent.get_payoff()
        if payoff > best_payoff:
            best_payoff = payoff
            best_types = [opponent.playertype]
        elif payoff == best_payoff:
            best_types.append(opponent.playertype)
    return best_types

class SoupPlayer(SimplePlayer):
    def evolve(self):
        self.playertype = self.next_playertype
    def get_payoff(self):
        return sum( game.payoff()[self] for game in self.games_played )
    def choose_next_type(self):
        # find the playertype(s) producing the highest score(s)
        best_playertypes = topscore_playertypes(self)
        # choose randomly from these best playertypes
        self.next_playertype = random.choice(best_playertypes)
        
class SoupRound:
    def __init__(self, players, payoffmat):
        self.players = players
        self.payoffmat = payoffmat
    def run(self):
        payoff_matrix = self.payoffmat
        for player1, player2 in random_pairs_of(self.players):
            game = CDIGame(player1, player2, payoff_matrix)
            game.run()

soup_player_list = []
for i in player_list:
    soup_player_i = SoupPlayer(i)
    soup_player_list.append(soup_player_i)
    




# Now we randomize list


# How to run the game?
# create and run the game
# game = CDIGame(player1, player2, PAYOFFMAT)
# game.run()
# # retrieve and print the payoffs
# payoffs = game.payoff()
# print ("Player1 payoff: ", payoffs[player1])
# print ("Player2 payoff: ", payoffs[player2])
    
    
    
# okay now that you have all this. 


