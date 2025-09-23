import csv
from file_handler import read_students, write_students

def delete_student():
    roll = input("Enter Roll_No to delete: ")
    students = read_students()
    for s in students:
        if s["Roll_No"] == roll:
            confirm = input(f"Are you sure to delete {s['Name']}? (Y/N): ")
            if confirm.lower() == "y":
                students.remove(s)
                write_students(students)
                with open("students_deleted.csv", "a", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=s.keys())
                    if f.tell() == 0: writer.writeheader()
                    writer.writerow(s)
                print("Student deleted & archived")
            return
    print("Roll_No not found")
