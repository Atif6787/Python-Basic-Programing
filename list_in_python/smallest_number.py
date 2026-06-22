# Find the smallest number in a list.

a = [23, 56, 34, 56, 34, 89]
smallest_number = a[0]
for i in a:
    if i < smallest_number:
        smallest_number = i
print(smallest_number)