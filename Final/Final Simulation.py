#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 07:35:16 2020

@author: vishali
"""
import random
from Game import Game
from SimplePlayer import SimplePlayer
from CDIPlayerType import CDIPlayerType
import numpy as np
import matplotlib.pyplot as plt

def random_pairs_of(players):
    """Return random pairs of all players."""
    # copy player list
    players = player_list
    # shuffle the new player list in place
    random.shuffle(players)
    # yield the shuffled players, 2 at a time
    player_iter = iter(players)
    return zip(player_iter, player_iter)

  

# Define game player to evolve and choose next playertype randomly
          
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



# Define each playertype

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



# get input for percentage of each player 

print(""" Please enter the proportion of each playertype between 0-100 (e.g. 20)
      
  Hint: Choose an equal number of people in each playertype and then replay the game with small sucessive tweaks to see how points across plaeyrtypes / total points change.
       
      """)

perc_coop = int(input("Enter the proportion of Cooperators: "))
perc_defect = int(input("Enter the proportion of Defectors: "))
perc_random = int(input("Enter the proportion of Random: "))
perc_grudger = int(input("Enter the proportion of Grudger: "))
perc_tft = int(input("Enter the proportion of Tit for Tat: "))


list_coop = list(range(1,(perc_coop*10+ 1)))
list_defect = list(range(1,(perc_defect*10+1)))
list_random = list(range(1,(perc_random*10+1)))
list_grudger = list(range(1,(perc_grudger*10+1)))
list_tft = list(range(1,(perc_tft*10+1)))


# create player list with the input

player_list = []




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
     
print ("\n The total number of playertypes in this society is", len(player_list), "of which there are", len(list_coop), " Cooperators, ", len(list_defect), " Defectors, ", len(list_random), " Random Players, ", len(list_tft), " Tit for tats, ", len(list_grudger), " Grudgers")


print (""" \n \n This is the payoff matrix: 
       
       
  PAYOFFMAT = [ [(2,2),(-1,4)],[(4,-1),(1,1)] ]  


Both cheat: 1 each
Both do not cheat: 2 each
One cheats while the other does not cheat: 4 to player who cheats, -1 to player to does not cheat


"""     
       )

PAYOFFMAT = [ [(2,2),(-1,4)],[(4,-1),(1,1)] ]  

print("\n Now please enter the number of rounds in the simulation. A new round will create new random pairs of players and allow them to play with each other ")

totalturns = int(input("Enter the number of turns: "))

listoftotalturns = list(range(0,totalturns))

for i in listoftotalturns: 

    # create empty variables for lists and scores
    
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
        game = Game.CDIGame(player1, player2, PAYOFFMAT)
        game.run()
        payoffs = game.payoff()


        # show payoffs and playertype for each player in game
        
        print ("Player1 payoff: ", (payoffs[player1]))
        print ("Player2 payoff: ", (payoffs[player2]))
        print("This player is a", player1.playertype)
        print("This player is a", player2.playertype)
        
        #  create llists for each player, append and add scores if belonging to specific playertype
        
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
            


# print scores

s = coop_score +  def_score + random_score + tft_score + grud_score
tshare = [coop_score/s, def_score/s, random_score/s, tft_score/s, grud_score/s]


print("Across", len(player_list), "and ", totalturns, " the payoffs earned by each playertype (total and share of total) is: \n")

print("Cooperator: total - ", coop_score, "and share -", round(coop_score/s, 2))
print("Defender: total - ", def_score, "and share -", round(def_score/s,2) )
print("Random:", random_score, "and share -", round(random_score/s,2))
print("Tit for Tat:", tft_score, "and share -", round(tft_score/s,2))
print("Grudger:", grud_score, "and share -", round(grud_score/s,2))

print("\n Check the graph above.")

print("\n \n Total Payoff derived by society across", len(player_list), " players and across ", totalturns, "is", s )

# Mapping the scores to playertypes using a Barplot

# Plot 1 : Payoffs across Players
t = [coop_score, def_score, random_score, tft_score, grud_score]
t_pos = ['Cooperator', 'Defender', 'Random', 'Tit for Tat', 'Grudger']

plt.bar(t_pos, t, color='green')
plt.xlabel("Payoff")
plt.ylabel("Players")
plt.title("Payoffs across Players")
plt.show()

# Plot 2

tshare_pos = ['Cooperator', 'Defender', 'Random', 'Tit for Tat', 'Grudger']

plt.bar(tshare_pos, tshare, color='red')
plt.xlabel(" Share of Payoffs")
plt.ylabel("Players")
plt.title("Share of Payoffs across Players")
plt.show()
         

