import mysql.connector


class DatabaseConnection:

    @staticmethod
    def initiate_database_connection():
        db_connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='UNL'
        )

        return db_connection

    @staticmethod
    def exit_database_connection(db_connection):
        db_connection.commit()
        db_connection.close()
