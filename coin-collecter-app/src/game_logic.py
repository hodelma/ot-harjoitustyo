class Game:
    def __init__(self):
        self.score = 0

    def collect_coin(self):
        """increase score by one when a coin is collected"""
        self.score += 1

    def hit_monster(self):
        """reset score when player hits a monster"""
        self.score = 0

    def has_won(self):
        """check if the player has won the game"""
        return self.score >= 20
