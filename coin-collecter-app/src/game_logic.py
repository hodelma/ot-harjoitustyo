import random

ALL_COINS = [
    (0.60, 1, "coin1.png"),
    (0.85, 2, "coin2.png"),
    (1.00, 3, "coin3.png"),]

def roll_coin():
    """Randomly rolls a coin based on weighted probabilities.

    Returns:
        Tuple: A tuple containing the coin value (1-3) and its image filename.
    """
    roll = random.random()
    for threshold, value, image_file in ALL_COINS:
        if roll < threshold:
            return value, image_file

class Game:
    """Manages the game state and logic.

    Attributes:
        score: Current score earned by the player.
        is_over: Flag indicating if the game has ended.
        won: Flag indicating if the player has won.
        state: Current game state.
        high_score: Highest score achieved in current session.
        lives: Number of lives remaining before game over.
    """
    def __init__(self, score_repository=None):
        """Initialize a new Game instance.

        Args:
            score_repository: Optional repository for saving and retrieving scores.
        """
        self.score = 0
        self.is_over = False
        self.won = False
        self.state = "menu"
        self.high_score = 0
        self.lives = 3
        self._score_repository = score_repository

    def collect_coin(self, value):
        """Add coin value to score and check for win condition.

        Args:
            value: The value of the collected coin.
        """
        self.score += value
        self.high_score = max(self.high_score, self.score)

        if self.has_won():
            self.won = True
            self.is_over = True
            self.state = "game_over"
            self._save_score()

    def hit_monster(self):
        """Handle player collision with a monster.

        Decreases lives by one and ends the game if lives reach zero.
        """
        self.lives -= 1
        if self.lives <= 0:
            self.is_over = True
            self.state = "game_over"
            self._save_score()

    def _save_score(self):
        """Save the current score to the database if repository is available."""
        if self._score_repository:
            self._score_repository.save_score(self.score)

    def has_won(self):
        """Check if the player has reached the win condition.

        Returns:
            bool: True if score is 20 or higher, False otherwise.
        """
        return self.score >= 20

    def reset(self):
        """resets the game state"""
        self.score = 0
        self.is_over = False
        self.won = False
        self.state = "playing"
        self.lives = 3
