student_id = input("Enter Student ID: ")
password = input("Enter Password: ")

id_valid = True

if len(student_id) != 6:
    id_valid = False
elif student_id[:3] != "STU":
    id_valid = False
elif not student_id[3:].isdigit():
    id_valid = False

password_valid = True
upper = False
lower = False
digit = False

if len(password) < 8:
    password_valid = False
else:
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True

    if not (upper and lower and digit):
        password_valid = False

if id_valid and password_valid:
    print("Access Granted")
else:
    print("Access Denied")

    if not id_valid:
        print("Invalid Student ID")

    if not password_valid:
        print("Invalid Password")
