import pygame
from game_logic.level import Level
from ui.game_loop import GameLoop
from ui.renderer import Renderer
from event_queue import EventQueue
from clock import Clock
from repositories.score_repository import get_score_repository
from db.initialize_database import initialize_database


def main():
    """Initializes and starts the game.

    Sets up the pygame display, initializes the database, creates all
    game objects needed and starts the main game loop.
    """
    pygame.init()
    initialize_database()

    display = pygame.display.set_mode((1250, 700))
    pygame.display.set_caption("Coin Collector Game")

    level = Level()
    event_queue = EventQueue()
    score_repository = get_score_repository()
    renderer = Renderer(display, level.all_sprites, level.game, score_repository)
    clock = Clock()

    game_loop = GameLoop(level, renderer, event_queue, clock)
    game_loop.start()

    pygame.quit()


if __name__ == "__main__":
    main()
