import pygame


class Arithmatics(pygame.sprite.Sprite):
    def __init__(self, sign, pos_x, pos_y, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.sign = sign
        
        #maybe add sound later

