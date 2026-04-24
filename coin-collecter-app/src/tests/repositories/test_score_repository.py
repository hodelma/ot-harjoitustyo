import unittest
from repositories.score_repository import get_score_repository

class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        self._score_repository = get_score_repository()
        self._score_repository.delete_all()

    def test_save_score(self):
        self._score_repository.save_score(10)
        self.assertEqual(self._score_repository.get_high_score(), 10)

    def test_get_high_score(self):
        self._score_repository.save_score(5)
        self._score_repository.save_score(15)
        self._score_repository.save_score(8)
        self.assertEqual(self._score_repository.get_high_score(), 15)

    def test_get_recent_scores(self):
        self._score_repository.save_score(5)
        self._score_repository.save_score(10)
        scores = self._score_repository.get_recent_scores()
        self.assertEqual(len(scores), 2)