UserName = input("Enter the Username : ")
password = input("Enter the password : ")
Age = int(input("Enter the age : "))

problems = []
if len(UserName) < 4:
  problems.append("UserName should contain at least 4 letters")

if Age < 18:
  problems.append("User must be 18 years old or older")

if len(password) < 6:
  problems.append("Password should contain minimum 6 characters")

if len(problems) == 0:
    print("\nUser profile validated successfully!")
else:
    print("\nUser profile validation failed")
    print("Reasons:")
    for p in problems:
        print("-", p)
