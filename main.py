from admissions import add_student
from lookup import search_student
from updates import update_student
from deletions import delete_student
from reports import generate_report
from bulk_import import bulk_import
from sorting_filtering import sort_filter_students

def main_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student (Admission)")
        print("2. Search Student")
        print("3. Update Records")
        print("4. Delete Student")
        print("5. Generate Report")
        print("6. Bulk Import from CSV")
        print("7. Sort / Filter Students")
        print("8. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            filename = input("Enter CSV filename to import: ")
            bulk_import(filename)
        elif choice == "7":
            sort_filter_students()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
