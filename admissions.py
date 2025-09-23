from file_handler import read_students, write_students
from models import Student
from utils import validate_student

def add_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    branch = input("Branch: ")
    year = input("Year: ")
    gender = input("Gender: ")
    age = input("Age: ")
    attendance = input("Attendance %: ")
    mid1 = input("Mid1 Marks: ")
    mid2 = input("Mid2 Marks: ")
    quiz = input("Quiz Marks: ")
    final = input("Final Marks: ")

    student = Student(roll, name, branch, year, gender, age,
                      attendance, mid1, mid2, quiz, final)

    students = read_students()
    if any(int(s["Roll_No"]) == student.roll_no for s in students):
        print("Duplicate Roll_No!")
        return

    valid, msg = validate_student(student.to_dict())
    if not valid:
        print(f"Validation failed: {msg}")
        return

    students.append(student.to_dict())
    write_students(students)
    print("Student added successfully!")
