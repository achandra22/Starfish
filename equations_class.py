import pygame

from objects import WIDTH, HEIGHT


class Equation(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("Hello World", True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
