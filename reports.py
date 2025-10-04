# reports.py
import csv
from file_handler import read_students
from utils import grade

def generate_report():
    branch = input("Enter Branch: ")
    year = input("Enter Year: ")
    students = [s for s in read_students() if s["Branch"] == branch and s["Year"] == year]

    if not students:
        print("No students found for this branch/year")
        return

    total_students = len(students)
    avg_marks = sum((float(s["Mid1_Marks"]) + float(s["Mid2_Marks"]) +
                     float(s["Quiz_Marks"]) + float(s["Final_Marks"])) / 4 for s in students) / total_students
    highest = max(students, key=lambda s: float(s["Final_Marks"]))
    lowest = min(students, key=lambda s: float(s["Final_Marks"]))

    print("\nReport:")
    print(f"Total Students: {total_students}")
    print(f"Class Average: {avg_marks:.2f}")
    print(f"Highest Scorer: {highest['Name']} ({highest['Final_Marks']})")
    print(f"Lowest Scorer: {lowest['Name']} ({lowest['Final_Marks']})")

    # Grade distribution
    grades = {"A": 0, "B": 0, "C": 0, "D": 0}
    for s in students:
        total = (float(s["Mid1_Marks"]) + float(s["Mid2_Marks"]) +
                 float(s["Quiz_Marks"]) + float(s["Final_Marks"])) / 4
        grades[grade(total)] += 1

    print("Grade Distribution:", grades)

    # Export CSV
    filename = f"report_{branch}_{year}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Total Students", "Class Average", "Highest", "Lowest", "Grades"])
        writer.writerow([total_students, avg_marks, highest["Name"], lowest["Name"], grades])
    print(f"Report exported to {filename}")
