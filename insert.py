import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='UNL'
)

cursor = db.cursor()

#insert rows into the table

add_Student = "INSERT INTO students " \
              "(nuid, firstName, lastName, level, department )" \
              "VALUES (%s, %s, %s, %s, %s)"
data_Student = (1, "sujan", "shrestha", "graduate", "Computer Science & Engineering")

cursor.execute(add_Student, data_Student)

cursor.close()
db.commit()
db.close()
