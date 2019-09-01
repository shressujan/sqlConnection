
import mysql.connector

con = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password=''
)

#cursor
cursor = con.cursor()

#create a database
db = "CREATE DATABASE IF NOT EXISTS UNL"
cursor.execute(db)

#Drop the table when needed
# sql = "DROP TABLE UNL.userAccount"
# cursor.execute(sql)

#create table


table = "CREATE TABLE IF NOT EXISTS UNL.students (nuid INT PRIMARY KEY," \
        " firstName VARCHAR(255)," \
        " lastName VARCHAR(255)," \
        " level VARCHAR(255)," \
        " department VARCHAR(255))"

studentAccountTable = "CREATE TABLE IF NOT EXISTS UNL.studentAccount (nuid INT PRIMARY KEY," \
                   " username VARCHAR(255)," \
                   " password VARCHAR(255))"


cursor.execute(table)
cursor.execute(studentAccountTable)

cursor.close()
con.commit()
con.close()
