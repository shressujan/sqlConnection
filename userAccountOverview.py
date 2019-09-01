import mysql.connector
import hashlib


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')

    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='UNL'
)

#login
nuid = input("Enter you nuid: ")
username = input("Enter your username: ")
entered_password = input("Enter you password: ")

# select query with where clause for filtering
student_password_sql = "SELECT password FROM studentAccount WHERE nuid = '%d'" % int(nuid)

cursor = db.cursor()

cursor.execute(student_password_sql)

# gets the first item that is return
student_password_result = cursor.fetchone()[0]

print("encrypted password is: " + student_password_result)

# condition to check if the login is successful or not
if check_password(student_password_result, entered_password):
    print("login successfull!!")
else:
    print("login failed!!")

cursor.close()
db.commit()
db.close()
