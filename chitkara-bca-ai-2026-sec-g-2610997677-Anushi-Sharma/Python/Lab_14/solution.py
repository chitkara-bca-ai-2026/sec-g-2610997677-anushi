# Lab 14 - Library Book Collection


def main():
    books = [
        ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
        ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
        ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
        ("Clean Code", "Robert C. Martin", "2008", "Software Engineering"),
    ]
    library_categories = {book[3] for book in books}
    student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}
    print("LIBRARY BOOK & CATEGORY MANAGER")
    while True:
        print("\n1. View Cataloged Books\n2. Add New Book Record\n3. View Unique Library Categories"
              "\n4. Add Category to Student Wishlist\n5. Run Category Gap Analysis\n6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            for number, book in enumerate(books, 1):
                title, author, year, category = book
                print(f'{number}. "{title}" by {author} ({year}) | Genre: {category}')
            print(f"Total Books: {len(books)}")
        elif choice == "2":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            year = input("Enter publication year: ").strip()
            category = input("Enter category/genre: ").strip()
            if all((title, author, year, category)):
                books.append((title, author, year, category))
                library_categories.add(category)
                print(f'[SUCCESS] "{title}" added as an immutable catalog record.')
                print(f'[INFO] Category set updated with: "{category}"')
            else:
                print("[ERROR] All book fields are required.")
        elif choice == "3":
            for category in sorted(library_categories):
                print(f"- {category}")
            print(f"Total Unique Genres: {len(library_categories)}")
        elif choice == "4":
            category = input("Enter requested category: ").strip()
            if category:
                student_wishlist.add(category)
                print(f'[SUCCESS] "{category}" added to student wishlist.')
            else:
                print("[ERROR] Category cannot be empty.")
        elif choice == "5":
            print("CATEGORY GAP ANALYSIS")
            print("Library Holdings (Set):", sorted(library_categories))
            print("Student Wishlist (Set):", sorted(student_wishlist))
            print("Already in Stock (Intersection &):", sorted(library_categories & student_wishlist))
            print("Purchase Order Needed (Difference -):", sorted(student_wishlist - library_categories))
            print("Full Combined Genre Coverage (Union |):", sorted(library_categories | student_wishlist))
        elif choice == "6":
            print("Thank you for using the Library Manager. Goodbye!")
            break
        else:
            print("[ERROR] Choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
