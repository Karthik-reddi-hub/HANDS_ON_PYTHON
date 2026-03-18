
# Energy readings input
energy = list(map(int, input("Enter energy readings: ").split()))

# dictionary for classification
data = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

# classification
for e in energy:

    if e < 0:
        data["invalid"].append(e)

    elif e <= 50:
        data["efficient"].append(e)

    elif e <= 150:
        data["moderate"].append(e)

    else:
        data["high"].append(e)


# list comprehension for valid readings
valid = [x for x in energy if x >= 0]

total = sum(valid)

# tuple summary
summary = (len(energy), total)


# efficiency analysis
if total > 600:
    result = "Energy Waste Detected"

elif len(data["high"]) > 3:
    result = "Moderate Usage"

elif abs(len(data["efficient"]) - len(data["moderate"])) <= 1:
    result = "Efficient Campus"

else:
    result = "Moderate Usage"


print("\nEnergy Efficiency Report")
print("-------------------------")

for k, v in data.items():
    print(k, ":", v)

print("Total Consumption:", summary[1])
print("Number of Buildings:", summary[0])
print("Result:", result)
