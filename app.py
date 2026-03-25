"""
Python CGPA Calculator (V2 - CSV Version)
----------------------------------------
- Stores course data in CSV file
- Reads and writes persistent data
- Converts raw scores to GPA
- Calculates CGPA dynamically
- Menu-driven program
"""
import os
import csv

FILENAME = "grades.csv"
credits = 3  # constant credit per course

def score_to_gpa(score):
    """ Converted raw scores to gpa according to UoP grading scale """
    if 93 <= score <= 100:
        return 4.0
    elif 90 <= score <= 92:
        return 3.67
    elif 88 <= score <= 89:
        return 3.33
    elif 83 <= score <= 87:
        return 3.0
    elif 80 <= score <= 82:
        return 2.67
    elif 78 <= score <= 79:
        return 2.33
    elif 73 <= score <= 77:
        return 2.0
    elif 70 <= score <= 72:
        return 1.67
    elif 68 <= score <= 69:
        return 1.33
    elif 63 <= score <= 67:
        return 1.00
    else:
        return 0.0
    
# -----------------------------
# File Handling
# -----------------------------
def initialize_file():
    """Create CSV file with header if it doesn't exist"""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["course", "score"])


def read_courses():
    """Read all courses from CSV"""
    courses = []
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                courses.append({
                    "course": row["course"],
                    "score": float(row["score"])
                })
    except FileNotFoundError:
        print("No data file found.")
    return courses


def add_courses():
    """Add new courses to CSV"""
    while True:
        try:
            num = int(input("How many courses to add: "))
            if num <= 0:
                print("Enter a positive number!")
                continue
            break
        except ValueError:
            print("Enter a valid integer!")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)

        for i in range(1, num + 1):
            course = input(f"Course name {i}: ")

            while True:
                try:
                    score = float(input(f"Score for {course}: "))
                    if 0 <= score <= 100:
                        break
                    else:
                        print("Score must be between 0 and 100!")
                except ValueError:
                    print("Enter a valid number!")

            writer.writerow([course, score])

    print("Courses added successfully!")


# -----------------------------
# CGPA Calculation
# -----------------------------
def calculate_cgpa(courses):
    total_points = 0
    total_credits = 0

    for c in courses:
        gpa = score_to_gpa(c["score"])
        total_points += gpa * credits
        total_credits += credits

    if total_credits == 0:
        return 0.0

    return round(total_points / total_credits, 2)


def display_courses(courses):
    print("\n--- Course Records ---")
    for i, c in enumerate(courses, start=1):
        gpa = score_to_gpa(c["score"])
        print(f"{i}. {c['course']} | Score: {c['score']} | GPA: {gpa}")


# -----------------------------
# Main Menu
# -----------------------------
def main():
    initialize_file()

    print("\nWelcome to UoPeople CGPA Calculator (V2)\n")

    while True:
        print("\nMenu:")
        print("1. Add Courses")
        print("2. View Courses & CGPA")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_courses()

        elif choice == "2":
            courses = read_courses()

            if not courses:
                print("No data available.")
                continue

            display_courses(courses)
            cgpa = calculate_cgpa(courses)
            print(f"\nYour CGPA is: {cgpa}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()