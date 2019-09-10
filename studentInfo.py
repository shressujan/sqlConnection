from database_connection import DatabaseConnection


class StudentInformation:

    def __init__(self, nuid, first_name, last_name, level, department):
        self.nuid = nuid
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.department = department

    def add_student_info(self):

        add_student = "INSERT INTO students " \
                      "(nuid, firstName, lastName, level, department )" \
                      "VALUES (%s, %s, %s, %s, %s)"

        data_student = (self.nuid, self.first_name, self.last_name, self.level, self.department)

        db_connection = DatabaseConnection.initiate_database_connection()
        cursor = db_connection.cursor()
        cursor.execute(add_student, data_student)
        cursor.close()
        DatabaseConnection.exit_database_connection(db_connection)
