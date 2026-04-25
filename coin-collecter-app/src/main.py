import pygame
from level import Level
from ui.game_loop import GameLoop
from ui.renderer import Renderer
from event_queue import EventQueue
from clock import Clock
from repositories.score_repository import get_score_repository


def main():
    """initializes and starts the game"""
    pygame.init()

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
