

import pygame
class lives_class(pygame.sprite.Sprite):
    def __init__(self, pos_x, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, 100]