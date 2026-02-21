# 🎵 Smart Playlist Intelligence System

## 📌 Project Information
- **Course:** CSE205 – Hands-on Python  
- **Challenge:** Code2Xplore – 60 Days Challenge (Day-5)  
- **University:** SRM University–AP  
- **Register Number:** APA4110011888  

---

## 🧠 Problem Statement

The objective of this project is to analyze a music playlist represented as a list of song durations (in seconds).  
The system evaluates the playlist and categorizes it as:

- Too Short  
- Too Long  
- Repetitive  
- Balanced  
- Irregular  

Based on the detected category, the program provides a suitable recommendation.

---

## ⚙️ Features

- Accepts dynamic user input
- Validates invalid durations (≤ 0)
- Calculates total playlist duration
- Detects duplicate song durations
- Applies personalized variation logic
- Generates a final recommendation
- Uses only Python built-in functions (no external libraries)

---

## 📏 Classification Rules

| Condition | Category |
|------------|----------|
| Any duration ≤ 0 | Invalid Playlist |
| Total duration < 300 sec | Too Short Playlist |
| Total duration > 3600 sec | Too Long Playlist |
| Duplicate durations | Repetitive Playlist |
| Variation exceeds threshold | Irregular Playlist |
| Otherwise | Balanced Playlist |

---

## 🔢 Personalization Applied

- **Register Number:** APA4110011888  
- **Last Digit:** 8  
- **Variation Threshold:** `8 × 50 = 400`

If:

```python
max(playlist) - min(playlist) > 400
```

Then the playlist is categorized as **Irregular Playlist**.

This ensures the classification logic is personalized based on the register number.

---

## ▶️ How to Run

1. Open terminal or command prompt.
2. Navigate to the project folder.
3. Run the program:

```bash
python playlist.py
```

4. Enter song durations separated by space.

Example:
```
180 200 220 210
```

---

## 📌 Sample Output

```
Total Duration: 810 seconds
Songs: 4
Category: Balanced Playlist
Recommendation: Good listening session
```

---

## 📚 Learning Outcomes

- Practiced input validation techniques
- Implemented rule-based classification logic
- Applied conditional decision structures
- Used Python built-in functions effectively
- Integrated personalized logic into problem solving

---

## 👤 Author

**Name:** (Your Name)  
**Register Number:** APA4110011888  
**Course Code:** CSE205  
**University:** SRM University–AP  

---
