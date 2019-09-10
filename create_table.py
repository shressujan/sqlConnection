from database_connection import DatabaseConnection

db_connection = DatabaseConnection.initiate_database_connection()

#cursor
cursor = db_connection.cursor()

#create a database
db = "CREATE DATABASE IF NOT EXISTS UNL"
cursor.execute(db)

#Drop the table when needed
# sql = "DROP TABLE UNL.userAccount"
# cursor.execute(sql)

#create table


studentInformationtable = "CREATE TABLE IF NOT EXISTS UNL.students (nuid INT PRIMARY KEY," \
        " firstName VARCHAR(255)," \
        " lastName VARCHAR(255)," \
        " level VARCHAR(255)," \
        " department VARCHAR(255))"

studentAccountTable = "CREATE TABLE IF NOT EXISTS UNL.studentAccount (nuid INT PRIMARY KEY," \
                   " username VARCHAR(255)," \
                   " password VARCHAR(255))"


cursor.execute(studentInformationtable)
cursor.execute(studentAccountTable)

cursor.close()
DatabaseConnection.exit_database_connection(db_connection)
