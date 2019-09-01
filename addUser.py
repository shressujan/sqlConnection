import mysql.connector
import uuid
import hashlib


def hash_password(password):
    salt = uuid.uuid4().hex
    print('salt is: ' + salt)

    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


con = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    database='UNL',
    password=''
)

nuid = input("Enter nuid: ")
username = input("Enter username: ")
student_password = input("Enter password: ")


add_student_account = "INSERT INTO studentAccount (nuid, username, password)" \
                      "VALUES (%s, %s, %s)"
student_account_data = (nuid, username, hash_password(student_password))

cursor = con.cursor()
cursor.execute(add_student_account, student_account_data)

cursor.close()
con.commit()
con.close()
