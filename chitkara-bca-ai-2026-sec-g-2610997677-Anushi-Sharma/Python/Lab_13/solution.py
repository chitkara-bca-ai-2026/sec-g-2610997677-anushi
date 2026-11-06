# Lab 13 - Inventory Control System


def main():
    inventory = ["Notebook", "Pen", "Eraser", "Ruler"]
    print("INVENTORY CONTROL SYSTEM")
    while True:
        print("\n1. View Inventory\n2. Add Item\n3. Remove Item\n4. Sort Inventory\n5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            print("--- Current Inventory ---")
            for number, item in enumerate(inventory, 1):
                print(f"{number}. {item}")
            if not inventory:
                print("Inventory is empty.")
        elif choice == "2":
            item = input("Enter item name to add: ").strip()
            if item:
                inventory.append(item)
                print(f'[SUCCESS] "{item}" added to inventory.')
            else:
                print("[ERROR] Item name cannot be empty.")
        elif choice == "3":
            item = input("Enter item name to remove: ").strip()
            if item in inventory:
                inventory.remove(item)
                print(f'[SUCCESS] "{item}" removed from inventory.')
            else:
                print("[ERROR] Item not found.")
        elif choice == "4":
            inventory.sort()
            print("[SUCCESS] Inventory sorted alphabetically.\nUpdated Inventory:")
            for number, item in enumerate(inventory, 1):
                print(f"{number}. {item}")
        elif choice == "5":
            print("Thank you for using the Inventory System. Goodbye!")
            break
        else:
            print("[ERROR] Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
