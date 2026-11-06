# Lab 18 - Mathematics Learning Tool


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print("MATHEMATICS LEARNING TOOL")
    while True:
        print("\n1. Calculate Factorial\n2. Generate Fibonacci Series\n3. Exit")
        choice = input("Enter choice (1-3): ").strip()
        if choice in ("1", "2"):
            prompt = "Enter a non-negative integer: " if choice == "1" else "Enter number of terms: "
            try:
                number = int(input(prompt))
            except ValueError:
                print("[ERROR] Enter a non-negative integer.")
                continue
            # shortcut: classroom recursion is bounded; use a faster algorithm for larger inputs.
            limit = 500 if choice == "1" else 30
            if not 0 <= number <= limit:
                print(f"[ERROR] Enter an integer from 0 to {limit} for this recursive demo.")
                continue
            if choice == "1":
                print(f"[RESULT] Factorial of {number} ({number}!) = {factorial(number)}")
            else:
                series = [fibonacci(i) for i in range(number)]
                print(f"[RESULT] Fibonacci series ({number} terms): {series}")
        elif choice == "3":
            print("Thank you for using the Mathematics Learning Tool. Goodbye!")
            break
        else:
            print("[ERROR] Choose an operation from 1 to 3.")


if __name__ == "__main__":
    main()
