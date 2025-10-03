# updates.py
from file_handler import read_students, write_students

def update_student():
    roll = input("Enter Roll_No to update: ")
    students = read_students()
    for s in students:
        if s["Roll_No"] == roll:
            print("Found:", s)
            
            # Show menu for update
            fields = ["Attendance_%", "Mid1_Marks", "Mid2_Marks", "Quiz_Marks", "Final_Marks"]
            print("Select field to update:")
            for i, f in enumerate(fields, start=1):
                print(f"{i}. {f}")
            
            choice = int(input("Enter choice number: "))
            if choice < 1 or choice > len(fields):
                print("Invalid choice")
                return
            
            field = fields[choice - 1]
            new_val = input(f"Enter new value for {field}: ")
            print(f"Old: {s[field]}, New: {new_val}")
            
            s[field] = new_val
            write_students(students)
            print("Record updated")
            return
    print("Roll_No not found")
