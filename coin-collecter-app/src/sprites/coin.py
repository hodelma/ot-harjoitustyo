import os
import random
import pygame

dirname = os.path.dirname(__file__)
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 700


class Coin(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None):
        super().__init__()

        self.coin_image = pygame.image.load(os.path.join(dirname, "..", "assets", "coin.png"))
        self.rect = self.coin_image.get_rect()
        self.speed = 2

        if x is None:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        else:
            self.rect.x = x

        if y is None:
            self.rect.y = random.randint(-SCREEN_HEIGHT // 2, 0)
        else:
            self.rect.y = y

    def update(self):
        """moves coin downward and wraps if it reaches bottom"""
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.randomize_position()

    def randomize_position(self):
        """moves coin to a random start position at the top"""
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-SCREEN_HEIGHT, -self.rect.height)
