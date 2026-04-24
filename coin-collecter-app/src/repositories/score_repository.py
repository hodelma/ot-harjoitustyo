from db.database_connection import get_database_connection


class ScoreRepository:
    def __init__(self, connection):
        self._connection = connection

    def save_score(self, score):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into scores (score) values (?);",(score,))
        self._connection.commit()

    def get_high_score(self):
        cursor = self._connection.cursor()
        result = cursor.execute(
            "select max(score) as high_score from scores;").fetchone()
        return result["high_score"] or 0

    def get_recent_scores(self, limit=10):
        cursor = self._connection.cursor()
        rows = cursor.execute(
            "select score from scores order by id desc limit ?;", (limit,)).fetchall()
        return rows

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from scores;")
        self._connection.commit()


def get_score_repository():
    connection = get_database_connection()
    return ScoreRepository(connection)
