#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:20:54 2020

@author: riamodh
"""
# 1 - Import libraries
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from enum import Enum
from pygame.sprite import RenderUpdates


# 2 - Importing graphics and font
RED = (250, 75, 75)
BLACK = (0,0,0)
player = pygame.image.load("Content/Graphics/dude.png")
war = pygame.image.load("Content/Graphics/war.png")

#3 - Making a surface that will accept text input
def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Copperplate", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

#4 - Defining what the text will look like and how it would respond to the mouse
class nextMove(Sprite):
    "A user interface element being added to the game screen"
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
        """
        # calls the init method of the parent sprite class
        super().__init__()
        
        self.mouse_over = False  # indicates if the mouse is over the element

        # create the default image
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]
        
        self.action = action
        
    # properties that vary the image and its rect when the mouse is over the element
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
        
    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect) 
        
#5 - Defining the elements on the screen
class GameState(Enum):
    Quit = -1
    Title = 0
    Start = 1
    Aboutpage = 2
    Simulation = 3

#6 - Initialising pygame
def main():
    pygame.init()
    width, height = 640, 480
    screen=pygame.display.set_mode((width, height))
    game_state = GameState.Title
    
    while True:
        if game_state == GameState.Title:
            game_state = title_screen(screen)

        if game_state == GameState.Start:
            game_state = start(screen)
        
        if game_state == GameState.Aboutpage:
            game_state = about_screen(screen)

        if game_state == GameState.Quit:
            pygame.quit()
            return

# Making a function for the while loop executing pygame to avoid repetition
def game_loop(screen, buttons):
    """ Handles game loop until an action is return by a button in the
    buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.blit(war, (0,0))        
        screen.blit(player, (100,300))
        screen.blit(player, (440,300))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            buttons.draw(screen)
       
        pygame.display.flip()

# Defining elements and actions on the main menu
def title_screen(screen):
    welcome_btn = nextMove(
        center_position = (300,100), 
        font_size=35, 
        bg_rgb=None, 
        text_rgb=RED,
        text="Welcome Player!",
        action=None
        )

    start_btn = nextMove(
        center_position=(300, 200),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="Start",
        action=GameState.Start,
    )
    
    sim_btn = nextMove(
        center_position = (300,250),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="Simulation",
        action=None,
        )
    
    about_btn = nextMove(
        center_position=(300,300),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="About",
        action=GameState.Aboutpage,
    )
        
    quit_btn = nextMove(
        center_position=(300, 350),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="Quit",
        action=GameState.Quit,
    )
    
    buttons = RenderUpdates(welcome_btn, start_btn, sim_btn, about_btn, quit_btn)
    
    return game_loop(screen, buttons)

# defining elements and actions once the game starts
def start(screen):
    shoot_btn = nextMove(
        center_position = (200,100), 
        font_size=35, 
        bg_rgb=None, 
        text_rgb=RED,
        text="Shoot",
        action=None,
        )

    hide_btn = nextMove(
        center_position=(440, 100),
        font_size=35,
        bg_rgb=None,
        text_rgb=RED,
        text="Ignore",
        action=None,
    )

    quit_btn = nextMove(
        center_position = (550,450),
        font_size=25,
        bg_rgb=None,
        text_rgb=RED,
        text="Quit",
        action=GameState.Quit)
    
    return_btn = nextMove(
        center_position=(125, 450),
        font_size=20,
        bg_rgb=None,
        text_rgb=RED,
        text="Return to main menu",
        action=GameState.Title,
    )
    
    buttons = RenderUpdates(shoot_btn, hide_btn, quit_btn, return_btn)
    
    return game_loop(screen,buttons)

# defining elements on the about page
def about_screen(screen):
    return_btn = nextMove(
        center_position=(300, 400),
        font_size=20,
        bg_rgb=None,
        text_rgb=RED,
        text="Return to main menu",
        action=GameState.Title,
    )
    
    info = nextMove(
        center_position = (300,50),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="Here is how the game goes:",
        action=None,
        )
    
    info2 = nextMove(
        center_position = (300,100),
        font_size = 22,
        bg_rgb=None,
        text_rgb=RED,
        text="You are armed and you see an armed opponent",
        action=None,
        )
    
    info3 = nextMove(
        center_position= (300,150),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="Will you shoot or not?",
        action=None,
        )
    
    info4 = nextMove(
        center_position= (300,200),
        font_size=15,
        bg_rgb=None,
        text_rgb=BLACK,
        text="Both shoot = 1 point",
        action=None,
        )
    
    info5 = nextMove(
        center_position= (300,225),
        font_size=15,
        bg_rgb=None,
        text_rgb=BLACK,
        text="Both ignore = 2 points",
        action=None,
        )
    
    info6 = nextMove(
        center_position= (300,250),
        font_size=15,
        bg_rgb=None,
        text_rgb=BLACK,
        text="Only you shoot = 4 points",
        action=None,
        )
    
    info7 = nextMove(
        center_position= (300,275),
        font_size=15,
        bg_rgb=None,
        text_rgb=RED,
        text="Only you ignore = -1 points",
        action=None,
        )
    

    buttons = RenderUpdates(return_btn, info, info2, info3, info4, info5, info6, info7)
    
    return game_loop(screen, buttons)

#Running the completed function
main()


