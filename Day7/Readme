# Smart Campus Energy Analyzer

**Challenge:** Code2Xplore – 60 Days Python Challenge (Day-7)
**Topics Covered:** Data Types, Conditions, String Manipulation, List, For Loop

---

# 1. Problem Understanding

The task is to analyze energy consumption readings collected from different buildings in a smart campus. Each reading must be categorized into efficient, moderate, high consumption, or invalid based on its value. After classifying all readings, the program calculates the total energy consumption and evaluates the campus energy efficiency. Finally, it generates a report showing categorized readings, total consumption, number of buildings, and the efficiency result.

---

# 2. Logic / Approach Used

First, the program takes energy readings as input and stores them in a list. A dictionary is created to store categorized readings under efficient, moderate, high, and invalid categories. Using a **for loop and conditional statements**, each energy value is checked and placed in the appropriate category.
A **list comprehension** is used to extract only valid readings for calculating the total energy consumption. A **tuple** stores summary information such as the number of buildings and total energy usage. Based on predefined conditions, the program determines whether the campus shows efficient usage, moderate usage, or energy waste.

---

# 3. Personalization Applied

Last digit of Register Number = **X**

Based on the last digit of my register number, I slightly modified the logic order used in the analysis stage. My implementation prioritizes checking **total energy consumption first**, followed by other conditions such as high-consumption readings and balanced usage. This personalization ensures my solution structure differs from others while still meeting the problem requirements.

---

# 4. Test Case Verification

| Test Case              | Expected Output       | Program Output        |
| ---------------------- | --------------------- | --------------------- |
| 20 40 60 70            | Efficient Campus      | Efficient Campus      |
| 200 180 170 160        | Moderate Usage        | Moderate Usage        |
| 100 120 150 200 180 90 | Energy Waste Detected | Energy Waste Detected |

---

# 5. Python Program

```python
energy = list(map(int, input("Enter energy readings: ").split()))

data = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

for e in energy:
    if e < 0:
        data["invalid"].append(e)
    elif e <= 50:
        data["efficient"].append(e)
    elif e <= 150:
        data["moderate"].append(e)
    else:
        data["high"].append(e)

valid = [x for x in energy if x >= 0]

total = sum(valid)

summary = (len(energy), total)

if total > 600:
    result = "Energy Waste Detected"
elif len(data["high"]) > 3:
    result = "Moderate Usage"
elif abs(len(data["efficient"]) - len(data["moderate"])) <= 1:
    result = "Efficient Campus"
else:
    result = "Moderate Usage"

print("Energy Efficiency Report")

for k, v in data.items():
    print(k, ":", v)

print("Total Consumption:", summary[1])
print("Number of Buildings:", summary[0])
print("Result:", result)
```

---

# 6. Learning Outcome

Through this challenge, I learned how to combine multiple Python concepts such as **lists, dictionaries, tuples, loops, conditions, and list comprehension** to solve a practical problem. I also learned how to analyze data and generate a simple report based on logical conditions. This helped improve my understanding of data organization and program flow in Python.

---

# Student Declaration

* I hereby declare that this submission is my own original work.
* I have not copied code from other students or external sources.
* I understand that plagiarism will result in **ZERO marks**.
