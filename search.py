def linear_search(customer_list, target_element):
    found = False

    for i in range(len(customer_list)):
        if customer_list[i] == target_element:
            print(f"Customer ID is found at index {i}")
            found = True
            break

    if not found:
        print("Not found")


def binary_search(customer_list, target_element):
    customer_list = sorted(customer_list)

    left = 0
    right = len(customer_list) - 1
    found = False

    while left <= right:
        mid = (left + right) // 2

        if customer_list[mid] == target_element:
            print(f"Target element is found at index {mid}")
            found = True
            break

        elif customer_list[mid] < target_element:
            left = mid + 1

        else:
            right = mid - 1

    if not found:
        print("Not found")


# Main Program
num = int(input("Enter the number of customers you want to enter: "))

customer_list = []


for i in range(1, num + 1):
    element = int(input(f"Enter element {i}: "))
    customer_list.append(element)
target_num = int(input("Enter the number you want to search: "))

result = int(input("Enter choice (1 for Linear Search, 0 for Binary Search): "))

if result == 0:
    binary_search(customer_list, target_num)

elif result == 1:
    linear_search(customer_list, target_num)

else:
    print("Wrong choice")