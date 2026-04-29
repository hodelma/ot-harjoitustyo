from db.database_connection import get_database_connection


class ScoreRepository:
    """Handles persistence of game scores to the database.

    Attributes:
        _connection: Database connection object for executing queries.
    """
    def __init__(self, connection):
        """Initialize the ScoreRepository with a database connection.

        Args:
            connection: Database connection object.
        """
        self._connection = connection

    def save_score(self, score):
        """Save a score to the database.

        Args:
            score: The score value to save.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO scores (score) VALUES (?);",(score,))
        self._connection.commit()

    def get_high_score(self):
        """Retrieve the highest score from the database.

        Returns:
            int: The highest score, or 0 if no scores exist.
        """
        cursor = self._connection.cursor()
        result = cursor.execute(
            "SELECT MAX(score) AS high_score FROM scores;").fetchone()
        return result["high_score"] or 0

    def get_recent_scores(self, limit=10):
        """Retrieve the most recent scores from the database.

        Args:
            limit: Maximum number of recent scores to retrieve. Defaults to 10.

        Returns:
            List: A list of score records ordered by most recent first.
        """
        cursor = self._connection.cursor()
        rows = cursor.execute(
            "SELECT score FROM scores ORDER BY id DESC LIMIT ?;", (limit,)).fetchall()
        return rows

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM scores;")
        self._connection.commit()


def get_score_repository():
    """Factory function to create and return a ScoreRepository instance.

    Creates a database connection and wraps it in a ScoreRepository for
    managing score persistence.

    Returns:
        ScoreRepository: A repository instance for score operations.
    """
    connection = get_database_connection()
    return ScoreRepository(connection)
