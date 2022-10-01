import pygame

from objects import WIDTH, HEIGHT


class Goal(pygame.sprite.Sprite):
    def __init__(self, goal):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.goal = f"Goal: {goal}"
        self.font = pygame.font.SysFont("comicsansms", 64)
        self.text = self.font.render(self.goal, True, (255, 255, 255))
        self.image.blit(self.text, (0, HEIGHT - 100))

    def set_goal(self, goal):
        self.goal = goal

    def get_goal(self):
        return self.goal
