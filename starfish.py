# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:15:04 2022

@author: hbori
"""

import pygame
import objects

WIDTH = 500  # width of our game window
HEIGHT = 500 # height of our game window
FPS = 30 # frames per second

BLACK = (0, 0, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

### bg

background = pygame.image.load('bg.jpg')
bg_rect = background.get_rect()

### sprites

all_sprites = pygame.sprite.Group()

player = objects.Player()
all_sprites.add(player)

# Game Loop
running = True
while running:
    
    clock.tick(FPS)
    
    ######## Process input (events)
    
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False    
    
    ######## Update
    
    all_sprites.update()
    
    ######## Render (draw)
    
    screen.fill(BLACK)
    screen.blit(background, bg_rect)
    all_sprites.draw(screen)
    
    pygame.display.flip()
    
pygame.quit()