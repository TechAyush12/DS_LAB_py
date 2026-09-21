# Undo-Redo System using Stack

undo_stack = []
redo_stack = []
document = ""

while True:
    print("\n--- Text Editor ---")
    print("1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        change = input("Enter text to add: ")

        document = document + change

        # Store change in Undo Stack
        undo_stack.append(change)

        # Clear Redo Stack after new change
        redo_stack.clear()

        print("Change added successfully.")

    elif choice == 2:
        if len(undo_stack) == 0:
            print("Nothing to Undo!")
        else:
            change = undo_stack.pop()

            # Remove last change from document
            document = document[:-len(change)]

            # Store change in Redo Stack
            redo_stack.append(change)

            print("Undo successful.")

    elif choice == 3:
        if len(redo_stack) == 0:
            print("Nothing to Redo!")
        else:
            change = redo_stack.pop()

            # Reapply the change
            document = document + change

            # Store back in Undo Stack
            undo_stack.append(change)

            print("Redo successful.")

    elif choice == 4:
        print("\nCurrent Document:", document)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")