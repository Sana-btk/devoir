
numbers = [1, 2, 3, 4, 5]

def display_list():
    print("Updated List:", numbers)

while True:
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Quit")

    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue

    if choice == 1:
       
        try:
            value = int(input("Enter value to append: "))
            numbers.append(value)
            display_list()
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    elif choice == 2:
        
        try:
            value = int(input("Enter value to insert: "))
            index = int(input("Enter index to insert at: "))
            if 0 <= index <= len(numbers):
                numbers.insert(index, value)
                display_list()
            else:
                print("Index out of range.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    elif choice == 3:
       
        try:
            index = int(input("Enter index to pop: "))
            if 0 <= index < len(numbers):
                numbers.pop(index)
                display_list()
            else:
                print("Index out of range.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except IndexError:
            print("Invalid index for pop operation.")

    elif choice == 4:
       
        try:
            value = int(input("Enter value to remove: "))
            if value in numbers:
                numbers.remove(value)
                display_list()
            else:
                print(f"Value {value} not found in the list.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    elif choice == 5:
       
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose a number between 1 and 5.")
