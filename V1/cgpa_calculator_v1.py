"""
Python CGPA Calculator (V1)
--------------------------------
- Stores raw scores in a list
- Converts raw scores to GPA
- Treats credit unit as constant (3)
- Computes CGPA dynamically (not stored)
"""

import time

CREDITS = 3  # constant credit per course


def score_to_gpa(score):
    """Convert raw score to GPA according to UoPeople grading scale"""
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
        return 1.0
    else:
        return 0.0


def input_scores():
    """Ask user for number of courses and their scores"""
    scores = []

    while True:
        try:
            num_courses = int(input("Enter the number of courses completed: "))
            if num_courses <= 0 or num_courses > 40:
                print("Enter a number between 1 and 40!")
                continue
            break
        except ValueError:
            print("Enter a valid integer!")

    for i in range(1, num_courses + 1):
        while True:
            try:
                score = float(input(f"Enter score for course number {i}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Please enter a score between 0 and 100!")
            except ValueError:
                print("Please enter a valid number!")

    return scores


def calculate_cgpa(scores):
    """Calculate CGPA from list of scores"""
    total_points = 0
    total_credits = 0

    for score in scores:
        gpa = score_to_gpa(score)
        total_points += gpa * CREDITS
        total_credits += CREDITS

    if total_credits == 0:
        return 0.0

    return round(total_points / total_credits, 2)


def main():
    print("\nWelcome to UoPeople CGPA Calculator! (V1)\n")

    scores = input_scores()

    print("\nCalculating CGPA...")
    for i, score in enumerate(scores, start=1):
        time.sleep(0.3)  # optional delay for better UX
        print(f"Course {i}: Score = {score}, GPA = {score_to_gpa(score)}")

    cgpa = calculate_cgpa(scores)
    print(f"\nYour CGPA is: {cgpa}")


if __name__ == "__main__":
    main()