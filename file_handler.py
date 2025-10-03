import csv
import os

CSV_FILE = "students.csv"

def read_students():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, newline="") as f:
        return list(csv.DictReader(f))

def write_students(students):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)

def append_student(student_dict):
    students = read_students()
    students.append(student_dict)
    write_students(students)
