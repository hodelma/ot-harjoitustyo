import os
import random
import pygame
from utils.utils import set_position

dirname = os.path.dirname(__file__)


class Monster(pygame.sprite.Sprite):
    """An enemy sprite that falls from the sky.

    Attributes:
        speed: The vertical speed at which the monster falls.
    """
    def __init__(self, x=None, y=None):
        """Initialize a new Monster sprite.

        Args:
            x: Optional horizontal position; random if None.
            y: Optional vertical position; random if None.
        """
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "monster.png"))
        self.rect = self.image.get_rect()
        self.speed = 3

        set_position(self.rect, x, y, (-700 // 2, -self.rect.height))

    def update(self):
        """Move monster down and reset position if it leaves the screen."""
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.reset_position()

    def reset_position(self):
        """Move monster to a random position at the top of the screen."""
        self.rect.x = random.randint(0, 1250 - self.rect.width)
        self.rect.y = random.randint(-700, -self.rect.height)
