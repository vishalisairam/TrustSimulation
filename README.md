# TrustSimulation

Comments for submission (Please look at the 'Final' Folder)

A. We had planned three components to our project:
- The Interactive Game with human input
- A Simulation
- A GUI for presentation

B. We completed the game and simulation as programs and we also have a basic structure for the GUI (Pygame GUI for the Game and tkinter GUI for Simulation)

C. However, we struggled with merging the final game and simulation codes with the respective GUI codes. The Human Input for both the Game and Simulation work in the console but not with the GUI. 
- In the Game, '0' is Cooperate and '1' is defect. 

---------------------------------------------------------------------------------------------------------------------------------------------------------------





Python Blueprint

Game Blueprint

**Class 1: Game**

While loop: exit

Attributes:

1. actions (RSPT)
2. Points for each

R = 2

S = -1

T = 3

P = 0

Class Game:

def __init__(self,points, r: points=2, s: points= -1, t: points=3, p: points=0)

Self.__points = { (C,C) : (r,r), (D, D): (p,p), (C,D): (s,t), (D,C): (t,s)}

def score(self, pair: Tuple[Action, Action]) -\&gt; Tuple[Score, Score]:

"""Returns the appropriate score for a decision pair.

Parameters

----------

pair: tuple(Action, Action)

A pair actions for two players, for example (C, C).

Returns

-------

tuple of int or float

Scores for two player resulting from their actions.

"""

return self.scores[pair]

***Class 2: Strategy***

Def __init__(self, other = false, strategy):

Self.strategy = C, D

Self.other = other

Def strategy(self):

def D(self):

print(score)

self.history.append()

def C(self):

print(score)

self.history.append()

Comp = strategy()

***Class 3: Player***

Attributes: History, Score,

Methods:

Def __init__(self, historySelf, historyOther, score, compStrategy, otherStrategy):

Self.score = score

Self.historySelf = []

Self.historyOther = []

Self.compStrategy = []

Self.otherStrategy = otherStrategy

# Combine Actions and Score into dictionary

Def score(self):

Def historySelf(self):

Def historyOther(self):

Def compStrategy(self):

  classCopycat(Player):

  "Player mimics move""

  name = "Copycat"

  def strategy(self,other):

  #first move

  if len(self.history) == 0:

  return C

  elif other.history[-1]== D:

  return D

  else:

  return C

  class Cooperator(Player):

  "Player cooperates"

  name = "Cooperator"

  def strategy(self, opponent):

  if len(self.history) == 0:

  return C

  else:

  return C

  class Cheater(Player):

  "Player cheats"

  name = "Cheater""

  def strategy(self,opponent):

  if len(self.history) == 0:

  return D

  else:

  return D

  class Grudger(Player):

  "Player cooperates until opponent cheats"

  name = "Grudger""

  def strategy(self,opponent):

  if len(self.history) == 0:

  return D

  if opponent.history[-1] = C:

  return C

  else:

  return D

  class Reformer(Player):

  "Player cheats until opponent cooperates"

  name = "Reformer""


def strategy(self,opponent):

if len(self.history) == 0:

return C

if opponent.history[-1] = D:

return D

else:

return C

Def otherStrategy(self):

Input = input(&quot;C or D&quot;)

While input ! C or D:

Ask again.

If c:

Append.Otherhistory[]

Print(Score)

If d:

Append.Otherhistory[]


***Class 4: Match***

Class Match:

Def__init__()

Listofcompstrat = [cooperator, copycat, cheater, grudger, reformer]

Game = [random.sample(listofcompstrat), otherstrategy)]
