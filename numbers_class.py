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
        
        self.image = pygame.image.load('fish.png').convert()
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        # starting position
        self.rect.left = WIDTH
        self.rect.top = random.randrange(32, HEIGHT - 32)
        
        # speeds
        self.speed = random.randrange(1, 5)
        
        # the objects mathematical value
        self.val = random.randrange(1, 9)
        
    def update(self):
        self.rect.x -= self.speed