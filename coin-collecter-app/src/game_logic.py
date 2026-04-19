class Game:
    """manages the game state and logic"""
    def __init__(self):
        self.score = 0
        self.is_over = False
        self.won = False
        self.state = "menu"
        self.high_score = 0

    def collect_coin(self, value):
        self.score += value
        self.high_score = max(self.high_score, self.score)

        if self.has_won():
            self.won = True
            self.is_over = True
            self.state = "game_over"

    def hit_monster(self):
        """resets score when player hits a monster"""
        self.score = 0
        self.is_over = True
        self.state = "game_over"

    def has_won(self):
        """checks if the player has won the game"""
        return self.score >= 20

    def reset(self):
        """resets the game state"""
        self.score = 0
        self.is_over = False
        self.won = False
        self.state = "playing"
