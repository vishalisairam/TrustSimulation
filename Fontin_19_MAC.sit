#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 07:34:24 2020

@author: vishali
"""

import random
import numpy as np
import matplotlib.pyplot as plt



def transpose(seqseq): 
    """Return transpose of `seqseq`."""
    return zip(*seqseq)

# Simple Game

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
 
 
# Specifying the probabilities for each playertype
   
playercoop = CDIPlayerType((0.3,0.3,0.3))
playerdef = CDIPlayerType((0.8,0.9,0.9))
playerrandom = CDIPlayerType((0.5,0.5,0.5))
playergrudger = CDIPlayerType((0.4, 0.7, 0.7))
playertft = CDIPlayerType((0.4,0.8,0.7))

# create a new player type

s_coop = SimplePlayer(playercoop)
s_def = SimplePlayer(playerdef)
s_random = SimplePlayer(playerrandom)
s_grudger = SimplePlayer(playergrudger)
s_tft = SimplePlayer(playertft)

player_list = [s_coop, s_def, s_grudger, s_random, s_tft]
    

PAYOFFMAT = [ [(2,2),(0,4)],[(4,0),(1,1)] ]

#totalturns = int(input("Please enter a number of turns."))
totalturns = 3
listoftotalturns = list(range(0,totalturns))


def coop_game():
    """
    CDI Game with Cooperator Playertype and Human Input


    """
    print("You are playing with Player A!")
    coop_score = [] # empty list of all scores by cooperator in this game
    human_score_coop= [] # empty list of all scored scored by human in this game
    for i in listoftotalturns:
        
        int1 = int(input("Please enter 0 to cooperate or 1 to defect: ")) #listing all probabilities of 
        int2 = int1
        int3 = int1
        playerinput = CDIPlayerType((int1,int2,int3))
        s_input = SimplePlayer(playerinput)
        
        game = CDIGame(s_input, s_coop, PAYOFFMAT)
        game.run()
        payoffs = game.payoff()
        
        print ("Player1 payoff: ", payoffs[s_input])
        print ("Player2 payoff: ", payoffs[s_coop])
        
        coop_score.append(payoffs[s_coop])
        human_score_coop.append(payoffs[s_input])
        
    global total_coop
    total_coop = 0
    for ele in range(0, len(coop_score)):
        total_coop = total_coop + coop_score[ele]
        
    global total_human_coop
    total_human_coop = 0
    for ele in range(0, len(human_score_coop)):
        total_human_coop = total_human_coop + human_score_coop[ele]
    
    print("The total payoffs earned by the computer player is: ", total_coop)
    print("The total payoffs earned by the you is: ", total_human_coop) 


def def_game():
    print("You are playing with Player B!")
    def_score = []
    human_score_def= [] 
    
    for i in listoftotalturns:
        int1 = int(input("Please enter 0 to cooperate or 1 to defect: "))
        int2 = int1
        int3 = int1
        playerinput = CDIPlayerType((int1,int2,int3))
        s_input = SimplePlayer(playerinput)
        
        
        game = CDIGame(s_input, s_def, PAYOFFMAT)
        game.run()
        payoffs = game.payoff()
        print ("Player1 payoff: ", payoffs[s_input])
        print ("Player2 payoff: ", payoffs[s_def])
        
        def_score.append(payoffs[s_def])
        human_score_def.append(payoffs[s_input])
        
    global total_def    
    total_def = 0
    for ele in range(0, len(def_score)):
        total_def = total_def + def_score[ele]
        
    global total_human_def
    total_human_def = 0
    for ele in range(0, len(human_score_def)):
        total_human_def = total_human_def + human_score_def[ele]
    
    print("The total payoffs earned by the computer player is: ", total_def)
    print("The total payoffs earned by the you is: ", total_human_def) 
        

       
def random_game():
    print("You are playing with Player C!")
    random_score = []
    human_score_random= [] 
    
    for i in listoftotalturns:
        int1 = int(input("Please enter 0 to cooperate or 1 to defect: "))
        int2 = int1
        int3 = int1
        playerinput = CDIPlayerType((int1,int2,int3))
        s_input = SimplePlayer(playerinput)
        
        game = CDIGame(s_input, s_random, PAYOFFMAT)
        game.run()
        payoffs = game.payoff()
        print ("Player1 payoff: ", payoffs[s_input])
        print ("Player2 payoff: ", payoffs[s_random])
        
        random_score.append(payoffs[s_random])
        human_score_random.append(payoffs[s_input])
        
    global total_random
    total_random = 0
    for ele in range(0, len(random_score)):
        total_random = total_random + random_score[ele]
        
    global total_human_random
    total_human_random = 0
    for ele in range(0, len(human_score_random)):
        total_human_random = total_human_random + human_score_random[ele]
    
    print("The total payoffs earned by the computer player is: ", total_random)
    print("The total payoffs earned by the you is: ", total_human_random) 
     


def tft_game():
    print("You are playing with Player D!")
    tft_score = []
    human_score_tft= [] 
    
    for i in listoftotalturns:
        int1 = int(input("Please enter 0 to cooperate or 1 to defect: "))
        int2 = int1
        int3 = int1
        playerinput = CDIPlayerType((int1,int2,int3))
        s_input = SimplePlayer(playerinput)
        
        game = CDIGame(s_input, s_tft, PAYOFFMAT)
        game.run()
        payoffs = game.payoff()
        print ("Player1 payoff: ", payoffs[s_input])
        print ("Player2 payoff: ", payoffs[s_tft])
        
        tft_score.append(payoffs[s_tft])
        human_score_tft.append(payoffs[s_input])
        
    global total_tft    
    total_tft = 0
    for ele in range(0, len(tft_score)):
        total_tft = total_tft + tft_score[ele]
    
    global total_human_tft
    total_human_tft = 0
    for ele in range(0, len(human_score_tft)):
        total_human_tft = total_human_tft + human_score_tft[ele]
    
    print("The total payoffs earned by the computer player is: ", total_tft)
    print("The total payoffs earned by the you is: ", total_human_tft)
                
def grud_game():
    print("You are playing with Player E!")
    grud_score = []
    human_score_grud= [] 
    
    for i in listoftotalturns:
        int1 = int(input("Please enter 0 to cooperate or 1 to defect: "))
        int2 = int1
        int3 = int1
        playerinput = CDIPlayerType((int1,int2,int3))
        s_input = SimplePlayer(playerinput)

        game = CDIGame(s_input, s_grudger, PAYOFFMAT)
        game.run()
        payoffs = game.payoff()
        print ("Player1 payoff: ", payoffs[s_input])
        print ("Player2 payoff: ", payoffs[s_grudger])
        
        
        grud_score.append(payoffs[s_grudger])
        human_score_grud.append(payoffs[s_input])
        
    global total_grud
    total_grud = 0
    for ele in range(0, len(grud_score)):
        total_grud = total_grud + grud_score[ele]
        
 
    global total_human_grud 
    total_human_grud = 0
    for ele in range(0, len(human_score_grud)):
        total_human_grud = total_human_grud + human_score_grud[ele]
    
    print("The total payoffs earned by the computer player is: ", total_grud)
    print("The total payoffs earned by the you is: ", total_human_grud)
    


# def run_functions_in_random_order(funcs):
#     funcs = function_list
#     function_list = [coop_game(), def_game(), random_game(), tft_game(), grud_game()]
#     random.shuffle(funcs)
#     for func in function_list:
#         func()
#         break

listoffuncs =[coop_game(), def_game(), random_game(), tft_game(), grud_game()]
#run_functions_in_random_order(listoffuncs)

# def run(funcs): 
#     functions_game = [coop_game(), def_game(), random_game(), tft_game(), grud_game()] 
#     random.shuffle(functions_game)
#     for func in random.shuffle(functions_game):
#         func

# run(functions_game)

# Final Resul

print(total_grud)

print("In the game against Cooperator player, you scored", total_coop, "while the Cooperator scored", total_human_coop)
print("In the game against Defector player, you scored", total_def, "while the Defector scored", total_human_def)
print("In the game against Random player, you scored", total_random, "while the Random scored", total_human_random)
print("In the game against Tit for Tat player, you scored", total_tft, "while the Tit for Tat scored", total_human_tft)
print("In the game against Grudger player, you scored", total_grud, "while the Grudger scored", total_human_grud)