# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 13:43:36 2022

@author: hbori
"""
import pygame

import random

WIDTH = 1050  # width of our game window
HEIGHT = 700  # height of our game window

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class numbers(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        image = ["can.png", "plastic-bottle.png", "plastic.png"]

        self.image = pygame.image.load(random.choice(image)).convert()
        self.image = pygame.transform.scale(self.image, (100, 100)).convert_alpha()

        self.image = pygame.transform.rotate(self.image, random.randint(-90, 90))

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        # the objects mathematical value
        self.val = str(random.randrange(1, 9))

        # add number to the image
        self.font = pygame.font.SysFont("comicsansms", 32)
        self.text = self.font.render(self.val, True, (255, 255, 255))
        self.image.blit(self.text, (0, 0))

        # starting position
        self.rect.left = WIDTH
        self.rect.top = random.randrange(32, HEIGHT - 32)

        # speeds
        self.speed = random.randrange(1, 5)

    def update(self):
        self.rect.x -= self.speed
