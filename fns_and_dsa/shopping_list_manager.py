# shopping_list_manager.py

def display_menu():
    print(f" Shopping List Manager")
    print("1. Add item")
    print("2. Remove  item")
    print("3. View list")
    print("4. Exit")


def main():
    shopping_list = []  # Start with an empty shopping list

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":  # Prompt for add an item

            item = input("Enter the item to add: ").strip()
            if item:  # only add non-empty items
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print(" Item name cannot be empty.")

        elif choice == "2": # Prompt for remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f" '{item}' has been removed from your shopping list.")
            else:
                print(f" '{item}' not found in your shopping list.")

        elif choice == "3":  # Display the shopping list
            if shopping_list:
                print(" Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print(" Your shopping list is currently empty.")

        elif choice == "4":
            print("  Goodbye!")
            break

        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

def main():
    shopping_list = []  # Start with an empty shopping list

    while True:
        print(f" Shopping List Manager")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View shopping list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f" '{item}' has been added to your shopping list.")
            else:
                print(" Item name cannot be empty.")

        elif choice == "2":
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f" '{item}' has been removed from your shopping list.")
            else:
                print(f" '{item}' not found in your shopping list.")

        elif choice == "3":
            if shopping_list:
                print(" Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print(" Your shopping list is currently empty.")

        elif choice == "4":
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice. Please enter a number between 1 and 4.")
