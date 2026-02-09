import json
from student import Student

DATA_FILE = "data.json"


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = Student(student_id, name, age, course)
    data = load_data()
    data.append(student.to_dict())
    save_data(data)

    print("✅ Student added successfully!")


def view_students():
    data = load_data()
    if not data:
        print("❌ No students found.")
        return

    for s in data:
        print(f"ID: {s['student_id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")


def search_student():
    student_id = input("Enter Student ID to search: ")
    data = load_data()

    for s in data:
        if s["student_id"] == student_id:
            print("✅ Student Found:")
            print(s)
            return

    print("❌ Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ")
    data = load_data()

    for s in data:
        if s["student_id"] == student_id:
            s["name"] = input("Enter new name: ")
            s["age"] = input("Enter new age: ")
            s["course"] = input("Enter new course: ")
            save_data(data)
            print("✅ Student updated successfully!")
            return

    print("❌ Student not found.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")
    data = load_data()

    new_data = [s for s in data if s["student_id"] != student_id]

    if len(new_data) == len(data):
        print("❌ Student not found.")
    else:
        save_data(new_data)
        print("✅ Student deleted successfully!")


def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice. Try again.")


menu()
