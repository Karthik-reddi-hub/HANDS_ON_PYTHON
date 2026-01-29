name = input("Enter your full name: ").strip()
email = input("Enter your email id: ").strip()
mobile = input("Enter your mobile number: ").strip()
age = int(input("Enter Age: "))

valid = True


if len(name) == 0 or name.count(' ') < 1:
    valid = False


if '@' not in email or '.' not in email or email[0] == '@':
    valid = False

if len(mobile) != 10 or not mobile.isdigit() or mobile[0] == '0':
    valid = False


if age < 18 or age > 60:
    valid = False

if valid:
    print("User Profile is Valid")
else:
    print("User Profile is Invalid")
