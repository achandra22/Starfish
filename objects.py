# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:24:11 2022

@author: hbori
"""
import pygame

WIDTH = 500
HEIGHT = 500

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# player_img = 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('starfish.png').convert()
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        # starting position
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
        # speeds
        self.speed = 5
        
    def update(self):
        
        # updating position
        
        self.speedx = 0
        self.speedy = 0
        
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
            
            
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # wrapping the object around
        
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH
            
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        
        
        