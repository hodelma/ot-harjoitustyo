import random

ALL_COINS = [
    (0.60, 1, "coin1.png"),
    (0.85, 2, "coin2.png"),
    (1.00, 3, "coin3.png"),]

def roll_coin():
    roll = random.random()
    for threshold, value, image_file in ALL_COINS:
        if roll < threshold:
            return value, image_file

class Game:
    """manages the game state and logic"""
    def __init__(self, score_repository=None):
        self.score = 0
        self.is_over = False
        self.won = False
        self.state = "menu"
        self.high_score = 0
        self.lives = 3
        self._score_repository = score_repository

    def collect_coin(self, value):
        self.score += value
        self.high_score = max(self.high_score, self.score)

        if self.has_won():
            self.won = True
            self.is_over = True
            self.state = "game_over"
            self._save_score()

    def hit_monster(self):
        """resets score when player hits a monster"""
        self.lives -= 1
        if self.lives <= 0:
            self.is_over = True
            self.state = "game_over"
            self._save_score()

    def _save_score(self):
        """saves score to db if repository exists"""
        if self._score_repository:
            self._score_repository.save_score(self.score)

    def has_won(self):
        """checks if the player has won the game"""
        return self.score >= 20

    def reset(self):
        """resets the game state"""
        self.score = 0
        self.is_over = False
        self.won = False
        self.state = "playing"
        self.lives = 3
