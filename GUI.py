#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 11:40:18 2020

@author: vishali
"""

import PySimpleGUI as sg

sg.ChangeLookAndFeel('GreenTan')

# layout = [[sg.Text("specify number of turns here"), sg.Input()],
#            [sg.Text("Percentage of Cooperators", sg.Slider(range=(1, 10), default_value=2, orientation = "v"))],
#            [sg.Text("Percentage of Defectors",sg.Slider(range=(1, 10), default_value=2, orientation = "v"))],
#            [sg.Text("Percentage of Randomizers", sg.Slider(range=(1, 10), default_value=2, orientation = "v"))],
#            [sg.Text("Percentage of Tit for Tats",sg.Slider(range=(1, 10), default_value=2, orientation = "v"))],
#            [sg.Text("Percentage of Grudgers", sg.Slider(range=(1, 10), default_value=2, orientation = "v"))],
#           [sg.Button("GO")], [sg.Exit()]]


layout = [[sg.Text("specify number of turns here")], [sg.Input(key  = 'turns')],
           [sg.Text("Percentage of Cooperators")], [sg.Input(key = 'coop')],
           [sg.Text("Percentage of Defectors")],[sg.Input(key = 'def')],
           [sg.Text("Percentage of Randomizers")], [sg.Input(key = "random")],
           [sg.Text("Percentage of Tit for Tats")],[sg.Input(key = "tft")],
           [sg.Text("Percentage of Grudger")],[sg.Input(key = "grud")],
          [sg.Button('Ok')], [sg.Exit()]]
          
# Create the window
window = sg.Window('Simulation of Trust', layout)

event,values = window.read()

# while True: 
#     event, values = window.read()
#     print(event, values)
#     if event == 'Exit':
#         break
  
window.close() 

# perc_random = values[3]
# perc_tft = values[4]
# perc_grudger = values[5]


print(event, values)

turns = 0
coop = 0
defector = 0
random = 0
tft = 0
grud = 0

values['turns'] = turns
values['coop'] = coop
values['def'] = defector
values['random'] = random
values['tft'] = tft
values['grud'] = grud