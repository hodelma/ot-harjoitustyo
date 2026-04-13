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

    def test_reset_gets_default_state_back(self):
        self.game.score = 5
        self.game.is_over = True
        self.game.won = True
        self.game.state = "game_over"
        self.game.reset()

        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.is_over, False)
        self.assertEqual(self.game.won, False)
        self.assertEqual(self.game.state, "playing")

    def test_high_score_stays_after_reset(self):
        for _ in range(3):
            self.game.collect_coin()
        self.game.reset()
        self.assertEqual(self.game.high_score, 3)

    def test_collect_coin_gives_win_at_20(self):
        self.game.score = 19
        self.game.collect_coin()

        self.assertEqual(self.game.won, True)
        self.assertEqual(self.game.is_over, True)
        self.assertEqual(self.game.state, "game_over")

    def test_hit_monster_sets_game_over(self):
        self.game.collect_coin()
        self.game.hit_monster()

        self.assertEqual(self.game.is_over, True)
        self.assertEqual(self.game.state, "game_over")
        self.assertEqual(self.game.won, False)
