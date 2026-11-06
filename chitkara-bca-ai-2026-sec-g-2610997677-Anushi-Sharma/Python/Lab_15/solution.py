# Lab 15 - Student Information Management System


def main():
    students = {
        "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
        "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
        "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]},
    }
    print("STUDENT INFORMATION MANAGEMENT SYSTEM")
    while True:
        print("\n1. View All Students\n2. Search Student by Roll Number\n3. Register New Student"
              "\n4. Update Student Details\n5. View Academic Performance\n6. Delete Student Record\n7. Exit")
        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            for roll, student in students.items():
                print(f"Roll No: {roll} | Name: {student['Name']} | Branch: {student['Branch']}"
                      f" | Sem: {student['Semester']} | Marks: {student['Marks']}")
            print(f"Total Enrolled Students: {len(students)}")
        elif choice == "2":
            roll = input("Enter Roll Number to search: ").strip()
            student = students.get(roll)
            if student is None:
                print("[ERROR] Student not found.")
            else:
                print(f"[FOUND] Record for Roll No {roll}:")
                for field, value in student.items():
                    print(f"{field}: {value}")
        elif choice == "3":
            roll = input("Enter Roll Number: ").strip()
            if not roll or roll in students:
                print("[ERROR] Roll Number must be non-empty and unique.")
                continue
            name = input("Enter Student Name: ").strip()
            branch = input("Enter Branch: ").strip()
            semester = input("Enter Semester: ").strip()
            if not all((name, branch, semester)):
                print("[ERROR] All student fields are required.")
                continue
            marks = []
            for subject in range(1, 4):
                while True:
                    value = input(f"Subject {subject} marks (0-100): ").strip()
                    if value.isascii() and value.isdecimal() and len(value) <= 3 and int(value) <= 100:
                        marks.append(int(value))
                        break
                    print("[ERROR] Enter a whole number from 0 to 100.")
            students[roll] = {"Name": name, "Branch": branch, "Semester": semester, "Marks": marks}
            print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")
        elif choice == "4":
            roll = input("Enter Roll Number to update: ").strip()
            student = students.get(roll)
            if student is None:
                print("[ERROR] Student not found.")
                continue
            field = input("Choose field to update (1 for Branch, 2 for Semester): ").strip()
            if field not in ("1", "2"):
                print("[ERROR] Choose 1 or 2.")
                continue
            field = "Branch" if field == "1" else "Semester"
            value = input(f"Enter new {field.lower()}: ").strip()
            if value:
                student[field] = value
                print(f"[SUCCESS] {field} updated to '{value}'.")
            else:
                print("[ERROR] Value cannot be empty.")
        elif choice == "5":
            roll = input("Enter Roll Number for Academic Performance: ").strip()
            student = students.get(roll)
            if student is None:
                print("[ERROR] Student not found.")
                continue
            total = sum(student["Marks"])
            average = total / len(student["Marks"])
            print("ACADEMIC REPORT")
            print(f"Student Name: {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {student['Marks']}")
            print(f"Total Marks: {total} / 300")
            print(f"Average Marks: {average:.2f}%")
            print("Final Result:", "PASS" if average >= 40 else "FAIL")
        elif choice == "6":
            roll = input("Enter Roll Number to delete: ").strip()
            student = students.pop(roll, None)
            if student is None:
                print("[ERROR] Student not found.")
            else:
                print(f"[SUCCESS] Record for '{student['Name']}' (Roll No: {roll}) deleted successfully.")
        elif choice == "7":
            print("Thank you for using Student Information System. Goodbye!")
            break
        else:
            print("[ERROR] Choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
