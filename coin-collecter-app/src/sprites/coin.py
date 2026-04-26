import os
import random
import pygame
from utils.utils import set_position

dirname = os.path.dirname(__file__)

COIN_SPEED = 2


class Coin(pygame.sprite.Sprite):
    """A collectible coin sprite that falls from the top of the screen.

    Attributes:
        value: The point value of the coin (1-3).
        speed: The vertical speed at which the coin falls.
    """
    def __init__(self, value, image_file, x=None, y=None):
        """Initialize a new coin sprite.

        Args:
            value: The point value of the coin.
            image_file: The filename of the coin's image asset.
            x: Optional horizontal position; random if None.
            y: Optional vertical position; random if None.
        """
        super().__init__()
        self.value = value
        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", image_file))
        self.rect = self.image.get_rect()
        self.speed = COIN_SPEED

        set_position(self.rect, x, y, (-1250 // 2, 0))

    def update(self):
        """Update coin position by moving it down the screen.

        Moves the coin downward and repositions it at the top if it goes
        off the bottom of the screen.
        """
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.randomize_position()

    def randomize_position(self):
        """Move coin to a random start position at the top of the screen.

        Repositions the coin with a random horizontal position and places it
        above the visible screen area.
        """
        self.rect.x = random.randint(0, 1250 - self.rect.width)
        self.rect.y = random.randint(-700, -self.rect.height)
