from file_handler import read_students

def search_student():
    students = read_students()
    choice = input("Search by (1) Roll_No (2) Name: ")
    
    if choice == "1":
        roll = input("Enter Roll_No: ")
        result = [s for s in students if s["Roll_No"] == roll]
    else:
        name = input("Enter Name (partial ok): ").lower()
        result = [s for s in students if name in s["Name"].lower()]
    
    if result:
        for s in result:
            print(s)
    else:
        print("No student found")
