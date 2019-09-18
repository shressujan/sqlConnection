from database_connection import DatabaseConnection


class StudentInformation:

    def __init__(self, nuid, first_name, last_name, level_study, department):
        self.nuid = nuid
        self.first_name = first_name
        self.last_name = last_name
        self.level_study = level_study
        self.department = department

    @staticmethod
    def add_student_information(nuid):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        level_study = input("Enter the level of study: ")
        department = input("Enter what department you are in: ")

        add_student_query = "INSERT INTO students " \
                            "(studentAccount_nuid, firstName, lastName, level, department)" \
                            "VALUES (%s, %s, %s, %s, %s)"

        data_student = (nuid, first_name, last_name, level_study, department)

        db_connection = DatabaseConnection.initiate_database_connection()
        cursor = db_connection.cursor()
        cursor.execute(add_student_query, data_student)
        cursor.close()
        DatabaseConnection.exit_database_connection(db_connection)

    @staticmethod
    def get_student_information(nuid):
        student_information_query = "SELECT * FROM students WHERE nuid = '%d'" % int(nuid)

        db_connection = DatabaseConnection.initiate_database_connection()
        cursor = db_connection.cursor()
        cursor.execute(student_information_query)

        student_information_result = cursor.fetchone()
        cursor.close()
        DatabaseConnection.exit_database_connection(db_connection)

        return student_information_result
