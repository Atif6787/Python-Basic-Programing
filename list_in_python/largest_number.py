# Find the largest number in a list.
a = [23, 56, 34, 56, 34, 89]
largest_number = a[0]
for i in a:
    if i > largest_number:
        largest_number = i
print(largest_number)