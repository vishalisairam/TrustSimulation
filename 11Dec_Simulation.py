#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:38:58 2020

@author: vishali
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:08:01 2020

@author: vishali
"""

import random
import numpy as np
import matplotlib.pyplot as plt

#totalturns = int(input("Please enter a number of turns."))
totalturns = 1
numberturns = 1


def transpose(seqseq): #simple 2-dimensional transpose
    """Return transpose of `seqseq`."""
    return zip(*seqseq)

# Simple Game

class SimpleGame:
    def __init__(self, player1, player2, payoffmat):
        # initialize instance attributes
        self.players = [ player1, player2]
        self.payoffmat = payoffmat
        self.history = list()
    def run(self, game_iter=5):
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
        self.p_cdi = p_cdi
        self.character = character
    def __str__(self):
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
    
player_list = []



def random_pairs_of(players):
    """Return all of players as random pairs."""
    # copy player list
    players = player_list
    # shuffle the new player list in place
    random.shuffle(players)
    # yield the shuffled players, 2 at a time
    player_iter = iter(players)
    return zip(player_iter, player_iter)


def random_pair(players):
    for i in players:
        players = player_list
        newlist = []
        random.sample(players,2)
        player_iter = iter(players)
        player_iter_2 = next(iter(players))
        return zip(player_iter,player_iter_2)

            
class GamePlayer(SimplePlayer):
    def evolve(self):
        self.playertype = self.next_playertype
    def type(self):
        character_list = []
        character_list.append(self.playertype)
        print(character_list)
    def get_payoff(self):
        return sum( game.payoff()[self] for game in self.games_played )
    def get_type(self):
        return (self.playertype for game in self.games_played)
    def choose_next_type(self):
        self.next_playertype = random.shuffle(player_list), random.shuffle(player_list)


playercoop = CDIPlayerType((0.2,0.3,0.5), "Cooperator")
playerdefect = CDIPlayerType((0.5,0.8,1.0), "Defector")
playerrandom = CDIPlayerType((0.1,0.2,0.6), "Random")
playergrudger = CDIPlayerType((0.2,0.8,0.5), "Grudger")
playertft = CDIPlayerType((0.0,1.0,0.5), "Tit for Tat")


sp_playercoop = GamePlayer(playercoop)
sp_playercoop.playertype == "Cooperator"
sp_playerdefect = GamePlayer(playerdefect)
sp_playerdefect.playertype == "Defector"
sp_playerrandom = GamePlayer(playerrandom)
sp_playerrandom.playertype == "Random"
sp_playergrud = GamePlayer(playergrudger)
sp_playergrud.playertype == "Grudger"
sp_playertft = GamePlayer(playertft)
sp_playertft.playertype == "Tit for Tat"


perc_coop = 2
perc_defect = 2
perc_random = 2
perc_grudger = 2
perc_tft = 2

list_coop = list(range(1,(perc_coop*10+ 1)))
list_defect = list(range(1,(perc_defect*10+1)))
list_random = list(range(1,(perc_random*10+1)))
list_grudger = list(range(1,(perc_grudger*10+1)))
list_tft = list(range(1,(perc_tft*10+1)))


player_list = []

len(player_list)


for  i in list_coop:
    sp_playercoop_i = GamePlayer(playercoop)
    player_list.append(sp_playercoop_i)
    sp_playercoop_i.playertype == "Cooperator"
for  i in list_defect:
    sp_playerdefect_i = GamePlayer(playerdefect)
    player_list.append(sp_playerdefect_i)  
    sp_playerdefect_i.playertype == "Defector"
for  i in list_random:
    sp_playerrandom_i = GamePlayer(playerrandom)
    player_list.append(sp_playerrandom_i)
    sp_playerrandom_i.playertype == "Random"
for  i in list_grudger:
    sp_playergrud_i = GamePlayer(playergrudger)
    player_list.append(sp_playergrud_i)
    sp_playergrud_i.playertype == "Grudger"
for  i in list_tft:
    sp_playertft_i = GamePlayer(playertft)
    player_list.append(sp_playertft_i)
    sp_playertft_i.playertype == "Tit for Tat"


len(player_list)        
     

PAYOFFMAT = [ [(3,3),(0,5)],[(5,0),(1,1)] ]  



totalturns = 2



listoftotalturns = list(range(0,totalturns))

for i in listoftotalturns: 
    
    player1dict = {}
    player2dict = {}
    
    global listscorecoop
    global coop_score
    listscorecoop = []
    coop_score = 0
    
    
    global listscoredef
    global def_score
    listscoredef = []
    def_score = 0
    
    
    
    global listscorerandom
    global random_score
    listscorerandom = []
    random_score = 0
    
    
    global listscoretft
    global tft_score
    listscoretft = []
    tft_score = 0
    
    
    
    global listscoregrud
    global grud_score
    listscoregrud = []
    grud_score = 0
    
    
    for player1, player2 in random_pairs_of(player_list):
        print("This is a new game")
        game = CDIGame(player1, player2, PAYOFFMAT)
        game.run()
        payoffs = game.payoff()
        
        player1dict[player1.playertype] = (payoffs[player1])
        player2dict[player2.playertype] = (payoffs[player2])
        print ("Player1 payoff: ", (payoffs[player1]))
        print ("Player2 payoff: ", (payoffs[player2]))
        print("This player is a", player1.playertype)
        print("This player is a", player2.playertype)
        
        if str(player1.playertype) == "Cooperator":
            listscorecoop.append(payoffs[player1])
        elif str(player2.playertype) == "Cooperator":
            listscorecoop.append(payoffs[player2])
        for ele in range(0, len(listscorecoop)):
            coop_score = coop_score + listscorecoop[ele]
            
        if str(player1.playertype) == "Defector":
            listscoredef.append(payoffs[player1])
        elif str(player2.playertype) == "Defector":
            listscoredef.append(payoffs[player2])
        for ele in range(0, len(listscoredef)):
            def_score = def_score + listscoredef[ele]
            
        if str(player1.playertype) == "Random":
            listscorerandom.append(payoffs[player1])
        elif str(player2.playertype) == "Random":
            listscorerandom.append(payoffs[player2])
        for ele in range(0, len(listscorerandom)):
            random_score = random_score + listscorerandom[ele]
            
            
        if str(player1.playertype) == "Tit for Tat":
            listscoretft.append(payoffs[player1])
        elif str(player2.playertype) == "Tit for Tat":
            listscoretft.append(payoffs[player2])
        for ele in range(0, len(listscoretft)):
            tft_score = tft_score + listscoretft[ele]
        
            
        if str(player1.playertype) == "Grudger":
            listscoregrud.append(payoffs[player1])
        elif str(player2.playertype) == "Grudger":
            listscoregrud.append(payoffs[player2])
        for ele in range(0, len(listscoregrud)):
            grud_score = grud_score + listscoregrud[ele]
            



print(coop_score)
print(def_score)
print(random_score)
print(tft_score)
print(grud_score)

t = [coop_score, def_score, random_score, tft_score, grud_score]
t_pos = [i for i, _ in enumerate(t)]

plt.bar(t_pos, t, color='green')
plt.xlabel("Payoff")
plt.ylabel("Players")
plt.title("Payoffs across Players")
plt.show()



         

