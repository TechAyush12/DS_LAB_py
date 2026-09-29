# Student Record Management System
# Using Singly Linked List

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # Add Student
    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Student added successfully.")

    # Display Students
    def display(self):
        if self.head is None:
            print("No records found.")
            return

        temp = self.head

        print("\nRoll No\tName\tMarks")
        print("------------------------")

        while temp:
            print(temp.roll, "\t", temp.name, "\t", temp.marks)
            temp = temp.next

    # Search Student
    def search(self, roll):
        temp = self.head

        while temp:
            if temp.roll == roll:
                print("\nStudent Found")
                print("Roll No:", temp.roll)
                print("Name:", temp.name)
                print("Marks:", temp.marks)
                return
            temp = temp.next

        print("Student not found.")

    # Delete Student
    def delete(self, roll):
        if self.head is None:
            print("No records found.")
            return

        # Delete first node
        if self.head.roll == roll:
            self.head = self.head.next
            print("Student deleted.")
            return

        temp = self.head

        while temp.next:
            if temp.next.roll == roll:
                temp.next = temp.next.next
                print("Student deleted.")
                return
            temp = temp.next

        print("Student not found.")

    # Update Student
    def update(self, roll):
        temp = self.head

        while temp:
            if temp.roll == roll:
                temp.name = input("Enter new name: ")
                temp.marks = float(input("Enter new marks: "))
                print("Student updated.")
                return
            temp = temp.next

        print("Student not found.")

    # Sort Students
    def sort(self, choice, order):
        if self.head is None:
            print("No records found.")
            return

        current = self.head

        while current:
            temp = current.next

            while temp:
                if choice == 1:       # Sort by Roll No
                    a = current.roll
                    b = temp.roll
                else:                 # Sort by Marks
                    a = current.marks
                    b = temp.marks

                # Ascending
                if (order == 1 and a > b):
                    self.swap(current, temp)

                # Descending
                elif order == 2 and a < b:
                    self.swap(current, temp)

                temp = temp.next

            current = current.next

        print("Records sorted successfully.")

    # Swap data
    def swap(self, a, b):
        a.roll, b.roll = b.roll, a.roll
        a.name, b.name = b.name, a.name
        a.marks, b.marks = b.marks, a.marks


# Main Program
students = StudentList()

while True:

    print("\n===== STUDENT RECORD MANAGEMENT =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display Students")
    print("6. Sort Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students.add(roll, name, marks)

    elif choice == 2:
        roll = int(input("Enter Roll No: "))
        students.delete(roll)

    elif choice == 3:
        roll = int(input("Enter Roll No: "))
        students.update(roll)

    elif choice == 4:
        roll = int(input("Enter Roll No: "))
        students.search(roll)

    elif choice == 5:
        students.display()

    elif choice == 6:
        print("\nSort By:")
        print("1. Roll Number")
        print("2. Marks")

        sort_choice = int(input("Enter choice: "))

        print("\nOrder:")
        print("1. Ascending")
        print("2. Descending")

        order = int(input("Enter choice: "))

        students.sort(sort_choice, order)

    elif choice == 7:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")