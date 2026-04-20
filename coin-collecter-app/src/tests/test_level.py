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

        self.assertGreater(level.game.score, 0)
        self.assertEqual(len(level.coins), coin_amount_before)

    def test_monster_collision_reduces_lives(self):
        level = Level()
        level.game.state = "playing"
        monster = list(level.monsters)[0]
        monster.rect.center = level.player.rect.center
        level.update(FakeKeys())

        self.assertEqual(level.game.lives, 2)
        self.assertEqual(level.game.is_over, False)

    def test_three_monster_collisions_ends_game(self):
        level = Level()
        level.game.hit_monster()
        level.game.hit_monster()
        level.game.hit_monster()

        self.assertEqual(level.game.is_over, True)
        self.assertEqual(level.game.state, "game_over")

    def test_reset_resets_player_score_coins_and_lives(self):
        level = Level()
        level.game.score = 5
        level.game.hit_monster()
        level.reset()

        self.assertEqual(level.game.score, 0)
        self.assertEqual(level.game.lives, 3)
        self.assertEqual(len(level.coins), 3)
        self.assertEqual(level.player.rect.x, 1250 // 2)
        self.assertEqual(level.player.rect.y, 700 // 2)

    def test_player_stays_in_boundaries(self):
        level = Level()
        level.player.rect.x = -100
        level.player.rect.y = -100
        level._check_boundaries()

        self.assertEqual(level.player.rect.x, 0)
        self.assertEqual(level.player.rect.y, 0)

    def test_player_doesnt_move_without_input(self):
        level = Level()
        level.game.state = "playing"
        starting_position = level.player.rect.topleft
        level.update(FakeKeys())

        self.assertEqual(level.player.rect.topleft, starting_position)