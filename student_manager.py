# Student Record Manager using Python Dictionary

# Dictionary to store student data
students = {}  # Format: { student_id: {"name": ..., "age": ..., "grade": ...} }

def add_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student already exists!")
    else:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        students[student_id] = {"name": name, "age": age, "grade": grade}
        print("Student added successfully!")

def search_student():
    student_id = input("Enter Student ID to search: ")
    if student_id in students:
        print(f"🎓 Student Found: {students[student_id]}")
    else:
        print("Student not found!")

def update_student():
    student_id = input("Enter Student ID to update: ")
    if student_id in students:
        print("Current Record:", students[student_id])
        name = input("Enter new Name (leave blank to keep same): ")
        age = input("Enter new Age (leave blank to keep same): ")
        grade = input("Enter new Grade (leave blank to keep same): ")
        
        if name:
            students[student_id]["name"] = name
        if age:
            students[student_id]["age"] = age
        if grade:
            students[student_id]["grade"] = grade
        print("Student updated successfully!")
    else:
        print("Student not found!")

def display_all():
    if students:
        print("All Student Records:")
        for sid, info in students.items():
            print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")
    else:
        print("⚠️ No records available.")

def menu():
    while True:
        print("\n--- Student Record Manager ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Display All Students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            display_all()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    menu()
