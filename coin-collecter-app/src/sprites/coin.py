import os
import random
import pygame
from utils.utils import set_position

dirname = os.path.dirname(__file__)


class Coin(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "coin.png"))
        self.rect = self.image.get_rect()
        self.speed = 2

        set_position(self.rect, x, y, (-1250 // 2, 0))

    def update(self):
        """moves coin down and wraps if it gets to the bottom"""
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.randomize_position()

    def randomize_position(self):
        """moves coin to a random start position at the top"""
        self.rect.x = random.randint(0, 1250 - self.rect.width)
        self.rect.y = random.randint(-700, -self.rect.height)
