from password_encryptor import PasswordEncryptor
from database_connection import DatabaseConnection


class StudentAccount:

    def __init__(self, nuid, username, password):
        self.nuid = nuid
        self.username = username
        self.password = password

    def add_student_user_account(self):

        add_student_account = "INSERT INTO studentAccount (nuid, username, password)" \
                              "VALUES (%s, %s, %s)"

        hashed_password = PasswordEncryptor.hash_password(self.password)

        student_account_data = (int(self.nuid), self.username, hashed_password)

        db_connection = DatabaseConnection.initiate_database_connection()
        cursor = db_connection.cursor()
        cursor.execute(add_student_account, student_account_data)
        cursor.close()
        DatabaseConnection.exit_database_connection(db_connection)



