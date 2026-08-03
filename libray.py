n = int(input("Enter number of books: "))

book_names = []
borrow_counts = []

for i in range(n):
    name = input("Enter book name: ")
    count = int(input("Enter borrow count: "))
    book_names.append(name)
    borrow_counts.append(count)

# 1. Average borrow count
average = sum(borrow_counts) / n
print("\nAverage borrow count =", average)

# 2. Highest and Lowest borrowed book
max_count = max(borrow_counts)
min_count = min(borrow_counts)

print("Highest borrowed book:", book_names[borrow_counts.index(max_count)], "-", max_count)
print("Lowest borrowed book:", book_names[borrow_counts.index(min_count)], "-", min_count)

# 3. Count books with zero borrowings
zero_count = borrow_counts.count(0)
print("Books not borrowed:", zero_count)

# 4. Find Mode (Most frequent borrow count)
mode = borrow_counts[0]
max_frequency = 0

for i in borrow_counts:
    frequency = borrow_counts.count(i)
    if frequency > max_frequency:
        max_frequency = frequency
        mode = i

print("Most frequent borrow count (Mode):", mode)
