import unittest
from level import Level


class FakeKeys:
    def __getitem__(self, key):
        return False


class TestLevel(unittest.TestCase):

    def test_collect_coin_increases_score_and_replaces_coin(self):
        level = Level()
        level.game.state = "playing"

        coin = list(level.coins)[0]
        coin.rect.center = level.player.rect.center

        coin_count_before = len(level.coins)
        level.update(FakeKeys())

        self.assertEqual(level.game.score, 1)
        self.assertEqual(len(level.coins), coin_count_before)