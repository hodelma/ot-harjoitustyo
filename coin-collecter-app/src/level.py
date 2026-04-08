import pygame
from sprites.player import Player
from sprites.coin import Coin
from sprites.monster import Monster
from game_logic import Game


class Level:
    """manages all game objects and handles collisions"""
    def __init__(self):
        self.game = Game()

        #creates sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()

        #initializes game objects
        self.player = Player(600, 200)
        self.all_sprites.add(self.player)

        #creates three coins randomly on the screen
        for _ in range(3):
            coin = Coin()
            self.all_sprites.add(coin)
            self.coins.add(coin)

        #creates two monsters randomly
        for _ in range(2):
            monster = Monster()
            self.all_sprites.add(monster)
            self.monsters.add(monster)
