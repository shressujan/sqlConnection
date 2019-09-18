from student_account import StudentAccount
from studentInformation import StudentInformation


def login():
    username = input("Enter username:")
    password = input("Enter password:")

    student_account = StudentAccount.get_student_account(username, password)

    if student_account:

        student_information = StudentInformation.get_student_information(student_account.nuid)
        print(student_information)

    else:
        choice = int(input("Login Failed!!!\n"
                           "Enter 1 to Login again\n"
                           "Enter 2 to create a student account: "))
        print(choice)
        selected_operation(choice)


def main():
    print("This is an SQL application that allows the user\n"
          "to create Student accounts in the mock student database\n"
          "and add their information "
          "and get student account information")
    login()


def default():
    return 0


def selected_operation(choice):

    switcher = {
        1: login,
        2: StudentAccount.add_student_account,
    }
    switcher.get(choice, default)()


if __name__ == '__main__': main()
