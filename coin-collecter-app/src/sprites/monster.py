import os
import random
import pygame
from utils.utils import set_position

dirname = os.path.dirname(__file__)


class Monster(pygame.sprite.Sprite):
    """enemy drops from the sky"""
    def __init__(self, x=None, y=None):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "monster.png"))
        self.rect = self.image.get_rect()
        self.speed = 3

        set_position(self.rect, x, y, (-700 // 2, -self.rect.height))

    def update(self):
        """move monster down and reset position"""
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, 1250 - self.rect.width)
        self.rect.y = random.randint(-700, -self.rect.height)
