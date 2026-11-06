# Lab 19 - Student Notes Management System
import os


def write_notes(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    except OSError as error:
        print(f"[ERROR] Could not save notes: {error}")
    else:
        print(f"[SUCCESS] Notes successfully saved to '{filename}'.")


def read_notes(filename):
    if not os.path.exists(filename):
        return "No notes file exists yet. Save notes first."
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except (OSError, UnicodeError) as error:
        return f"[ERROR] Could not read notes: {error}"


def main():
    print("STUDENT NOTES MANAGEMENT SYSTEM")
    while True:
        print("\n1. Write / Save Notes (replaces previous notes)\n2. View Saved Notes\n3. Exit")
        choice = input("Enter choice (1-3): ").strip()
        if choice == "1":
            write_notes("notes.txt", input("Enter notes to save: "))
        elif choice == "2":
            print("\n--- Notes Content (notes.txt) ---")
            print(read_notes("notes.txt"))
        elif choice == "3":
            print("Thank you for using the Notes Management System. Goodbye!")
            break
        else:
            print("[ERROR] Choose an operation from 1 to 3.")


if __name__ == "__main__":
    main()
