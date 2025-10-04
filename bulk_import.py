# bulk_import.py
import csv
from file_handler import read_students, write_students
from utils import validate_student

def bulk_import(filename):
    students = read_students()
    errors = []

    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):  # start=2 to account for header line
            valid, msg = validate_student(row)
            if not valid or any(s["Roll_No"] == row["Roll_No"] for s in students):
                errors.append((i, row, msg or "Duplicate Roll_No"))
                continue
            students.append(row)

    write_students(students)

    if errors:
        with open("import_errors.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Line", "Error", "Data"])
            for line, row, err in errors:
                writer.writerow([line, err, row])
        print("Errors found! See import_errors.csv")
    else:
        print("Bulk import completed successfully")
