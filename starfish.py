# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:15:04 2022

@author: hbori
"""

#from curses.textpad import rectangle
import pygame
import random

import arithmatics_class, numbers_class
from objects import Player, WIDTH, HEIGHT

# import objects
FPS = 30  # frames per second

BLACK = (0, 0, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
pygame.mixer.music.load("game_music.mp3")
pygame.mixer.music.play(-1)

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

all_signs = pygame.sprite.Group()
sign_plus = arithmatics_class.Arithmatics("+", 100, 650, "plus.png")
all_signs.add(sign_plus)
sign_sub = arithmatics_class.Arithmatics("-", 200, 650, "minus.png")
all_signs.add(sign_sub)

numbers = pygame.sprite.Group()
def create_number(n):
    
    for i in range(n):
        number = numbers_class.numbers()
        all_sprites.add(number)
        numbers.add(number)
        
create_number(5)

### 

goal_num = random.randrange(3, 50)

# Game Loop
running = True
while running:

    clock.tick(FPS)

    ######## Process input (events)

    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # When they press space to compare
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
              ### compare their current val to goal_num
              pass

    ######## Update

    all_sprites.update()

    # hits between player and numbers
    _hits1 = pygame.sprite.spritecollide(player, numbers, True)
    
    if _hits1:
        for num in _hits1:
            player.current.append(num.val)

    # keeps 5 fish on screen at all times
    if len(numbers) < 5:
        create_number(5 - len(numbers))
        
    # hits between the arithmetic signs and player
    _hits2 = pygame.sprite.spritecollide(player, all_signs, False)
    
    if _hits2:
        for hit in _hits2:
            player.current.append(hit.sign)
                   
    ######## Render (draw)

    screen.fill(BLACK)
    screen.blit(background, bg_rect)
    all_signs.draw(screen)
    all_sprites.draw(screen)

    
    pygame.display.flip()
    
pygame.quit()

