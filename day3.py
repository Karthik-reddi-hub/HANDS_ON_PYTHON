n=int(input("Enter number of students : "))
m=[0]*n
name="Karthik"
nameLength=len(name)

for i in range(n):
   m[i]=int(input(f"Enter the marks of student {i+1}: "))
totalvalidstudents = 0
totalfailstudents = 0

for i in range(n):
 mark=m[i]
 result = ""
if mark<0 or mark>100:
 result="Invalid"
else:
 totalvalidstudents += 1

if mark>=90:
 result="Excellent"
elif mark>=75:
 result="Very Good"
elif mark>=60:
 result="Good"
elif mark>=40:
 result="Average"
else:
 result="Fail"
 totalfailstudents+=1

if mark % nameLength == 0:
 result=result+"(Special Case)"

print(mark, "→", result)
print("Total Valid Students:", totalvalidstudents)
print("Total Failed Students:", totalfailstudents)
