# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:15:04 2022

@author: hbori
"""

import pygame

import arithmatics_class
from objects import Player, WIDTH, HEIGHT

# import objects
FPS = 30  # frames per second

BLACK = (0, 0, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

### bg

background = pygame.image.load("bg.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
bg_rect = background.get_rect()

### sprites
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# all_signs = pygame.sprite.Group()
# sign = arithmatics_class.Arithmatics("plus", 100, 300, "plus.png")

#all_signs.add(sign)

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

    # all_signs.draw(screen)
    pygame.display.flip()

    #testtttting
    
pygame.quit()

