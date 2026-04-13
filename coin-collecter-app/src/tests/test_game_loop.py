import unittest
import pygame
from game_loop import GameLoop
from level import Level


class DummyQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class DummyRenderer:
    def render(self):
        pass


class DummyClock:
    def tick(self, fps):
        pass


def _make_game_loop():
    level = Level()
    return GameLoop(level, DummyRenderer(), DummyQueue([]), DummyClock())


class TestGameLoop(unittest.TestCase):

    def test_menu_enter_resets_level_and_sets_state_playing(self):
        game_loop = _make_game_loop()
        game_loop._level.game.state = "menu"
        game_loop._level.game.score = 5

        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_RETURN})
        result = game_loop._menu_keydown(event)

        self.assertEqual(result, True)
        self.assertEqual(game_loop._level.game.state, "playing")
        self.assertEqual(game_loop._level.game.score, 0)