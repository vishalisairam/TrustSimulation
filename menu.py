#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:53:35 2020

@author: riamodh
"""

import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum

BLACK = (0,0,0)
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
RED = (250, 75, 75)
bg = pygame.image.load( "Content/Graphics/standoff.jpg" )
bg = pygame.transform.scale(bg, (800,600))


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Copperplate", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    """ An user interface element that can be added to a surface """
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

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    ABOUTPAGE = 2
    SIMULATION = 3

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE
    
    while True:
        if game_state == GameState.TITLE:
           game_state = title_screen(screen)
            
        if game_state == GameState.NEWGAME:
            game_state = play_level(screen)
            
        if game_state == GameState.SIMULATION:
            game_state = simulation(screen)
            
        if game_state == GameState.ABOUTPAGE:
            game_state = about_screen(screen)
            
        if game_state == GameState.QUIT:
            pygame.quit() 
            return

def title_screen(screen):
    welcome_btn = UIElement(
        center_position = (600,100), 
        font_size=35, 
        bg_rgb=None, 
        text_rgb=RED,
        text="Welcome Player!",
        action=None
        )

    start_btn = UIElement(
        center_position=(600, 200),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="Start",
        action=GameState.NEWGAME,
    )
    
    sim_btn = UIElement(
        center_position=(600, 250),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="Simulation",
        action=GameState.SIMULATION,
    )

    about_btn = UIElement(
        center_position=(600,300),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="About",
        action=GameState.ABOUTPAGE,
    )
        
    quit_btn = UIElement(
        center_position=(600, 350),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="Quit",
        action=GameState.QUIT,
    )
    
    buttons = [welcome_btn, start_btn, sim_btn, about_btn, quit_btn]
    
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.blit(bg, [0,0])

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
    
def play_level(screen):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=None,
        text_rgb=BLACK,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.blit(bg, [0,0])

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()   
  

def about_screen(screen):
    information = UIElement( 
        center_position=(600,100),
        font_size=30,
        bg_rgb=None,
        text_rgb=RED,
        text="Based on the theory of the prioners dilemma, this trust game ventures to guage hoe much you trust you opponent/n",
        action=None,
        )
    
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=None,
        text_rgb=BLACK,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    
    buttons = [information, return_btn]
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.blit(bg, [0,0])

        ui_action = buttons.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        buttons.draw(screen)

        pygame.display.flip()  

def simulation(screen):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=None,
        text_rgb=BLACK,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.blit(bg, [0,0])

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()
    
main()