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
from goal_class import Goal
from helper_funcs import evaluate_equation
from lives_class import LivesClass

# import objects
FPS = 30  # frames per second

BLACK = (0, 0, 0)

garbage = pygame.image.load("assets/garbage.png")
pygame.display.set_icon(garbage)


# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
pygame.mixer.music.load("assets/game_music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Starfish")
clock = pygame.time.Clock()

### bg

background = pygame.image.load("assets/bg.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
bg_rect = background.get_rect()


goal_num = random.randrange(2, 20)
lives = 3

### sprites
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

equation = Equation("")
all_sprites.add(equation)

goal = Goal(str(goal_num))
all_sprites.add(goal)

all_signs = pygame.sprite.Group()
sign_plus = arithmatics_class.Arithmatics("+", 450, 650, "assets/plus.png")
all_signs.add(sign_plus)
sign_sub = arithmatics_class.Arithmatics("-", 550, 650, "assets/minus.png")
all_signs.add(sign_sub)

numbers = pygame.sprite.Group()

end_state = False


def create_number(n):

    for _ in range(n):
        number = numbers_class.numbers()
        all_sprites.add(number)
        numbers.add(number)


create_number(5)

###

# # Display the goal number
# font = pygame.font.SysFont("comicsansms", 72)
# text = font.render(str(goal_num), True, (0, 0, 0))
# screen.blit(text, (0, 0))

# Game Loop
running = True

####

start = False

font = pygame.font.SysFont("comicsansms", 72)
start_font = pygame.font.SysFont("comicsansms", 40)

while not start:
    
        screen.blit(background, bg_rect)
        text = start_font.render("Help penta-paul clean his ocean niche!", True, (255, 255, 255))
        text1 = start_font.render("Use the arrow keys to collect numbers and operations", True, (255, 255, 255))
        text2 = start_font.render("All the while cleaning up the seas!", True, (255, 255, 255))
        text3 = start_font.render("Press the U key to undo", True, (255, 255, 255))
        text4 = start_font.render("Press space to submit your expression", True, (255, 255, 255))
        text5 = start_font.render("To STARt press space!", True, (255, 255, 255))

        screen.blit(text, (WIDTH/2-350, 50))
        screen.blit(text1, (WIDTH/2-500, 130))
        screen.blit(text2, (WIDTH/2-320, 210))
        screen.blit(text3, (WIDTH/2-250, 290))
        screen.blit(text4, (WIDTH/2-350, 370))
        screen.blit(text5, (WIDTH/2-250, 450))
        pygame.display.flip()

        for event in pygame.event.get():
        # check for closing window
            if event.type == pygame.QUIT:
                start, running = True, False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start = True
####

while running:

    clock.tick(FPS)
    screen.blit(background, bg_rect)
    ######## Process input (events)

    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
            player.current = player.current[:-1]
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if int(evaluate_equation(player.current)) == goal_num:
                # win
                end_state = True
                running = False
            else:
                # lost life
                lives -= 1
                player.current = []

    if lives == 0:
        running = False
        end_state = False

    # lives update
    all_lives = pygame.sprite.Group()
    current_x = 1000
    for _ in range(lives):
        all_lives.add(LivesClass(current_x, "assets/heart.png"))
        current_x -= 80

    ######## Update

    all_sprites.update()

    # hits between player and numbers
    if hits1 := pygame.sprite.spritecollide(player, numbers, True):
        player.Sound()
        for num in hits1:
            if (
                len(player.current) == 0
                or len(player.current) > 0
                and not player.current[-1].isdigit()
            ):
                player.current.append(num.val)

    # respawns a new fish if one goes off screen
    for obj in numbers:
        if obj.rect.right < 0:
            numbers.remove(obj)

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

    screen.blit(background, bg_rect)
    all_lives.draw(screen)
    all_signs.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()


hi = True

starfish_happy = pygame.image.load("assets/starfish_end.png")
bg_happy = pygame.image.load("assets/bg_clean.jpg")
bg_happy = pygame.transform.scale(bg_happy, (WIDTH, HEIGHT))
bg_happy_rect = bg_happy.get_rect()

starfish_sad = pygame.image.load("assets/starfish_sad.png")
bg_sad = pygame.image.load("assets/bg_dirty.jpg")
bg_sad = pygame.transform.scale(bg_sad, (WIDTH, HEIGHT))
bg_sad_rect = bg_sad.get_rect()

middle = (WIDTH / 2, HEIGHT / 2)

while hi:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            hi = False
        if event.type == pygame.QUIT:
            hi = False

    if end_state:
        screen.fill(BLACK)
        screen.blit(bg_happy, bg_happy_rect)
        screen.blit(starfish_happy, (WIDTH / 2 - 128, HEIGHT / 2 - 128))
        text = font.render("You're a star!", True, (255, 255, 255))
        screen.blit(text, (WIDTH / 2 - 200, 0))

    elif end_state == False:
        screen.fill(BLACK)
        screen.blit(bg_sad, bg_sad_rect)
        screen.blit(starfish_sad, (WIDTH / 2 - 128, HEIGHT / 2 - 128))

        text = font.render(" what a Di-STAR-ster!", True, (255, 255, 255))
        screen.blit(text, (WIDTH / 2 - 400, 0))


    pygame.display.flip()


pygame.quit()
