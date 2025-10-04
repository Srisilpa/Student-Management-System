# sorting_filtering.py
from file_handler import read_students
import csv

def sort_filter_students():
    students = read_students()
    choice = input("Sort by (1) Marks (2) Filter by Attendance < threshold: ")

    if choice == "1":
        sorted_students = sorted(students, key=lambda s: float(s["Final_Marks"]), reverse=True)
        for s in sorted_students:
            print(s)
    elif choice == "2":
        threshold = float(input("Enter attendance threshold: "))
        filtered = [s for s in students if float(s["Attendance_%"]) < threshold]
        for s in filtered:
            print(s)
        if filtered:
            export = input("Export to CSV? (Y/N): ")
            if export.lower() == "y":
                with open("filtered_students.csv", "w", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=filtered[0].keys())
                    writer.writeheader()
                    writer.writerows(filtered)
                print("Exported to filtered_students.csv")
    else:
        print("Invalid choice")
