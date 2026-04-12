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

        coin_amount_before = len(level.coins)
        level.update(FakeKeys())

        self.assertEqual(level.game.score, 1)
        self.assertEqual(len(level.coins), coin_amount_before)

    def test_monster_collision_is_game_over(self):
        level = Level()
        level.game.state = "playing"

        monster = list(level.monsters)[0]
        monster.rect.center = level.player.rect.center

        level.update(FakeKeys())

        self.assertEqual(level.game.score, 0)
        self.assertEqual(level.game.is_over, True)
        self.assertEqual(level.game.state, "game_over")
        self.assertEqual(level.game.won, False)

    def test_reset_resets_player_score_and_coins(self):
        level = Level()
        level.game.state = "playing"
        level.game.score = 5
        level.player.rect.x += 100
        level.player.rect.y += 100

        level.reset()

        self.assertEqual(level.game.state, "playing")
        self.assertEqual(level.game.score, 0)
        self.assertEqual(level.player.rect.x, 1250 // 2)
        self.assertEqual(level.player.rect.y, 700 // 2)
        self.assertEqual(len(level.coins), 3)
