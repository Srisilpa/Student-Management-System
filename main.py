from admissions import add_student
from lookup import search_student
from updates import update_student
from deletions import delete_student
from reports import generate_report
from bulk_import import bulk_import
from sorting_filtering import sort_filter_students

def main_menu():
    print("===== Welcome to Student Management System =====")
    
    # Select user role
    print("Select your role:")
    print("1. Office Clerk")
    print("2. Faculty / Teacher")
    print("3. HOD / Admin")
    role_choice = input("Enter role number: ")

    if role_choice == "1":
        role = "Office Clerk"
    elif role_choice == "2":
        role = "Faculty / Teacher"
    elif role_choice == "3":
        role = "HOD / Admin"
    else:
        print("Invalid role!")
        return

    while True:
        print(f"\n===== {role} Menu =====")
        
        if role == "Office Clerk":
            print("1. Add Student (Admission)")
            print("2. Delete Student")
            print("3. Bulk Import from CSV")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                add_student()
            elif choice == "2":
                delete_student()
            elif choice == "3":
                filename = input("Enter CSV filename to import: ")
                bulk_import(filename)
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

        elif role == "Faculty / Teacher":
            print("1. Search Student")
            print("2. Update Records (Marks/Attendance)")
            print("3. Generate Report")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                search_student()
            elif choice == "2":
                update_student()
            elif choice == "3":
                generate_report()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

        elif role == "HOD / Admin":
            print("1. Generate Summary Report (Avg Marks, Top Performers)")
            print("2. Export Data / Backup CSV")
            print("3. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                generate_report()  # You can modify to show summary-specific report
            elif choice == "2":
                filename = input("Enter filename to export CSV: ")
                bulk_import(filename)  # Or create a dedicated export function
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
