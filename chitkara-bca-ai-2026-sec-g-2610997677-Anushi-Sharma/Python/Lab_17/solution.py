# Lab 17 - Student Records Handling


def calculate_results(marks):
    total = sum(marks)
    return total, total / len(marks)


def display_student(roll, student):
    total, average = calculate_results(student["Marks"])
    print(f"Roll No: {roll} | Name: {student['Name']} | Marks: {student['Marks']} "
          f"| Total: {total} | Average: {average:.2f}%")


def add_student(records, roll, name, marks):
    if roll in records:
        print("[ERROR] Roll number already exists.")
    elif not roll or not name or len(marks) != 3 or any(
        type(mark) is not int or not 0 <= mark <= 100 for mark in marks
    ):
        print("[ERROR] Enter a roll number, name, and 3 integer marks from 0 to 100.")
    else:
        records[roll] = {"Name": name, "Marks": marks}
        print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")


def main():
    students = {
        "101": {"Name": "Aman", "Marks": [85, 90, 78]},
        "102": {"Name": "Riya", "Marks": [92, 88, 95]},
        "103": {"Name": "Karan", "Marks": [74, 80, 82]},
    }
    print("STUDENT RECORDS MANAGEMENT SYSTEM")
    while True:
        print("\n1. Display All Students\n2. Add New Student\n3. Search Student\n4. Exit")
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            for roll, student in students.items():
                display_student(roll, student)
            print(f"Total Students: {len(students)}")
        elif choice == "2":
            roll = input("Enter Roll Number: ").strip()
            if not roll or roll in students:
                print("[ERROR] Roll number must be non-empty and unique.")
                continue
            name = input("Enter Student Name: ").strip()
            marks = []
            for subject in range(1, 4):
                while True:
                    try:
                        mark = int(input(f"Subject {subject}: "))
                        if 0 <= mark <= 100:
                            marks.append(mark)
                            break
                    except ValueError:
                        pass
                    print("[ERROR] Enter an integer from 0 to 100.")
            add_student(students, roll, name, marks)
        elif choice == "3":
            roll = input("Enter Roll Number to search: ").strip()
            student = students.get(roll)
            if student is None:
                print(f"[ERROR] No student found with Roll Number '{roll}'.")
            else:
                display_student(roll, student)
        elif choice == "4":
            print("Thank you for using the Student Records System. Goodbye!")
            break
        else:
            print("[ERROR] Choose an operation from 1 to 4.")


if __name__ == "__main__":
    main()
