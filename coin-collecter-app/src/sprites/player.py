import os
import pygame

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    """the playable character that the user can play with"""
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "player.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 5

    def move(self, dx, dy):
        """moves the player by dx and dy pixels"""
        self.rect.x += dx
        self.rect.y += dy

    def reset_position(self, x, y):
        """resets player to its initial position"""
        self.rect.x = x
        self.rect.y = y
