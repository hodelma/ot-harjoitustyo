from .database_connection import get_database_connection


def drop_tables(connection):
    """deletes the tables"""
    cursor = connection.cursor()
    cursor.execute("drop table if exists scores;")
    connection.commit()


def create_tables(connection):
    """creates the db tables"""
    cursor = connection.cursor()
    cursor.execute("""
        create table if not exists scores (
            id integer primary key autoincrement,
            score integer not null
        );
    """)
    connection.commit()


def initialize_database():
    """initializes the db tables"""
    connection = get_database_connection()
    create_tables(connection)



if __name__ == "__main__":
    initialize_database()
