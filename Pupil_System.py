import re
import csv
usernames = []
students = []

def LastStudent():

    print("Is this your last student? (Y/N)")
    choice = input('>').lower()

    while choice not in ['y', 'n']:
        choice = input('>')

    if choice == "y":

        print("Return to main menu? (Y)")
        toMain = input('>').lower()

        while toMain not in ['y']:
            toMain = input('>')

        if toMain == "y":
            mainmenu()

    elif choice == "n":
        addStudents()


def addStudents():
    print("You have choosen to add students")
    count = 0
    Number_of_Pupils = int(input("How many students do you want to add? "))
    while count < int(Number_of_Pupils):
        count += 1
        StudentName = input("Student Name: ").lower()

        with open('Studentname.csv', 'a', newline='') as file:
            fieldnames = ['StudentName']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'StudentName': StudentName})
            print("Student Added")
    LastStudent()

def searchStudents():
    print("You have choosen to Search students")
    with open('Studentname.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            students.append(row)
            print(students)
        StudentName = input("Student Name: ").lower()
        if StudentName in students:
            coldex = students.index(StudentName)
            print(StudentName, "Found! ")
            print(students)
        else:
            print("Student Not Found!")


def removeStudents():
    print("You have choosen to remove students")
def sortStudents():
    print("You have choosen to sort students")

def Register():
    print("Register Menu")
    usernameinput = input("Enter a Username: ").lower()
    print("Password Criteria:\nMust be 8 or more characters\nMust have a lower case\nMust have a upper case\nMust contain numbers\nMust have special letters\n")
    while True:
        passwordinput = input("Enter a Password: ")
        if (len(passwordinput) <= 8):
            print("Password is too short, It must be 8 or more characters.")
        elif not re.search("[a-z]", passwordinput):
            print("Password must contain lowercase letters")
        elif not re.search("[A-Z]", passwordinput):
            print("Password must contain uppercase letters")
        elif not re.search("[0-9]", passwordinput):
            print("Password must contain numbers")
        elif not re.search("[_@$]", passwordinput):
            print("Password must contain special characters like $")
        else:
            break
    with open('Register.csv', 'r') as file:
        csv_reader = csv.reader(file)
        xyz = 0
        for row in csv_reader:

            for xyz in range(len(row)-1):
                usernames.append(f'{row[0]}')

    y = 0

    for x in range(len(usernames)):
        if usernameinput == usernames[x]:
            print("Username Already Exists\n")
            y = 1
            Register()
    if y == 0:
        with open('Register.csv', 'a') as csvfile:
             fieldnames = ['Username', 'Password']
             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
             writer.writerow({'Username': usernameinput, 'Password': passwordinput})
             print("Registered Successfully!")


def mainmenu():
    print("Main Menu")
    print("1. Add Students")
    print("2. Search Students")
    print("3. Sort Students")
    print("4. Remove Students")
    print("5. Log out")
    choice = int(input("-> "))

    if choice == 1:
        addStudents()
    elif choice == 2:
        searchStudents()
    elif choice == 3:
        sortStudents()
    elif choice == 4:
        removeStudents()
    elif choice == 5:
        quit()

def login():
    notloggedin = True
    while notloggedin == True:
        print("***WELCOME - PLEASE LOGIN")
        with open("Register.csv", 'r') as csvfile:
            username = input("Enter username:-")
            password = input("Enter password:-")
            csvfile_Reader = csv.reader(csvfile)
            for row in csvfile_Reader:
                for field in row:
                    if field == username and row[1] == password:
                        print('Logged in')
                        notloggedin = False
                        mainmenu()



def main():
    print('1) Login')
    print('2) Register')
    print('x - Exit')
    choice = input('>')

    while choice not in ['1', '2', 'x']:
        choice = input('>')

    if choice == '1':
        login()
    elif choice == '2':
        Register()
    elif choice == 'x':
        quit()
main()
