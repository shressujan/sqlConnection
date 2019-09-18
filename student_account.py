from password_encryptor import *
from database_connection import DatabaseConnection
from studentInformation import StudentInformation


class StudentAccount:

    def __init__(self, nuid, username, password):
        self.nuid = nuid
        self.username = username
        self.password = password

    @staticmethod
    def add_student_account():

        username = input("Enter username: ")
        password = input("Enter password: ")

        # TODO auto generate the nuid
        add_student_account_query = "INSERT INTO studentAccount (username, password)" \
                                    "VALUES (%s, %s)"

        hashed_password = hash_password(password)
        student_account_data = (username, hashed_password)

        db_connection = DatabaseConnection.initiate_database_connection()
        cursor = db_connection.cursor()
        cursor.execute(add_student_account_query, student_account_data)
        cursor.close()
        DatabaseConnection.exit_database_connection(db_connection)

        # adding student information after their account has been create
        student_account = StudentAccount.get_student_account(username, password)
        StudentInformation.add_student_information(student_account.nuid)

    @staticmethod
    def get_student_account(username, password):

        db_connection = DatabaseConnection.initiate_database_connection()
        cursor = db_connection.cursor()

        student_account_sql = "SELECT *  FROM studentAccount " \
                              "WHERE username = %s "

        data_student_account = (username, )
        cursor.execute(student_account_sql, data_student_account)
        student_account_result = cursor.fetchone()

        cursor.close()
        DatabaseConnection.exit_database_connection(db_connection)

        if student_account_result and check_password_matches(student_account_result[2], password):
            return StudentAccount(int(student_account_result[0]), username, password)

        else:
            return


