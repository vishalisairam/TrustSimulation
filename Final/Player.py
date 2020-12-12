#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 11:02:12 2020

@author: riamodh
"""

import random

class Player:
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
    
    
    class CDIPlayerType:
        def __init__(self, p_cdi=(0.5,0.5,0.5),character = False):
            """
            Parameters
            ----------
            p_cdi : 
                DESCRIPTION. The default is (0.5,0.5,0.5). This is the probability of defecting given that the other player has defected/cooperated/on the initial move. 
            character : 
                DESCRIPTION. This specifies the playertype of the player.
    
            """
            self.p_cdi = p_cdi
            self.character = character
        def __str__(self):
            """
            Character: Returns playertype during the game
    
            """
       
            return self.character
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
     