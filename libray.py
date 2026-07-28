# Borrow counts of library members
books = [3, 0, 5, 2, 0, 4, 3, 5, 1, 3, 2]

# Average number of books borrowed
total = sum(books)
average = total / len(books)
print("Average books borrowed =", average)

# Highest and lowest borrow count
print("Highest borrow count =", max(books))
print("Lowest borrow count =", min(books))

# Members who did not borrow any books
count = 0
for i in books:
    if i == 0:
        count = count + 1
print("Members with no borrowed books =", count)

# Finding the mode (most frequent borrow count)
freq = {}

for i in books:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

mode = books[0]
max_count = freq[mode]

for i in freq:
    if freq[i] > max_count:
        max_count = freq[i]
        mode = i

print("Most frequently borrowed count =", mode)