import pygame

from objects import WIDTH, HEIGHT


class Equation(pygame.sprite.Sprite):
    def __init__(self, equation_string):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.equation = ""
        self.font = pygame.font.SysFont("comicsansms", 72)
        self.text = self.font.render(self.equation, True, (255, 255, 255))
        self.image.blit(self.text, (0, 0))

    def update(self):
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.text = self.font.render(self.equation, True, (255, 255, 255))
        self.image.blit(self.text, (0, 0))

    def set_equation(self, equation):
        self.equation = equation

    def get_equation(self):
        return self.equation

    def get_answer(self):
        return self.equation.split("=")[1]
