# 🚀 Python CGPA Calculator (V2 – CSV Storage)

A **Command-Line Interface (CLI)** application built with Python to calculate CGPA using the UoPeople grading scale, with **persistent data storage using CSV files**.

---

## 📌 Project Overview

This project extends the V1 CGPA calculator by introducing **file-based data persistence**. Instead of storing scores temporarily, course data is now saved and reused across program runs.

**Features:**

- Stores course data in a CSV file
- Allows adding new courses interactively
- Reads and processes stored data
- Converts raw scores (0–100) to GPA
- Treats credit units as a constant (3 per course)
- Dynamically calculates CGPA from stored records

---

## 🏗️ Architecture Design

The program follows a **modular and structured design**:

| Function | Purpose |
|----------|---------|
| `score_to_gpa(score)` | Converts raw score to GPA |
| `initialize_file()` | Ensures CSV file exists with header |
| `add_courses()` | Handles user input and saves data to CSV |
| `read_courses()` | Reads stored data from CSV file |
| `calculate_cgpa(courses)` | Computes CGPA from stored data |
| `display_courses(courses)` | Displays course records |
| `main()` | Controls application flow (menu system) |

**Execution entry point:**

```python
if __name__ == "__main__":
    main()
```

## 📁 Data Storage (CSV)

Course data is stored in a CSV file in the following format:

course,score
Math,95
English,88
Python,76

This enables persistent storage and reuse of academic records.

## 🧮 CGPA Formula
CGPA = (Σ GPA × Credit) / Total Credits

Since each course has a constant credit of 3:

Total Credits = Number of Courses × 3

The final CGPA is rounded to 2 decimal places.

## 🛠️ Technologies Used
* **Python 3**

* **Standard Library:**
  * `csv` → file handling
  * `os` → file checking

> No external libraries required.

## ▶️ How to Run
1. Clone the repository
2. Navigate to the project folder
3. Run:
```python 
cgpa_calculator.py
```

## 📂 Example Usage
### Add Courses

#### Menu:

1. Add Courses
2. View Courses & CGPA
3. Exit

#### Example Interaction:

Choose an option: 1  
How many courses to add: 2

Course name 1: Math  
Score for Math: 95

Course name 2: English  
Score for English: 88

Courses added successfully!

### View CGPA
Choose an option: 2

--- Course Records ---
|-------|-------|-------|
| 1. Math | Score: 95.0 | GPA: 4.0 |
| 2. English | Score: 88.0 | GPA: 3.33 |

Your CGPA is: 3.67

## 🎯 Design Decisions
* Data is stored persistently using CSV
* GPA values are computed dynamically
* CGPA is calculated from stored records
* Credit unit is constant for simplicity
* Menu-driven interface improves usability

## 🚀 Future Improvements (V3+ Ideas)
* Edit or delete course records
* Support variable credit units
* Add data validation improvements
* Convert into REST API (Flask / FastAPI)
* Add automated unit tests
* Build a graphical interface (GUI)

## 📚 Learning Goals

This project demonstrates:

* File handling with CSV
* Persistent data storage
* Modular programming design
* Input validation
* CLI application structure
* Real-world data processing workflow

## 👩‍💻 Author

Personal project built as part of a backend/data engineering learning journey.