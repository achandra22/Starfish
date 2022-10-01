# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:15:04 2022

@author: hbori
"""

# from curses.textpad import rectangle
import pygame
import random

import arithmatics_class, numbers_class
from objects import Player, WIDTH, HEIGHT
from equations_class import Equation
from helper_funcs import evaluate_equation

# import objects
FPS = 30  # frames per second

BLACK = (0, 0, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
pygame.mixer.music.load("game_music.mp3")
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starfish")
clock = pygame.time.Clock()

### bg

background = pygame.image.load("bg.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
bg_rect = background.get_rect()

### sprites
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

equation = Equation("1 + 1 = 2")
all_sprites.add(equation)

all_signs = pygame.sprite.Group()
sign_plus = arithmatics_class.Arithmatics("+", 450, 650, "plus.png")
all_signs.add(sign_plus)
sign_sub = arithmatics_class.Arithmatics("-", 550, 650, "minus.png")
all_signs.add(sign_sub)

numbers = pygame.sprite.Group()


def create_number(n):

    for _ in range(n):
        number = numbers_class.numbers()
        all_sprites.add(number)
        numbers.add(number)


create_number(5)

###

goal_num = random.randrange(2, 40)

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

                if evaluate_equation(player.current) == goal_num:
                    print("you_win")
                else:

                    print("lost_a_life")

    ######## Update

    all_sprites.update()

    # hits between player and numbers
    if hits1 := pygame.sprite.spritecollide(player, numbers, True):
        for num in hits1:
            if (
                len(player.current) == 0
                or len(player.current) > 0
                and not player.current[-1].isdigit()
            ):
                player.current.append(num.val)

    # keeps 5 fish on screen at all times
    if len(numbers) < 5:
        create_number(5 - len(numbers))

    # hits between the arithmetic signs and player
    if hits2 := pygame.sprite.spritecollide(player, all_signs, False):
        for hit in hits2:
            if len(player.current) > 0 and player.current[-1] not in ["-", "+"]:
                player.current.append(hit.sign)

    equation.set_equation(" ".join(player.current))

    ######## Render (draw)

    screen.fill(BLACK)
    screen.blit(background, bg_rect)
    all_signs.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
