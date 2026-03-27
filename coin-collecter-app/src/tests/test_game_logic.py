import unittest
from game_logic import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_initial_score_is_zero(self):
        self.assertEqual(self.game.score, 0)

    def test_collect_coin_increases_score(self):
        self.game.collect_coin()
        self.assertEqual(self.game.score, 1)

    def test_hit_monster_resets_score(self):
        self.game.collect_coin()
        self.game.collect_coin()
        self.game.hit_monster()
        self.assertEqual(self.game.score, 0)

    def test_has_won_returns_true_when_score_is_20(self):
        for _ in range(20):
            self.game.collect_coin()

        self.assertEqual(self.game.has_won(), True)

    def test_has_won_returns_false_when_score_is_less_than_20(self):
        for _ in range(10):
            self.game.collect_coin()

        self.assertEqual(self.game.has_won(), False)