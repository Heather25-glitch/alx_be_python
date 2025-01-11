def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize the shopping list as an empty list
    
    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ")  # Get user input for the menu option
        
        if choice == '1':  # Add item to the shopping list
            item = input("Enter the item to add: ")  # Ask user for the item name
            shopping_list.append(item)  # Append the item to the shopping list
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == '2':  # Remove item from the shopping list
            item = input("Enter the item to remove: ")  # Ask user for the item to remove
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item if it exists
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == '3':  # View the shopping list
            if shopping_list:
                print("Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is currently empty.")
        
        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()
