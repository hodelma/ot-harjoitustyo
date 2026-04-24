import pygame
from sprites.player import Player
from sprites.coin import Coin
from sprites.monster import Monster
from game_logic import Game, roll_coin


class Level:
    """manages all game objects and handles collisions"""
    def __init__(self):
        self.game = Game()
        self._undefeatable_until = 0

        #creates sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()

        #initializes game objects
        self.player = Player(600, 200)
        self.all_sprites.add(self.player)

        #creates three coins randomly on the screen
        for _ in range(3):
            value, image_file = roll_coin()
            coin = Coin(value, image_file)
            self.all_sprites.add(coin)
            self.coins.add(coin)

        #creates two monsters randomly
        for _ in range(2):
            monster = Monster()
            self.all_sprites.add(monster)
            self.monsters.add(monster)

    def update(self, keys_pressed):
        """updates game state"""
        if self.game.state != "playing":
            return

        #this handles player movement
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

        #update falling coins and monsters every frame
        self.coins.update()
        self.monsters.update()

        # check collisions in every frame
        self._check_collisions()

    def _check_boundaries(self):
        """keeps player within screen bounds"""
        self.player.rect.x = max(0, min(self.player.rect.x, 1250 - self.player.rect.width))
        self.player.rect.y = max(0, min(self.player.rect.y, 700 - self.player.rect.height))

    def _check_collisions(self):
        """checks collisions with coins and monsters"""
        coins_hit = pygame.sprite.spritecollide(
            self.player, self.coins, True, pygame.sprite.collide_rect_ratio(0.7)
            )

        for coin in coins_hit:
            self.game.collect_coin(coin.value)
            value, image_file = roll_coin()
            new_coin = Coin(value, image_file)
            self.all_sprites.add(new_coin)
            self.coins.add(new_coin)

        right_now = pygame.time.get_ticks()
        if right_now >= self._undefeatable_until:
            monsters_hit = pygame.sprite.spritecollide(
                self.player, self.monsters, False, pygame.sprite.collide_rect_ratio(0.8))

            if monsters_hit:
                self.game.hit_monster()
                self._undefeatable_until = right_now + 2000

                for monster in monsters_hit:
                    monster.kill()
                    new_monster = Monster()
                    self.all_sprites.add(new_monster)
                    self.monsters.add(new_monster)

    def reset(self):
        """resets the level"""
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
