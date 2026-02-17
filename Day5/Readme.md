# Day 5 – Smart Transport Load Balancing System

##  Problem Statement

A logistics company receives a list of package weights before transport.  
The system must classify each weight into predefined categories and apply a personalized adjustment rule (PLI) to ensure load balance and safety.

The final output displays categorized loads after personalization.

---

##  Approach

1. Accept weights from user input.
2. Convert input string into a list of integers manually using a loop.
3. Classify each weight using conditional statements:
   - < 0 → Invalid Entry
   - 0–5 → Very Light
   - 6–25 → Normal Load
   - 26–60 → Heavy Load
   - > 60 → Overload
4. Store values in separate lists.
5. Calculate:
   - Total valid weights (≥ 0)
   - Length of full name excluding spaces
   - PLI = L % 3
6. Apply rule based on PLI.
7. Display final categorized lists.

---

##  Personalization Details

Full Name Used: REDDI KARTHIK  

Length excluding spaces (L): 12  

PLI = 12 % 3 = 0  

Applied Rule: **Rule A**

Rule A → Move all Overload items to Invalid Entries.

---

##  Features Implemented

- Used only lists
- Used for loops
- Used conditional statements
- No list comprehension
- No dictionaries or sets
- No sum(), max(), min()
- No sorting
- Manual input parsing
- Counts affected items due to personalization

---

##  Sample Input


