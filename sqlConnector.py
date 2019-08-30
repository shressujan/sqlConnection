
import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='toor123$'
)

#Cursor
cursor = db.cursor()

# cursor.execute('SELECT * FROM sys.Student')
# for row in cursor.fetchall():
#     print(row)

add_Student = ("INSERT INTO sys.Student "
               "(nuid, firstName, lastName, level, department )"
               "VALUES (%s, %s, %s, %s, %s)")
data_Student = (2, 'john', 'shrestha', 'graduate', 'computer science & engineering')
cursor.execute(add_Student, data_Student)

cursor.execute('SELECT * FROM sys.Student')
for row in cursor.fetchall():
    print(row)


db.commit()
cursor.close()
db.close()
