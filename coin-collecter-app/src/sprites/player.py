import os
import pygame

dirname = os.path.dirname(__file__)

PLAYER_SPEED = 5


class Player(pygame.sprite.Sprite):
    """The playable character that the user controls.

    Attributes:
        speed: The movement speed in pixels per frame.
    """
    def __init__(self, x, y):
        """Initialize a new Player sprite.

        Args:
            x: Initial horizontal position in pixels.
            y: Initial vertical position in pixels.
        """
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "player.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = PLAYER_SPEED

    def move(self, dx, dy):
        """Move the player by the given deltas.

        Args:
            dx: Change in horizontal position (pixels).
            dy: Change in vertical position (pixels).
        """
        self.rect.x += dx
        self.rect.y += dy

    def reset_position(self, x, y):
        """Reset player to the specified position.

        Args:
            x: New horizontal position in pixels.
            y: New vertical position in pixels.
        """
        self.rect.x = x
        self.rect.y = y
