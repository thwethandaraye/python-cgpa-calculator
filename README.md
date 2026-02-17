# Python CGPA Calculator (V1)

A simple Command-Line Interface (CLI) application built with Python to calculate CGPA based on raw course scores using the UoPeople grading scale.

---

## 📌 Project Overview

This project simulates a basic academic CGPA calculation system. It is designed with modular functions and clean program structure, following good backend-oriented coding practices.

The calculator:

* Accepts the number of completed courses
* Collects raw scores (0–100)
* Converts scores to GPA using the UoPeople grading scale
* Treats credit units as a constant (3 per course)
* Dynamically calculates CGPA (not stored permanently)

---

## 🏗️ Architecture Design

The program follows a simple modular structure:

* `score_to_gpa(score)` → Converts raw score to GPA
* `input_scores()` → Handles user input and validation
* `calculate_cgpa(scores)` → Computes final CGPA
* `main()` → Controls application flow

The execution entry point is protected using:

```python
if __name__ == "__main__":
    main()
```

This ensures the file can be imported as a module without automatically running the CLI.

---

## 🧮 CGPA Formula

[
CGPA = \frac{\sum (GPA \times Credit)}{Total Credits}
]

Since each course has a constant credit of 3:

[
Total Credits = Number of Courses \times 3
]

The final CGPA is rounded to 2 decimal places.

---

## 🛠️ Technologies Used

* Python 3
* Standard Library (`time` for optional animation)

No external libraries required.

---

## ▶️ How to Run

1. Clone the repository
2. Navigate to the project folder
3. Run:

```bash
python cgpa_calculator.py
```

---

## 📂 Example Output

```
Welcome to UoPeople CGPA Calculator! (V1)

Enter the number of courses completed: 3
Enter score for course number 1: 94
Enter score for course number 2: 88
Enter score for course number 3: 76

Calculating CGPA...
Course 1: Score = 94, GPA = 4.0
Course 2: Score = 88, GPA = 3.33
Course 3: Score = 76, GPA = 2.0

Your CGPA is: 3.11
```

---

## 🎯 Design Decisions

* Raw scores are stored in a list
* GPA values are computed dynamically (not stored)
* CGPA is calculated when needed (not persisted)
* Credit unit is constant to simplify v1 implementation

This keeps the logic minimal and extensible for future versions.

---

## 🚀 Future Improvements (V2+ Ideas)

* Store data in a file (JSON or CSV)
* Add per-course updates
* Support variable credit units
* Convert into a REST API (Flask / FastAPI)
* Add automated unit tests

---

## 📚 Learning Goals

This project demonstrates:

* Function design and modular programming
* Input validation
* Control flow (loops & conditionals)
* Basic academic calculation logic
* Clean program entry structure

---

## 👩‍💻 Author

Personal project built as part of a backend/data engineering learning journey.
