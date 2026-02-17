user_input=input("Enter package weights separated by space: ")
weights=[]
current_number=""

for ch in user_input:
     if ch!=" ":
        current_number=current_number + ch
     else:
        if current_number!="":
            weights.append(int(current_number))
            current_number=""
if current_number!="":
      weights.append(int(current_number))
full_name = "Karthik Reddi"

L = 0
for ch in full_name:
    if ch!=" ":
        L=L+1
PLI=L%3

very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]

for weight in weights:

    if weight<0:
        invalid_entries.append(weight)

    elif weight>=0 and weight<=5:
        very_light.append(weight)

    elif weight>=6 and weight<=25:
        normal_load.append(weight)

    elif weight>=26 and weight<=60:
        heavy_load.append(weight)

    else:
        overload.append(weight)

total_valid = 0
for weight in weights:
    if weight>=0:
        total_valid=total_valid+1

affected_count = 0

if PLI == 0:
    for item in overload:
        invalid_entries.append(item)
        affected_count=affected_count+1
    overload=[]

elif PLI==1:
    for item in very_light:
        affected_count=affected_count+1
    very_light=[]

else:
    for item in very_light:
        affected_count=affected_count+1
    for item in overload:
        affected_count=affected_count+1
    very_light=[]
    overload=[]

print("\nL Value:", L)
print("PLI Value:", PLI)
print("Total Valid Weights:", total_valid)
print("Affected Items due to PLI:", affected_count)

print("\nFinal Loading Plan:")
print("Very Light:", very_light)
print("Normal Load:", normal_load)
print("Heavy Load:", heavy_load)
print("Overload:", overload)
print("Invalid Entries:", invalid_entries)
