# Lab 20 - Daily Log Book
import os


def append_entry(filename, entry):
    if not entry.strip():
        print("[ERROR] Log entry cannot be empty.")
        return
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(entry + "\n")
    except OSError as error:
        print(f"[ERROR] Could not append log entry: {error}")
    else:
        print(f"[SUCCESS] New entry logged to '{filename}'.")


def display_log(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            entries = file.read().splitlines()
    except FileNotFoundError:
        print("No log file exists yet. Add an entry first.")
    except (OSError, UnicodeError) as error:
        print(f"[ERROR] Could not read log: {error}")
    else:
        print("\nDAILY LOG BOOK")
        for number, entry in enumerate(entries, 1):
            print(f"[{number:02}] {entry}")
        print(f"Total Logged Entries: {len(entries)}")


def main():
    filename = "daily_log.txt"
    if not os.path.exists(filename):
        try:
            with open(filename, "x", encoding="utf-8") as file:
                file.write("09:00 AM - System server startup verified.\n"
                           "10:30 AM - Morning attendance synchronized.\n")
        except OSError as error:
            print(f"[ERROR] Could not create sample log: {error}")
    print("OFFICE DAILY LOG BOOK")
    while True:
        print("\n1. Add Log Entry\n2. Display Complete Log\n3. Exit")
        choice = input("Enter choice (1-3): ").strip()
        if choice == "1":
            append_entry(filename, input("Enter log entry: "))
        elif choice == "2":
            display_log(filename)
        elif choice == "3":
            print("Thank you for using the Daily Log Book. Goodbye!")
            break
        else:
            print("[ERROR] Choose an operation from 1 to 3.")


if __name__ == "__main__":
    main()
