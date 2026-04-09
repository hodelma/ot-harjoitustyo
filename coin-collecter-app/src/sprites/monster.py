import os
import random
import pygame

dirname = os.path.dirname(__file__)


class Monster(pygame.sprite.Sprite):
    """enemy drops from the sky"""
    def __init__(self, x=None, y=None):
        super().__init__()

        self.monster_image = pygame.image.load(os.path.join(dirname, "..", "assets", "monster.png"))
        self.rect = self.monster_image.get_rect()
        self.speed = 3

        if x is None:
            self.rect.x = random.randint(0, 1250 - self.rect.width)
        else:
            self.rect.x = x

        if y is None:
            self.rect.y = random.randint(-700 // 2, -self.rect.height)
        else:
            self.rect.y = y

    def update(self):
        """move monster down and reset position"""
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, 1250 - self.rect.width)
        self.rect.y = random.randint(-700, -self.rect.height)
