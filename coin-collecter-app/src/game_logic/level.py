import pygame
from sprites.player import Player
from sprites.coin import Coin
from sprites.monster import Monster
from game_logic.game_logic import Game, roll_coin
from repositories.score_repository import get_score_repository


class Level:
    """Manages all game objects and handles collisions.

    Attributes:
        game: The Game object tracking score, lives and game state.
        all_sprites: Group containing all sprites in the level.
        coins: Group containing all coin sprites.
        monsters: Group containing all monster sprites.
        player: The player sprite.
    """

    def __init__(self):
        """Initializes the level with a player, coins and monsters."""
        score_repository = get_score_repository()
        self.game = Game(score_repository)

        self.all_sprites = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()

        self.player = Player(600, 200)
        self.all_sprites.add(self.player)

        for _ in range(3):
            value, image_file = roll_coin()
            coin = Coin(value, image_file)
            self.all_sprites.add(coin)
            self.coins.add(coin)

        for _ in range(2):
            monster = Monster()
            self.all_sprites.add(monster)
            self.monsters.add(monster)

    def update(self, keys_pressed):
        """Updates game state based on player input and checks collisions.

        Args:
            keys_pressed: A pygame key state dict from pygame.key.get_pressed().
        """
        if self.game.state != "playing":
            return

        dx = 0
        dy = 0

        if keys_pressed[pygame.K_LEFT]:
            dx = -self.player.speed

        if keys_pressed[pygame.K_RIGHT]:
            dx = self.player.speed

        if keys_pressed[pygame.K_UP]:
            dy = -self.player.speed

        if keys_pressed[pygame.K_DOWN]:
            dy = self.player.speed

        if dx != 0 or dy != 0:
            self.player.move(dx, dy)

        self._check_boundaries()

        self.coins.update()
        self.monsters.update()

        self._check_collisions()

    def _check_boundaries(self):
        """Keeps player within screen bounds."""
        self.player.rect.x = max(0, min(self.player.rect.x, 1250 - self.player.rect.width))
        self.player.rect.y = max(0, min(self.player.rect.y, 700 - self.player.rect.height))

    def _check_collisions(self):
        """Checks and handles collisions between the player, coins and monsters.

        Collecting a coin replaces it with a new randomly generated coin.
        Hitting a monster costs a life and the monster is replaced with a new one.
        """
        coins_hit = pygame.sprite.spritecollide(
            self.player, self.coins, True, pygame.sprite.collide_rect_ratio(0.7))

        for coin in coins_hit:
            self.game.collect_coin(coin.value)
            value, image_file = roll_coin()
            new_coin = Coin(value, image_file)
            self.all_sprites.add(new_coin)
            self.coins.add(new_coin)

        monsters_hit = pygame.sprite.spritecollide(
            self.player, self.monsters, False, pygame.sprite.collide_rect_ratio(0.8))

        if monsters_hit:
            self.game.hit_monster()
            for monster in monsters_hit:
                monster.kill()
                new_monster = Monster()
                self.all_sprites.add(new_monster)
                self.monsters.add(new_monster)

    def reset(self):
        """Resets the level to its initial state."""
        self.game.reset()
        self.player.reset_position(1250 // 2, 700 // 2)

        self.all_sprites.remove(self.coins)
        self.coins.empty()

        for _ in range(3):
            value, image_file = roll_coin()
            coin = Coin(value, image_file)
            self.all_sprites.add(coin)
            self.coins.add(coin)

        for monster in self.monsters:
            monster.reset_position()
