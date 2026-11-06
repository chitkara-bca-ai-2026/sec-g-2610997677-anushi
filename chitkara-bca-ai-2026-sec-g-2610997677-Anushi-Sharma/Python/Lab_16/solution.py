# Lab 16 - Utility Calculator
import math
import re
import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    return base ** exp


def format_number(n):
    return int(n) if math.isfinite(n) and n == int(n) else n


def read_number(prompt, allow_blank=False):
    while True:
        text = input(prompt).strip()
        if not text and allow_blank:
            return None
        if re.fullmatch(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?", text):
            number = float(text)
            if math.isfinite(number):
                return number
        print("[ERROR] Enter a finite number.")


def main():
    history = []
    print("ENTERPRISE MODULAR UTILITY CALCULATOR")
    while True:
        print("\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)"
              "\n5. Modulus / Remainder (%)\n6. Power / Exponentiation (Default: Square)"
              "\n7. View Calculation History\n8. Exit")
        choice = input("Enter your choice (1-8): ").strip()
        if choice == "8":
            print("Thank you for using the Utility Calculator. Goodbye!")
            break
        if choice == "7":
            if not history:
                print("No calculations yet.")
            for number, record in enumerate(history, 1):
                print(f"{number}. {record}")
            continue
        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("[ERROR] Choose a number from 1 to 8.")
            continue
        a = read_number("Enter base: " if choice == "6" else "Enter first number: ")
        if choice == "6":
            b = read_number("Enter exponent (Enter to square): ", allow_blank=True)
            use_default = b is None
            if use_default:
                b = 2
            if (a == 0 and b < 0) or (a < 0 and not float(b).is_integer()):
                print("[ERROR] Power is undefined for these real-number inputs.")
                continue
            # Check the result size before exponentiation, without exceptions.
            if a != 0 and b * math.log(abs(a)) >= math.log(sys.float_info.max):
                print("[ERROR] Result is too large.")
                continue
            result = power(a) if use_default else power(a, b)
            symbol = "**"
        else:
            b = read_number("Enter second number: ")
            if choice == "1":
                result, symbol = add(a, b), "+"
            elif choice == "2":
                result, symbol = subtract(a, b), "-"
            elif choice == "3":
                result, symbol = multiply(a, b), "*"
            elif choice == "4":
                result, symbol = divide(a, b), "/"
            else:
                result, symbol = modulus(a, b), "%"
        if result is None:
            print("[ERROR] Cannot divide or take modulus by zero.")
        elif not math.isfinite(result):
            print("[ERROR] Result is too large.")
        else:
            record = f"{format_number(a)} {symbol} {format_number(b)} = {format_number(result)}"
            history.append(record)
            print(f"[RESULT] {record}")


if __name__ == "__main__":
    main()
