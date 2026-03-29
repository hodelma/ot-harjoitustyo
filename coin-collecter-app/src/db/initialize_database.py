from .database_connection import get_database_connection


def drop_tables(connection):
    """deletes the tables"""
    cursor = connection.cursor()
    cursor.execute("drop table if exists players;")
    connection.commit()


def create_tables(connection):
    """creates the db tables"""
    cursor = connection.cursor()
    cursor.execute("""
        create table players (
            username text primary key,
            highscore integer default 0
        );
    """)
    connection.commit()


def initialize_database():
    """initializes the db tables"""
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)



if __name__ == "__main__":
    initialize_database()